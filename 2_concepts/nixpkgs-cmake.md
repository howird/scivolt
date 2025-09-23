---
tags:
  - note
  - sw/nix
status: review
---
# Nix CMake Environment Variables

- When using Nix derivations to build packages with CMake, Nix sets several environment variables that can affect the CMake build process
- Nix aims to create reproducible builds by providing a controlled environment, and part of this involves setting environment variables that guide tools like CMake to find dependencies and use the correct compilers and flags

Here are some key environment variables that Nix sets during CMake builds:

1. **CMAKE\_PREFIX\_PATH**: This variable is set to include the prefixes of dependencies specified in the Nix derivation. It helps CMake locate installed libraries and headers in non-standard locations within the Nix store.

2. **CMAKE\_LIBRARY\_PATH** and **CMAKE\_INCLUDE\_PATH**: These variables point to the directories where libraries and headers are located, assisting CMake in finding the necessary files during the build process.

3. **CC** and **CXX**: Nix sets these variables to specify the C and C++ compilers to be used, ensuring that the build process uses the compilers provided by Nix rather than the system defaults.

4. **CFLAGS**, **CXXFLAGS**, **LDFLAGS**, and **CPPFLAGS**: These compiler and linker flags are set to include the necessary paths and options required for building the package correctly within the Nix environment.

5. **NIX\_CFLAGS\_COMPILE** and **NIX\_LDFLAGS**: These are additional flags that Nix injects to ensure that all compiled code references dependencies within the Nix store, promoting build purity and reproducibility.

6. **PKG\_CONFIG\_PATH**: This variable is set to help `pkg-config` find `.pc` files in the Nix store, which CMake might use to locate dependencies.

7. **SSL\_CERT\_FILE** and **SSL\_CERT\_DIR**: If the package requires SSL certificates, Nix sets these variables to point to the certificates within the Nix store.

Additionally, Nix may provide CMake with extra arguments through the `configureFlags` variable in the derivation, which can include options like `-DCMAKE_INSTALL_PREFIX` to specify the installation directory within the Nix store.

By setting these environment variables, Nix ensures that:

- **Isolation**: The build process does not inadvertently use system-wide libraries or tools, which enhances the reproducibility and reliability of the build.
- **Dependency Resolution**: All dependencies are correctly located within the Nix store, and the build process uses the exact versions specified in the derivation.
- **Compiler Consistency**: The same compiler and flags are used across different builds, preventing discrepancies due to differing compiler behaviors or defaults.

**Example**:

Here's a simplified example of how a Nix derivation for a CMake-based project might look:

```nix
{ stdenv, cmake, makeWrapper, pkgconfig, someDependency }:

stdenv.mkDerivation {
  name = "my-cmake-project-1.0";
  src = ./src;

  buildInputs = [ cmake pkgconfig someDependency ];

  preConfigure = ''
    export CXXFLAGS="$CXXFLAGS -std=c++17"
  '';

  cmakeFlags = [
    "-DCMAKE_BUILD_TYPE=Release"
    "-DSOME_OPTION=ON"
  ];
}
```

In this derivation:

- `buildInputs` ensures that `cmake`, `pkgconfig`, and `someDependency` are available in the environment.
- Nix will automatically set environment variables like `CMAKE_PREFIX_PATH` to include the paths to `someDependency` and other inputs.
- The `preConfigure` script allows you to modify environment variables before the configure phase, affecting how CMake runs.

**Conclusion**:

By controlling these environment variables, Nix provides a consistent and reproducible environment for building CMake projects. This approach minimizes external influences and ensures that builds are deterministic, which is a core principle of Nix package management.

## CMAKE_INSTALL_PREFIX

- Nix derivations for CMake-based projects typically set `CMAKE_INSTALL_PREFIX` variable to ensure that the software installs into the correct location within the Nix store
- However, instead of setting it as an environment variable like `cmake_install_prefix`, Nix specifies `CMAKE_INSTALL_PREFIX` directly through the **`cmakeFlags`** (or sometimes `configureFlags`) in the derivation

Here’s how it works:

1. **Setting `CMAKE_INSTALL_PREFIX` via `cmakeFlags`**:

   In a Nix derivation, you often see `cmakeFlags` used to pass additional arguments to CMake. Nix uses this to set `CMAKE_INSTALL_PREFIX` to the output path (`$out`) in the Nix store.

   **Example**:

   ```nix
   stdenv.mkDerivation {
     name = "my-cmake-project-1.0";
     src = ./src;

     buildInputs = [ cmake pkgconfig someDependency ];

     cmakeFlags = [
       "-DCMAKE_BUILD_TYPE=Release"
       "-DCMAKE_INSTALL_PREFIX=$out"
     ];
   }
   ```

   In this example, `-DCMAKE_INSTALL_PREFIX=$out` tells CMake to install the built files into the Nix store output path specified by `$out`. This ensures that when `make install` is run, the files go to the correct location managed by Nix.

2. **Why Not an Environment Variable?**

   CMake primarily uses command-line flags or variables set in `CMakeLists.txt` for configuration. While environment variables can influence CMake, setting `CMAKE_INSTALL_PREFIX` via an environment variable is not a standard practice and may not have the desired effect. CMake expects `CMAKE_INSTALL_PREFIX` to be defined as a cache variable, which is typically set using `-D` flags.

3. **Nix's Approach to Installation Paths**:

   - **Isolation and Reproducibility**: By explicitly setting `CMAKE_INSTALL_PREFIX` to `$out`, Nix ensures that the build is reproducible and that the installed files do not interfere with the rest of the system.
   - **Avoiding Environment Side Effects**: Relying on environment variables can introduce unintended side effects, especially in complex build environments. Nix prefers explicit configuration over implicit environment settings to maintain purity.

4. **Customizing `CMAKE_INSTALL_PREFIX` in Nix**:

   If you need to customize the installation prefix for some reason, you can modify the `cmakeFlags` in your derivation accordingly. However, it's important to ensure that the installation path remains within the Nix store to maintain the benefits of Nix's package management.

**Conclusion**:

- Nix derivations with CMake do not set an environment variable named `cmake_install_prefix`
- Instead, they set `CMAKE_INSTALL_PREFIX` directly via configuration flags (`cmakeFlags` or `configureFlags`), usually to `$out`, which is the designated output path in the Nix store
- This approach aligns with Nix's goals of build purity, reproducibility, and isolation from the system environment

**Additional Information**:

If you want to inspect the actual build process or see how variables are being set, you can:

- **Use Verbose Mode**: Add `-DCMAKE_VERBOSE_MAKEFILE=ON` to `cmakeFlags` to see detailed build commands.
- **Inspect Build Logs**: After running the build, check the logs in the Nix store for any messages from CMake about variable settings.
