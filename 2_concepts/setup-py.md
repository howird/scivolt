---
tags:
  - note
  - sw/python
status: done
---
# setup.py

When you use `setup.py` to install a Python package, it typically installs to one of a few standard locations depending on your environment and the type of installation specified. Here’s a breakdown:

### 1. **Global Installation**
   - If you run `python setup.py install` (without any virtual environment activated), the package installs globally.
   - For Unix-like systems (Linux, macOS), this often means the package is installed to a directory like `/usr/local/lib/pythonX.Y/site-packages/`, where `X.Y` is your Python version (e.g., `3.9`).
   - For Windows, it might go to something like `C:\PythonXY\Lib\site-packages\`, depending on where Python is installed.
   - You may need `sudo` privileges to install globally on Unix-like systems.

### 2. **User Installation**
   - Running `python setup.py install --user` installs the package to the user’s site-packages directory rather than system-wide. This is typically located at:
     - `~/.local/lib/pythonX.Y/site-packages/` on Unix-like systems.
     - `%APPDATA%\Python\PythonXY\site-packages` on Windows.

### 3. **Virtual Environment Installation**
   - If you activate a virtual environment before running `python setup.py install`, the package installs directly into the virtual environment’s `site-packages` directory.
   - This directory is isolated from the global Python installation, often at `env_name/lib/pythonX.Y/site-packages/` within the virtual environment folder.

### 4. **Editable Installations**
   - If you run `python setup.py develop` or `pip install -e .`, the package installs in *editable mode*. This means it links to the source directory, allowing you to modify the source code and have the changes reflected without reinstallation.
   - This approach typically still targets the `site-packages` directory of the active Python environment but keeps references to your source files instead of copying them fully.

For typical development, using a virtual environment is recommended since it keeps dependencies isolated and prevents conflicts with global packages.