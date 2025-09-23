---
status: doing
tags:
  - 'guide'
  - 'sw/nix'
---


# nixpkgs

## how can multiple packages in nixpkgs have different versions of the same dependency if there is only one derivation of each dependency

#### ChatGPT:
In Nixpkgs, while there may be only one *default* derivation of each dependency, Nix's functional and declarative nature allows multiple packages to depend on different versions of the same dependency. This is achieved through various mechanisms, such as package overrides, versioned attributes, and the use of overlays. Here's how multiple packages can have different versions of the same dependency:

---

### **1. Multiple Versions in Nixpkgs**

- **Versioned Attributes**:
  - Nixpkgs often provides multiple versions of a package under different attribute names.
  - For example, you might find both `openssl` (default version) and `openssl_1_1` in Nixpkgs.

- **Accessing Specific Versions**:
  - You can explicitly reference the versioned attributes when defining dependencies.
  - This allows packages to depend on different versions of the same dependency.

**Example**:

```nix
# Using different versions of OpenSSL
openssl_1_1 = pkgs.openssl_1_1;
openssl_3_0 = pkgs.openssl_3_0;
```

---

### **2. Functional Package Definitions**

- **Packages as Functions**:
  - In Nix, packages are defined as functions that take their dependencies as arguments.
  - This allows you to pass different versions of dependencies to the package functions.

- **Parameterization**:
  - By parameterizing packages, you can create new derivations with different dependencies.

**Example**:

```nix
# Override the OpenSSL dependency for a package
myPackage = pkgs.myPackage.override {
  openssl = pkgs.openssl_1_1;
};
```

---

### **3. Package Overrides**

- **`override` and `overrideAttrs`**:
  - Use these functions to modify a package's dependencies or attributes.
  - They create a new derivation with the changes applied.

- **Overriding Dependencies**:
  - You can override a package's dependencies to use different versions.

**Example**:

```nix
myPackage = pkgs.myPackage.override {
  openssl = pkgs.openssl_3_0;
};
```

---

### **4. Overlays**

- **Nixpkgs Overlays**:
  - Overlays allow you to extend or modify Nixpkgs without altering the original package set.
  - You can add new packages or override existing ones.

- **Defining an Overlay**:

  ```nix
  self: super: {
    myPackage = super.myPackage.override {
      openssl = super.openssl_1_1;
    };
  }
  ```

- **Using the Overlay**:

  ```nix
  {
    nixpkgs.overlays = [ (import ./overlay.nix) ];
  }
  ```

---

### **5. Call Packages Pattern**

- **`callPackage` Function**:
  - Nixpkgs uses `callPackage` to automatically provide dependencies to packages.
  - You can create your own `callPackage` to inject different dependencies.

**Example**:

```nix
myCallPackage = pkgs.callPackageWith (pkgs // { openssl = pkgs.openssl_1_1; });

myPackage = myCallPackage ./path/to/my-package.nix;
```

---

### **6. Using Different Package Sets**

- **Custom Package Sets**:
  - You can define custom package sets that use different versions of dependencies.

- **Example**:

  ```nix
  let
    myPkgs = import <nixpkgs> {
      overlays = [
        (self: super: {
          openssl = super.openssl_1_1;
        })
      ];
    };
  in
  myPkgs.myPackage
  ```

---

### **7. Multiple Outputs and Subpackages**

- **Splitting Packages**:
  - Packages can be split into multiple outputs (`out`, `dev`, `doc`, etc.).
  - This helps manage dependencies more granularly.

- **Including Specific Outputs**:

  ```nix
  myPackage = pkgs.myPackage;
  myPackageDev = pkgs.myPackage.dev;
  ```

---

### **8. Handling Conflicts**

- **Isolation in Nix Store**:
  - Each package version is stored in a unique path in the Nix store.
  - Different versions of a dependency do not interfere with each other at the storage level.

- **Avoiding Symlink Collisions**:
  - When including packages in `environment.systemPackages`, conflicts can occur if files overlap.
  - Use custom build environments or avoid including conflicting packages globally.

---

### **9. Custom Build Environments**

- **`buildEnv` Function**:
  - Create custom environments that include specific versions of packages.

- **Example**:

  ```nix
  myEnv = pkgs.buildEnv {
    name = "myEnv";
    paths = [ pkgs.packageA pkgs.packageB ];
  };
  ```

---

### **10. Practical Example**

Suppose you have two packages that require different versions of the same dependency:

- **Packages**:
  - `app1` requires `libfoo-1.0`
  - `app2` requires `libfoo-2.0`

- **Available Versions in Nixpkgs**:
  - `libfoo` (default version 2.0)
  - `libfoo_1` (version 1.0)

**Steps**:

1. **Override Dependencies**:

   ```nix
   app1 = pkgs.app1.override {
     libfoo = pkgs.libfoo_1;
   };

   app2 = pkgs.app2; # Uses default libfoo
   ```

2. **Include in Configuration**:

   ```nix
   {
     environment.systemPackages = with pkgs; [
       app1
       app2
     ];
   }
   ```

3. **Result**:

   - Both `app1` and `app2` are built with their required versions of `libfoo`.
   - No conflicts occur because each package uses its own dependency within the Nix store.

---

### **11. Nix Flakes and Inputs**

- **Flakes**:
  - Flakes provide a way to define precise inputs for your packages.
  - You can specify exact versions of dependencies.

- **Overriding Inputs**:

  ```nix
  {
    inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

    outputs = { self, nixpkgs }: {
      packages.x86_64-linux.myPackage = import nixpkgs {
        overlays = [ (final: prev: {
          openssl = prev.openssl_1_1;
        }) ];
      }.myPackage;
    };
  }
  ```

---

### **12. Considerations**

- **Dependency Trees**:
  - Changing a dependency version may require rebuilding dependent packages.
  - Ensure compatibility when overriding dependencies.

- **Reproducibility**:
  - By explicitly specifying dependency versions, builds remain reproducible.

- **Conflict Resolution**:
  - Be cautious of file collisions in symlinked directories.
  - Avoid including conflicting packages in `environment.systemPackages` directly.

---

### **13. Community Practices**

- **Maintainers Providing Versions**:
  - Nixpkgs maintainers often include multiple versions of critical libraries.
  - This supports packages that require older or specific versions.

- **Contributing New Versions**:
  - You can contribute additional versions of packages to Nixpkgs if needed.

---

### **14. Summary**

- **Functional Package Definitions**:
  - Packages are functions of their dependencies, allowing customization.

- **Multiple Versions Coexist**:
  - Different versions of dependencies can coexist in the Nix store.

- **Overrides and Overlays**:
  - Use overrides and overlays to specify different dependency versions.

- **Isolation**:
  - Package isolation in the Nix store prevents conflicts between versions.

- **Explicit Dependency Management**:
  - Explicitly managing dependencies ensures compatibility and reproducibility.
    