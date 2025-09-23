---
status: doing
tags:
  - 'guide'
  - 'sw/nix'
---
# Building Python Packages in Nix: Detailed Phases and Variables Explained

When building Python packages in Nix using `buildPythonPackage` or `buildPythonApplication`, the build process is divided into several **phases**. These phases are customized to accommodate Python's unique build and installation mechanisms. Understanding these phases, how they differ from standard Nix derivations, and the variables that affect them is crucial for effectively packaging Python software.

Below is a comprehensive guide to each phase, including the standard Nix derivation phases, how they differ in Python packages, the variables that affect them, and how different build systems (`setuptools`, `pyproject`, `wheel`) can influence these phases.

## 1. unpackPhase

**Purpose**: Extracts the source code from the provided source archives (e.g., `.tar.gz`, `.zip`).

**Behavior in Python Packages**:

- **Standard Behavior**: Similar to standard derivations; the source code specified in the `src` attribute is unpacked.
- **Special Cases**:
  - If the source is a wheel or egg, specific unpack hooks like `wheelUnpackHook` or `eggUnpackHook` might be used.

**Variables Affecting This Phase**:

- **`src` / `srcs`**: Source file(s) or directories to unpack.
- **`sourceRoot`**: Directory to change into after unpacking.
- **`setSourceRoot`**: Shell command to set `sourceRoot` dynamically.
- **`dontUnpack`**: Set to `true` to skip the unpack phase.
- **Hooks**:
  - **`preUnpack`**: Commands to run before unpacking.
  - **`postUnpack`**: Commands to run after unpacking.

**Differences Between Build Systems**:

- **All Build Systems**: Generally, all Python packages unpack their source code regardless of the build system used (`setuptools`, `pyproject`, etc.).

---

## 2. **patchPhase**

**Purpose**: Applies patches to the unpacked source code.

**Behavior in Python Packages**:

- **Standard Behavior**: Similar to standard derivations.
- **Common Uses**:
  - Applying patches to fix issues or adjust configurations.
  - Using `substituteInPlace` to modify files like `setup.py` or `pyproject.toml`.
  - Fixing shebangs, removing unsupported features, or adjusting dependencies.

**Variables Affecting This Phase**:

- **`patches`**: List of patch files to apply.
- **`patchFlags`**: Flags passed to the `patch` command (default is `-p1`).
- **`dontPatch`**: Set to `true` to skip this phase.
- **Hooks**:
  - **`prePatch`**: Commands to run before patching.
  - **`postPatch`**: Commands to run after patching.

**Differences Between Build Systems**:

- **All Build Systems**: Patching might be necessary to fix build issues specific to certain build systems or Python versions.

---

## 3. **configurePhase**

**Purpose**: Configures the build environment, often by running `./configure` scripts.

**Behavior in Python Packages**:

- **Usually Empty or Minimal**: Most Python packages do not have a `configure` script.
- **Default Behavior**: The default `configurePhase` does nothing unless overridden.

**Special Cases**:

- **Using CMake**:
  - If you add `cmake` to `nativeBuildInputs` (e.g., when packaging a `pybind11` project), the `cmake` command will automatically run during the `configurePhase`.
  - **Control**:
    - If you intend to run `cmake` later during the `buildPhase`, set `dontUseCmakeConfigure = true;` to prevent automatic execution during `configurePhase`.

**Variables Affecting This Phase**:

- **`dontConfigure`**: Set to `true` to skip the configure phase.
- **`configureScript`**: Path or command to run as the configure script.
- **`configureFlags`**: Additional flags for the configure script.

**Differences Between Build Systems**:

- **`setuptools` Packages**:
    - Typically do not require a configure phase.
- **`pyproject` Packages**:
    - May involve setting up the build environment according to `pyproject.toml`.

---

## 4. **buildPhase**

**Purpose**: Compiles the source code into binaries or libraries.

**Behavior in Python Packages**:

- **Varies Depending on Build System**:

### **Legacy Build System (`setup.py`):**

- **Command**: `python setup.py build`
- **Actions**:
  - Compiles any C extensions.
  - Prepares the package for installation.

### **PEP 517/518 Build System (`pyproject.toml`):**

- **Command**: `python -m build --wheel --no-isolation`
- **Actions**:
  - Builds the package into a wheel file.
  - The `--no-isolation` flag ensures that the build happens in the current environment.
- **Hooks**:
  - Uses `pypaBuildHook` to handle the build process.

**Variables Affecting This Phase**:

- **`pyproject`**: Set to `true` to use the `pyproject` build system.
- **`build-system`**: List of build-time Python dependencies (e.g., `setuptools`, `flit`).
- **`pypaBuildFlags`**: Flags passed to `python -m build`.
- **`buildInputs`**: Non-Python build-time dependencies (e.g., C libraries).
- **`buildFlags` / `buildFlagsArray`**: Flags specific to the build phase.

- **Hooks**:
    - **`preBuild`**: Commands to run before building.
    - **`postBuild`**: Commands to run after building.
    - **`setuptoolsBuildHook`**: Used when building with `setuptools`.
    - **`pypaBuildHook`**: Used when `pyproject = true`.

**Differences Between Build Systems**:

- **`setuptools` Packages**:
    - Use `setup.py` to build.
    - May require `setuptools` in `build-system`.
- **`pyproject` Packages**:
    - Use `python -m build --wheel`.
    - Build backend specified in `pyproject.toml` (e.g., `setuptools`, `flit`, `poetry-core`).
    - Must specify `build-system` dependencies.
- **Packages with C Extensions**:
    - May require additional `buildInputs` (e.g., `libffi`, `openssl`).

---

## 5. **checkPhase**

**Purpose**: Runs the package's test suite to verify the build.

**Behavior in Python Packages**:

- **Often Disabled by Default**:
  - `doCheck` is set to `false` by default because many Python packages require the package to be installed before testing.
- **Tests Usually Run in `installCheckPhase`**:
  - This allows tests to be run after the package is installed.

**Enabling Tests in `checkPhase`**:

- **Set `doCheck = true;`**: Enables the `checkPhase`.
- **Test Hooks**:
    - **`pytestCheckHook`**:
        - Simplifies running tests with `pytest`.
        - Automatically sets up the `checkPhase`.
    - **`unittestCheckHook`**:
        - Sets up `checkPhase` to run `python -m unittest discover`.

- **Variables Affecting This Phase**:
    - **`nativeCheckInputs`**: Dependencies needed during testing (e.g., `pytest`, `hypothesis`).
    - **`checkPhase`**: Can be customized to run specific test commands.
    - **`pytestFlagsArray`**: Flags for `pytest`.
    - **`disabledTests`**: List of test patterns to skip.
    - **`disabledTestPaths`**: Specific test files or directories to ignore.

- **Example**:

```nix
doCheck = true;
nativeCheckInputs = [ pytestCheckHook pytest ];
pytestFlagsArray = [ "--ignore=tests/integration" "-k" "not slow" ];
disabledTests = [ "test_network" ];
```

---

## 6. **installPhase**

**Purpose**: Installs the built package into the Nix store under `$out`.

**Behavior in Python Packages**:

- **Varies Depending on Build System**:

### **Legacy Build System (`setup.py`):**

- **Command**: `python setup.py install --prefix="$out" --root="$out"`
- **Actions**:
    - Installs the package files into the Nix store.
- **Hooks**:
    - Uses `setuptoolsInstallHook` to handle installation.

### **PEP 517/518 Build System (`pyproject.toml`):**

- **Command**: `python -m installer --destdir="$out" dist/*.whl`
- **Actions**:
    - Installs the wheel file into the Nix store using `installer`.
- **Hooks**:
    - Uses `pypaInstallHook` to handle installation.

**Variables Affecting This Phase**:

- **`dontInstall`**: Set to `true` to skip the install phase.
- **`installFlags` / `installFlagsArray`**: Flags specific to the install phase.
- **`makeWrapperArgs`**: Arguments passed to `makeWrapper` for wrapping binaries.
- **`dontWrapPythonPrograms`**: If `true`, skips wrapping Python scripts in `$out/bin`.
- **`removeBinByteCode`**: If `true`, removes bytecode from `/bin`.

**Differences Between Build Systems**:

- **`setuptools` Packages**:
    - May include additional flags to control installation paths.
    - Can set `setupPyInstallFlags` for extra control.
- **`pyproject` Packages**:
    - Use `pypaInstallHook` to install the wheel.
- **Packages with Binaries**:
    - Need to ensure that executables in `$out/bin` are correctly wrapped.

---

## 7. **fixupPhase**

**Purpose**: Performs post-installation fixes, such as wrapping binaries and adjusting file permissions.

**Behavior in Python Packages**:

- **Important for Wrapping Python Scripts and Setting Environment Variables**:
      - Ensures that scripts can find their dependencies.

**Actions**:

- **Wrapping Binaries**:
    - Uses `wrapPythonPrograms` function to wrap executables in `$out/bin`.
    - Sets environment variables like `PYTHONPATH`, `PATH`, and others.
- **Bytecode Compilation**:
    - Compiles `.py` files into `.pyc` bytecode.
    - May remove bytecode from `/bin` if `removeBinByteCode` is set.
- **Collision Handling**:
    - If `catchConflicts` is `true`, the `pythonCatchConflictsHook` may abort the build if there are conflicting files.

**Variables Affecting This Phase**:

- **`dontFixup`**: Set to `true` to skip this phase.
- **`dontWrapPythonPrograms`**: Prevents wrapping of scripts.
- **`wrapPythonPrograms`**: Function called during `postFixup` to wrap scripts.
- **`makeWrapperArgs`**: Additional arguments for `makeWrapper` when wrapping scripts.
- **`permitUserSite`**: If `true`, allows use of user site-packages (default is `false`).

**Hooks**:

- **`preFixup`**: Commands to run before fixup.
- **`postFixup`**: Commands to run after fixup (commonly where `wrapPythonPrograms` is called).

**Differences Between Build Systems**:

- **All Build Systems**: Need to ensure that scripts are correctly wrapped to find their dependencies.

---

## 8. **installCheckPhase**

**Purpose**: Performs tests on the installed package to ensure it works correctly.

**Behavior in Python Packages**:

- **Often Used for Running Tests That Require the Package to Be Installed**:
  - Allows testing of the installed package as it would be used by end-users.

**Actions**:

- **Running Tests**:
  - Executes tests using the installed package.
  - Commonly runs: `python -m pytest` or `python -m unittest`.
- **Import Checks**:
  - Uses `pythonImportsCheck` to verify that modules can be imported.
  - Simple way to ensure the package is correctly installed.

**Variables Affecting This Phase**:

- **`doInstallCheck`**: Set to `true` (default in `buildPythonPackage`) to enable this phase.
- **`installCheckPhase`**: Can be customized to define specific test commands.
- **`installCheckInputs`**: Dependencies needed during install checks.
- **`installCheckFlags` / `installCheckFlagsArray`**: Flags specific to this phase.

**Example**:

```nix
doInstallCheck = true;
installCheckPhase = ''
  python -m pytest tests/
'';
```

---

## Additional Notes on Python Package Derivations

### **Hooks Specific to Python Packages**

- **`setuptoolsBuildHook`**:
  - Used when building packages with `setuptools` and `setup.py`.
  - Overrides `buildPhase` and `installPhase` to use `setup.py`.

- **`pypaBuildHook` and `pypaInstallHook`**:
  - Used when building packages that comply with PEP 517/518.
  - Handles building wheels and installing them.

- **`pytestCheckHook`**:
  - Sets up the `checkPhase` or `installCheckPhase` to run tests using `pytest`.
  - Simplifies running tests and handling test dependencies.

- **`unittestCheckHook`**:
  - Sets up `checkPhase` to run `python -m unittest discover`.

- **`wrapPythonPrograms`**:
  - Wraps Python scripts to ensure the correct environment variables are set.
  - Ensures that `PYTHONPATH` includes the necessary site-packages directories.

### **Variables Affecting Multiple Phases**

- **`buildPythonPackage` Parameters**:
    - **`namePrefix`**: Prefixes the package name (e.g., `python3.11-`).
    - **`disabled`**: If `true`, the package is not built.
    - **`dependencies`**: Runtime Python dependencies.
    - **`build-system`**: Build-time Python dependencies.
    - **`nativeBuildInputs`**: Build-time tools (e.g., `pkg-config`, `cython`).
    - **`buildInputs`**: Build and/or runtime dependencies (e.g., C libraries).
    - **`propagatedBuildInputs`**: Dependencies that should be available to packages depending on this one.
    - **`pythonPath`**: Additional paths to include in `PYTHONPATH`.
    - **`pythonImportsCheck`**: Modules to import as a basic test.
    - **`doCheck`**: Controls whether the `checkPhase` is executed.
    - **`doInstallCheck`**: Controls whether the `installCheckPhase` is executed.

### **Environment Variables**

- **`PYTHONPATH`**:
    - Set to include the package's `site-packages` directory and dependencies.
    - Ensures that Python can find the installed modules.

- **`PYTHONNOUSERSITE`**:
    - Often set to prevent Python from using user-specific site-packages.
    - Ensures a clean and isolated environment.

## Conclusion

When packaging Python packages in Nix, the standard derivation phases are often customized or adjusted to fit Python's packaging and installation mechanisms. Key differences occur in the `buildPhase`, `installPhase`, and testing phases (`checkPhase` and `installCheckPhase`). Understanding these differences, along with the variables and hooks that affect each phase, helps in writing and debugging Python package derivations in Nix.

By carefully setting the appropriate variables and using the provided setup hooks, you can ensure that each phase executes correctly, resulting in a functional and reliable Python package in the Nix ecosystem. Whether you're working with `setuptools`, `pyproject`, or pre-built wheels, being aware of how each phase operates allows for effective customization and problem-solving during the packaging process.

---

**Note**: Always refer to the latest Nixpkgs documentation and best practices when packaging Python software, as tools and conventions may evolve over time.