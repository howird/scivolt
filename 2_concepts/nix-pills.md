---
status: doing
tags:
  - '#type/tutorial'
  - '#area/swe/nix/pills'
---

# Nix Pills Notes

## Pill 6: Our First Derivation

> \[!info\]
>
> A Nix derivation is a low-level, intermediate representation used in the Nix package manager to describe how a package or a build artifact should be constructed. It contains all the information needed to build a package, including:

- `derivation` function: builtin function that is used to create a derivation

  - arg: an attribute set, [the attributes of which](https://nix.dev/manual/nix/2.22/language/derivations) specify the inputs to the process
  - returns: an attribute set, and produces a store derivation (`.drv` file in `/nix/store`) as a side effect of evaluation
    - `outPath`: path to directory in `/nix/store` where the derivation would be build

- In, `nix repl`, we ran `derivation { name = "myname"; builder = "mybuilder"; system = builtins.currentSystem; }` to create a dummy derivation

  - when we try to build it (`:b`), we get a build error as `"mybuilder"` is an invalid path

- Next , we ran `derivation { name = "myname"; builder = "${coreutils}/bin/true"; system = builtins.currentSystem; }` to get closer to

  - note: prior to this, we loaded all of `nixpkgs` with `:l <nixpkgs>`
  - notice `"${coreutils}"` outputs the `outPath` of the built `coreutils` derivation in the `/nix/store`

- We still get a build error, now it is "failed to produce an output path"

  - this is because the builder didn't actually do anything
  - at (derivation) build time, an `outPath` is generated and it is expected that something is done with that path - here the builder just returned `true`, it didn't create anything with that path

- When Nix builds a derivation, it first creates a `.drv` file from a derivation expression, and uses it to build the output

## Pill 7: First Working Derivation

- In the last pill, our derivation didn't do anything with the `outPath` leading to our error
- We solve this by building: `derivation { name = "foo"; builder = "${bash}/bin/bash"; args = [./builder.sh]; system = builtins.currentSystem; }` where `builder.sh` is:

```bash
declare -xp
echo foo > $out
```

- Now, at build time, this builder script is run, which writes `"foo"` to the `outPath`. Note:

  - the `outPath` can be accessed as the environment variable `$out` by the builder
  - `declare -xp` is used to print the environment variables available when the script is run
    - nix intercepts the stderr and stdout to create build logs which can be accessed with: `nix-store --read-log <outPath>`

- Next, we stop using the `nix repl` and simply run the `nix-build` command on a file:

```nix
let
  pkgs = import <nixpkgs> { };
in
derivation {
  name = "simple";
  builder = "${pkgs.bash}/bin/bash";
  args = [ ./simple_builder.sh ];
  gcc = pkgs.gcc;
  coreutils = pkgs.coreutils;
  src = ./simple.c;
  system = builtins.currentSystem;
}
```
