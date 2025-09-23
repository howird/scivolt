---
tags:
  - note
  - sw/nix/os
status: doing
---

# NixOS Current System Build

In NixOS, the `/run/current-system` directory is a symbolic link to the current system generation stored in the Nix store. This setup is part of how NixOS achieves atomic upgrades and rollbacks, allowing you to switch between different system configurations seamlessly. Here's how NixOS builds and manages the `/run/current-system` folder:

1. **Configuration Definition**:
   - You define your system's configuration in `/etc/nixos/configuration.nix` and any additional imported `.nix` files.
   - This configuration includes system packages, services, user settings, and more.

2. **Building the System Derivation**:
   - When you run `nixos-rebuild switch` (or `boot`, `test`, etc.), Nix evaluates your configuration.
   - Nix constructs a *system derivation*, which is a build recipe that describes all packages, configurations, and services for your system.
   - The top-level system derivation is defined in the Nixpkgs repository, typically in `nixos/modules/system/activation/top-level.nix`.

3. **Storing in the Nix Store**:
   - The system derivation is built and stored in the Nix store under a unique path like `/nix/store/<hash>-nixos-system-<hostname>-<version>`.
   - The `<hash>` is derived from the contents of the derivation, ensuring that identical configurations result in the same store path.

4. **Activation Scripts**:
   - Alongside the system derivation, NixOS generates activation scripts.
   - These scripts handle tasks like updating system links, migrating system state, and starting services.

5. **Updating `/run/current-system`**:
   - During activation (triggered by `nixos-rebuild switch`), the activation script updates the `/run/current-system` symbolic link to point to the new system generation in the Nix store.
   - This link effectively tells the system which configuration is the "current" one.

6. **System State Management**:
   - The system maintains a list of generations in `/nix/var/nix/profiles/system-*`.
   - You can list and manage these generations using `nix-env --list-generations` and roll back if needed.

7. **Boot Loader Integration**:
   - The boot loader (like GRUB) is updated to include entries for the new system generation.
   - This allows you to select different system configurations at boot time.

**Summary**:

The `/run/current-system` directory in NixOS is a symbolic link that points to the current system generation built based on your NixOS configuration. When you rebuild your system, NixOS:

- Evaluates your configuration to produce a new system derivation.
- Builds this derivation and stores it in the Nix store.
- Updates the `/run/current-system` link during the activation phase to point to the new derivation.
- Manages system generations to allow easy rollbacks and system management.

This process ensures that your system is built declaratively, with all configurations and packages specified in a reproducible manner, providing consistency and reliability across system builds.


# How does each derivation contribute files in nixos

#### ChatGPT:
In NixOS, each derivation (which can represent a package, a service, or a configuration module) contributes files to the system in a controlled and composable way. The process is managed by the Nix package manager and the NixOS module system, which together ensure that the system is built declaratively and reproducibly. Here's how each derivation contributes files to NixOS:

---

### **1. Derivation Outputs in the Nix Store**

- **Isolation of Outputs**:
  - Each derivation builds its output in a unique directory within the Nix store, typically under `/nix/store/<hash>-<name>`.
  - The `<hash>` is derived from the derivation's inputs, ensuring that identical inputs produce the same output path.

- **Contents of Outputs**:
  - The output can include binaries, libraries, headers, documentation, configuration files, and any other resources the package provides.
  - These files are stored in standard subdirectories within the derivation output, such as `bin/`, `lib/`, `include/`, and `share/`.

---

### **2. Composition into the System Derivation**

- **System Derivation as an Aggregator**:
  - The NixOS system is itself a derivation called the **system derivation**.
  - Defined in Nixpkgs (the Nix Packages collection), it aggregates all the packages and configurations specified in your NixOS configuration.

- **NixOS Modules**:
  - NixOS uses a module system where each module defines options and configurations.
  - Modules can represent services, hardware configurations, user settings, etc.
  - They contribute to a global configuration by exporting settings that are merged according to predefined rules.

---

### **3. Merging Configurations and Files**

- **Attribute Set Merging**:
  - Nix's lazy functional language allows for the merging of attribute sets.
  - When multiple modules define the same option, they are combined according to the option's **merge semantics** (e.g., lists are concatenated, strings are overridden or combined).

- **Generating Configuration Files**:
  - Configuration files in `/etc/` are often generated by combining inputs from various modules.
  - For example, `/etc/ssh/sshd_config` might be generated by combining settings from the SSH service module and any user overrides.

---

### **4. Activation Scripts**

- **Purpose of Activation Scripts**:
  - The system derivation includes activation scripts that are executed when you switch to a new system generation.
  - These scripts handle tasks like updating symlinks, migrating state directories, and starting or reloading services.

- **Creating Symlinks and Directories**:
  - The activation script sets up necessary directories in `/var/`, `/etc/`, and other system paths.
  - It creates symlinks from the Nix store to standard system locations when necessary.

---

### **5. Symlinked Profiles and Environments**

- **System Profile**:
  - The system profile is a symlink located at `/nix/var/nix/profiles/system`.
  - It points to the current system generation, which is a symlink to the system derivation in the Nix store.

- **User Environments**:
  - For user-level packages, profiles are managed per user and are located in `/nix/var/nix/profiles/per-user/<username>/`.

- **Symlink Farms**:
  - Nix creates symlink farms where each package's binaries are symlinked into a `bin/` directory, making them available in the user's `$PATH`.

---

### **6. Handling File Collisions and Conflicts**

- **Namespace Isolation**:
  - Since each derivation's output is isolated in its own Nix store path, file collisions are avoided at the storage level.

- **Combining Files**:
  - When files need to be combined (e.g., shell profiles, configuration files), NixOS uses explicit mechanisms to merge them.
  - For example, the `environment.etc` option allows you to define entries in `/etc/`, specifying how files from different modules should be combined.

- **Conflict Detection**:
  - If two modules try to define the same option without a defined merge strategy, Nix will throw an error during evaluation, prompting you to resolve the conflict.

---

### **7. Services and Systemd Units**

- **Service Definitions**:
  - Modules defining services contribute by generating systemd unit files.
  - These units are placed in the Nix store and linked appropriately so that systemd can manage them.

- **Activation and Reloading**:
  - The activation script ensures that systemd is aware of the new or updated units.
  - Services are started, stopped, or reloaded based on changes in the configuration.

---

### **8. Hooks and Wrappers**

- **Build Hooks**:
  - During the build process, derivations can specify hooks that run at certain stages (e.g., post-install).
  - Hooks can modify files, set permissions, or perform other necessary adjustments.

- **Binary Wrappers**:
  - Some binaries are wrapped with scripts that set environment variables or adjust runtime behavior.
  - This ensures that binaries find their dependencies and function correctly within the Nix environment.

---

### **9. Example Workflow**

**Including a Package**:

- **Step 1**: You add `firefox` to your `environment.systemPackages` in `configuration.nix`.
- **Step 2**: Nix evaluates the `firefox` derivation, building it if necessary.
- **Step 3**: The `firefox` output is placed in the Nix store under its unique path.
- **Step 4**: The system derivation includes `firefox` in its closure.
- **Step 5**: During activation, symlinks to `firefox` binaries are created in the system profile's `bin/` directory.
- **Step 6**: `firefox` becomes available system-wide via the `$PATH` environment variable.

---

### **10. Benefits of This Approach**

- **Reproducibility**:
  - Since derivations are pure functions of their inputs, building the system from the same configuration will always yield the same outputs.

- **Atomic Upgrades and Rollbacks**:
  - Each system generation is stored separately, allowing you to switch between configurations safely.

- **Isolation and Purity**:
  - Dependencies are explicitly declared, and impurity is minimized, reducing the chance of unexpected interactions between packages.

---

### **Summary**

In NixOS, each derivation contributes files to the system through a well-defined process:

- **Build Outputs**: Derivations produce outputs stored in isolated paths within the Nix store.
- **System Composition**: The system derivation aggregates these outputs based on your configuration.
- **Activation Process**: Activation scripts set up the necessary symlinks, generate configuration files, and manage services.
- **Conflict Management**: NixOS uses explicit merging strategies and conflict detection to handle overlapping configurations.
- **Accessibility**: Symlinked profiles and environments ensure that binaries and resources are accessible where needed.

This method allows NixOS to provide a declarative, reliable, and reproducible operating system where each component contributes predictably to the whole.

    