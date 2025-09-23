---
tags:
  - note
  - sw/nix
status: done
---
# Nix Derivation Phases and Hooks Explained

In Nix, package builds are divided into **phases** to provide modularity and flexibility. Understanding these phases, how to control them, and the impact of various **hooks** is essential for effective package management. Below is a concise guide to each phase, the variables that affect them, and how certain hooks influence the build process.

## Controlling Phases

### Phase Control Variables

- **`phases`**: Specifies the list and order of phases to execute. Defaults to a standard sequence but can be customized if necessary.
  - **Usage**: Generally discouraged to set directly; prefer using the `*Phases` variables.
- **`prePhases` / `postPhases`**: Add custom phases before or after the default phases.
- **`preConfigurePhases`, `preBuildPhases`, `preInstallPhases`, `preFixupPhases`, `preDistPhases`**: Insert custom phases before specific default phases.

**Note**: It's recommended to use `pre*Phases` and `post*Phases` variables to modify the build process instead of overriding `phases`.

## Phases Overview

### 1. Unpack Phase

**Purpose**: Unpacks the source code into the build directory.

**Key Variables**:

- **`src` / `srcs`**: Source file(s) or directories to unpack.
- **`sourceRoot`**: Directory to change into after unpacking.
- **`setSourceRoot`**: Shell command to set `sourceRoot` dynamically.
- **`dontUnpack`**: Set to `true` to skip this phase.
- **Hooks**:
  - **`preUnpack`**: Commands to run before unpacking.
  - **`postUnpack`**: Commands to run after unpacking.

### 2. Patch Phase

**Purpose**: Applies patches to the source code.

**Key Variables**:

- **`patches`**: List of patch files to apply.
- **`patchFlags`**: Flags passed to the `patch` command (default is `-p1`).
- **`dontPatch`**: Set to `true` to skip this phase.

- **Hooks**:
    - **`prePatch`**: Commands to run before patching.
    - **`postPatch`**: Commands to run after patching.

### 3. Configure Phase

**Purpose**: Prepares the build system (e.g., runs `./configure`).

**Key Variables**:

- **`configureScript`**: Path or command to run as the configure script.
- **`configureFlags`**: Additional flags for the configure script.
- **`dontConfigure`**: Set to `true` to skip this phase.
- **`prefix`**: Installation prefix (defaults to `$out`).
- **`dontAddPrefix`**: Prevents automatic addition of `--prefix`.

- **Hooks**:
    - **`preConfigure`**: Commands to run before configuring.
    - **`postConfigure`**: Commands to run after configuring.

#### CMake Hook

- **Purpose**: Overrides the default configure phase to run the `cmake` command.
- **Activation**: Automatically used when `cmake` is in `nativeBuildInputs`.
- **Control Variables**:
  - **`dontUseCmakeConfigure`**: Set to `true` to disable the `cmakeConfigurePhase`.
  - **`cmakeFlags`**: Additional flags passed to `cmake`.
  - **`cmakeBuildDir`**: Directory where CMake places build files (default is `build`).
- **Effect on Phase**: Replaces the standard `configurePhase` with `cmakeConfigurePhase`.

**Notes**:

- Detects and uses Ninja generator if `ninja` is in `nativeBuildInputs`.
- Automatically adds dependencies to `CMAKE_PREFIX_PATH`.
- Enables parallel building by default.

### 4. Build Phase

**Purpose**: Compiles the source code.

**Key Variables**:

- **`dontBuild`**: Set to `true` to skip this phase.
- **`makeFlags` / `makeFlagsArray`**: Flags passed to `make`.
- **`buildFlags` / `buildFlagsArray`**: Flags specific to the build phase.
- **Hooks**:
  - **`preBuild`**: Commands to run before building.
  - **`postBuild`**: Commands to run after building.

### 5. Check Phase

**Purpose**: Runs the package's test suite.

**Key Variables**:

- **`doCheck`**: Set to `true` to enable this phase.
- **`checkTarget`**: Make target for running tests.
- **`checkFlags` / `checkFlagsArray`**: Flags specific to the check phase.
- **`checkInputs`**: Host dependencies needed during testing.
- **`nativeCheckInputs`**: Native build inputs needed during testing.

- **Hooks**:
    - **`preCheck`**: Commands to run before testing.
    - **`postCheck`**: Commands to run after testing.

**Note**: Tests are not run during cross-compilation.

### 6. Install Phase

**Purpose**: Installs the built package into the `$out` directory.

**Key Variables**:

- **`dontInstall`**: Set to `true` to skip this phase.
- **`installTargets`**: Make targets for installation (defaults to `install`).
- **`installFlags` / `installFlagsArray`**: Flags specific to the install phase.
- **Hooks**:
  - **`preInstall`**: Commands to run before installing.
  - **`postInstall`**: Commands to run after installing.

### 7. Fixup Phase

**Purpose**: Performs post-processing tasks like stripping binaries and fixing RPATHs.

**Key Variables**:

- **`dontFixup`**: Set to `true` to skip this phase.
- **`dontStrip`**: Prevents stripping of binaries.
- **`stripDebugList`**: Directories to strip debug symbols from.
- **`dontPatchELF`**: Disables `patchelf` usage on Linux.
- **`dontPatchShebangs`**: Prevents shebang rewriting.
- **`setupHook`**: Specifies a setup hook script.
- **Hooks**:
    - **`preFixup`**: Commands to run before fixup
    - **`postFixup`**: Commands to run after fixup

#### autoPatchelfHook

- **Purpose**: Automatically finds and patches missing shared library dependencies in ELF files.
- **Activation**: Include `autoPatchelfHook` in `nativeBuildInputs`.
- **Control Variables**:
  - **`dontAutoPatchelf`**: Set to a non-empty value to disable automatic patching.
  - **`autoPatchelfIgnoreMissingDeps`**: List of dependencies to ignore if missing.
  - **`runtimeDependencies`**: List of dependencies to add unconditionally to RPATH.
- **Effect on Phase**: Enhances the `fixupPhase` by automatically patching ELF files.

**Notes**:

- Useful for packaging proprietary software.
- By default, fails if any dependency is missing unless configured otherwise.
- Can specify `autoPatchelfIgnoreMissingDeps = [ "*" ]` to ignore all missing dependencies.

### 8. InstallCheck Phase

**Purpose**: Runs tests on the installed package.

**Key Variables**:

- **`doInstallCheck`**: Set to `true` to enable this phase.
- **`installCheckTarget`**: Make target for install checks.
- **`installCheckFlags` / `installCheckFlagsArray`**: Flags specific to the installCheck phase.
- **`installCheckInputs`**: Host dependencies for install checks.
- **`nativeInstallCheckInputs`**: Native build inputs for install checks.

- **Hooks**:
    - **`preInstallCheck`**: Commands to run before install checks.
    - **`postInstallCheck`**: Commands to run after install checks.

### 9. Distribution Phase

**Purpose**: Generates source distributions of the package.

**Key Variables**:

- **`doDist`**: Set to `true` to enable this phase.
- **`distTarget`**: Make target for distribution.
- **`distFlags` / `distFlagsArray`**: Flags specific to the distribution phase.
- **`tarballs`**: Patterns of tarball files to copy to `$out/tarballs/`.
- **`dontCopyDist`**: Prevents copying tarballs.

- **Hooks**:
    - **`preDist`**: Commands to run before distribution.
    - **`postDist`**: Commands to run after distribution.

## Additional Setup Hooks

### pkg-config Hook

- **Purpose**: Adds `lib/pkgconfig` and `share/pkgconfig` directories of build inputs to the `PKG_CONFIG_PATH`
- **Activation**: Automatically used when `pkg-config` is in `nativeBuildInputs`
- **Effect on Phases**:
    - **Configure Phase**: Ensures that `pkg-config` can find dependencies during configuration.
    - **Build Phase**: Assists in locating libraries and packages.

## Shell Functions and Utilities

### Common Functions

- **`runHook <hook>`**: Executes the specified hook and associated array hooks.
- **`makeWrapper`**: Creates wrapper scripts for executables
- **`wrapProgram`**: Convenience function to replace an executable with a wrapper
- **`substitute` / `substituteInPlace`**: Performs string substitutions in files
- **`substituteAll` / `substituteAllInPlace`**: Replaces `@varName@` with environment variables in files
- **`prependToVar` / `appendToVar`**: Modifies variables by adding elements

## Best Practices

- **Hooks**: When overriding a phase, always include `runHook prePhase` at the beginning and `runHook postPhase` at the end to ensure that all hooks are executed.
- **Avoid Overriding Phases Entirely**: Instead of replacing a phase, use `prePhase` and `postPhase` hooks to add commands.
- **Use `makeFlags` and `*Flags` Variables Appropriately**: Utilize these variables to pass necessary flags to `make` and other build tools without modifying the default build scripts.
- **Enabling Hooks**:
    - **CMake Hook**: Add `cmake` to `nativeBuildInputs`; control with `dontUseCmakeConfigure`.
    - **autoPatchelfHook**: Add `autoPatchelfHook` to `nativeBuildInputs`; control with `dontAutoPatchelf`.
    - **pkg-config Hook**: Add `pkg-config` to `nativeBuildInputs`.

---

By understanding and utilizing these phases, variables, and hooks, you can customize the build process of Nix packages effectively while maintaining clean and maintainable expressions.