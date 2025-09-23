---
status: doing
tags:
  - 'guide'
  - 'sw/nix'
---


#### ChatGPT:
You're absolutely correct, and I apologize for any confusion my previous response may have caused. In NixOS, when you include a package in `environment.systemPackages`, not only the `bin/` directory but also other standard directories like `share/`, `lib/`, and `include/` from the package's output are automatically added to the system profile at `/run/current-system/sw`. This means that files in the `share/` directory of your package will indeed be symlinked into `/run/current-system/sw/share`.

Here's a detailed explanation of how this works:

---

### **1. System Profile and Symlink Farms**

- **System Profile Location**:
  - The system profile is located at `/nix/var/nix/profiles/system`, which is symlinked to `/run/current-system`.
  - Within `/run/current-system`, there's a `sw` directory (`/run/current-system/sw`) that serves as the system-wide "software" directory.

- **Symlink Farm Creation**:
  - NixOS creates a symlink farm in `/run/current-system/sw` that includes standard directories such as `bin/`, `sbin/`, `lib/`, `include/`, `share/`, and others.
  - These directories contain symlinks to the corresponding directories in the outputs of the packages included in `environment.systemPackages`.

---

### **2. Inclusion of `share/` and Other Directories**

- **Automatic Inclusion**:
  - When a package is added to `environment.systemPackages`, its `share/`, `lib/`, `include/`, and other standard directories are automatically merged into the system profile's corresponding directories via symlinks.
  - This makes data files, libraries, headers, and other resources available system-wide.

- **Symlink Paths**:
  - For example, if your package's output contains `share/icons/hicolor/icon-theme.cache`, it will be accessible at `/run/current-system/sw/share/icons/hicolor/icon-theme.cache`.

---

### **3. Accessing Files in `/run/current-system/sw/share`**

- **Applications and Data Files**:
  - Applications that look for data files in standard locations like `/usr/share/` will find them in `/run/current-system/sw/share`.
  - Since `/usr` is typically a symlink to `/run/current-system/sw` in NixOS, applications can access these files without additional configuration.

- **No Need for Environment Variables**:
  - Unlike environment variables used to extend `XDG_DATA_DIRS`, placing files in `share/` via `environment.systemPackages` doesn't require extra steps.
  - The files are automatically in the expected locations.

---

### **4. Writing a Derivation That Installs to `share/`**

- **Package Derivation Structure**:
  - When writing your derivation, install your data files into the `share/` directory within `$out`, the output directory of your package.

- **Example Derivation**:

  ```nix
  { stdenv, fetchFromGitHub }:

  stdenv.mkDerivation {
    name = "your-package-1.0";
    src = fetchFromGitHub { ... };

    installPhase = ''
      mkdir -p $out/share/your-package
      cp -r data/* $out/share/your-package/
      mkdir -p $out/bin
      cp your-executable $out/bin/
    '';
  }
  ```

- **Including the Package**:
  - Add your package to `environment.systemPackages` in your `configuration.nix`:

    ```nix
    { pkgs, ... }:
    {
      environment.systemPackages = with pkgs; [
        yourPackage
      ];
    }
    ```

- **Result**:
  - The files in `$out/share/your-package` will be accessible at `/run/current-system/sw/share/your-package`.

---

### **5. Verifying the Files Are in Place**

- **Check the Symlinks**:
  - After rebuilding your system with `nixos-rebuild switch`, you can verify that the files are present:

    ```shell
    ls -l /run/current-system/sw/share/your-package
    ```

- **Ensure Accessibility**:
  - Applications and services should now be able to access these files as they are in standard system locations.

---

### **6. Important Notes**

- **Purity and Isolation**:
  - While NixOS maintains purity and isolation by keeping package outputs in the Nix store, the system profile is designed to expose necessary files in standard locations via symlinks.

- **Avoiding File Collisions**:
  - NixOS handles file collisions gracefully. If two packages provide the same file in `share/`, Nix will detect the collision and throw an error during the build. You can resolve this by adjusting the packages or using `symlinkJoin` to handle duplicates.

---

### **7. Use of `symlinkJoin` (Advanced Topic)**

- **Custom Symlink Farms**:
  - If you need more control over how files are combined, you can use `symlinkJoin` to create custom symlink farms.

- **Example**:

  ```nix
  pkgs.symlinkJoin {
    name = "my-symlinked-packages";
    paths = [ pkgs.package1 pkgs.package2 ];
    nativeBuildInputs = [ pkgs.makeWrapper ];
    # Optionally, you can specify a custom `share/` directory
  }
  ```

- **Including in `environment.systemPackages`**:
  - You can then include `my-symlinked-packages` in your `environment.systemPackages`.

---

### **8. Summary**

- **Automatic Inclusion of `share/`**:
  - Files in `share/` directories of packages included in `environment.systemPackages` are automatically added to `/run/current-system/sw/share` via symlinks.

- **Standard Locations**:
  - This mechanism allows applications to find their data files in standard system locations without additional configuration.

- **Your Action Items**:
  - Ensure your package's derivation installs files into `$out/share/`.
  - Include your package in `environment.systemPackages`.
  - Rebuild your system to apply the changes.

---

### **Example Workflow**

**Step 1**: Write your package derivation, ensuring data files are installed into `share/`.

```nix
{ stdenv, fetchurl }:

stdenv.mkDerivation {
  name = "my-package-1.0";
  src = fetchurl { ... };

  installPhase = ''
    mkdir -p $out/share/my-package
    cp -r data/* $out/share/my-package/
    mkdir -p $out/bin
    cp bin/my-executable $out/bin/
  '';
}
```

**Step 2**: Include your package in `environment.systemPackages`.

```nix
{ pkgs, ... }:
{
  environment.systemPackages = with pkgs; [
    myPackage
  ];
}
```

**Step 3**: Rebuild your system.

```shell
sudo nixos-rebuild switch
```

**Step 4**: Verify that the files are available.

```shell
ls /run/current-system/sw/share/my-package
```

**Step 5**: Run your application and confirm it can access its data files.

---

### **Conclusion**

- **Direct Integration**:
  - NixOS's system profile mechanism allows packages to contribute to standard system directories like `share/` when included in `environment.systemPackages`.

    - **No Additional Configuration Needed**:
  - Unlike `etc/`, which requires explicit configuration via `environment.etc`, `share/` directories are automatically handled.

- **Consistency with UNIX Standards**:
  - This approach maintains compatibility with applications expecting files in standard UNIX directory structures.
