---
tags:
  - note
  - sw/linux
status: done
aliases:
  - RPATH
---
# Shared Libraries in Linux

In Linux, `RPATH` is a mechanism used to specify a runtime search path for shared libraries that are needed by an executable. When an executable is compiled and linked, `RPATH` can be embedded within it to tell the runtime linker where to look for shared libraries at runtime. This can be particularly useful when libraries are not in standard locations like `/lib` or `/usr/lib`.

Here's a breakdown of key points about `RPATH`:

1. **Usage**: `RPATH` is a directory path embedded in the executable file itself. When the executable is run, the linker (`ld.so`) uses `RPATH` to find libraries needed by that executable.

2. **Setting RPATH**: When linking an executable, you can set the `RPATH` with the linker flag:
```bash
gcc -o myprogram myprogram.o -Wl,-rpath,/path/to/lib
```

   Here, `-Wl,-rpath,/path/to/lib` tells the linker to embed `/path/to/lib` as an `RPATH` in `myprogram`.

3. **Precedence and Security**:
   - `RPATH` is looked at before the default library paths, making it useful for finding libraries that might be located in custom directories.
   - However, `RPATH` has been generally replaced by `RUNPATH` in modern systems because of its security and flexibility advantages.
   - `RPATH` is considered to be more “hardcoded,” as it cannot be overridden by environment variables like `LD_LIBRARY_PATH`.

4. **RUNPATH**: `RUNPATH` is similar to `RPATH`, but it allows paths to be overridden by `LD_LIBRARY_PATH`. This is more flexible and is generally preferred.

5. **Checking for RPATH**:
   - You can check if an executable has an `RPATH` set by using the `readelf` command:
```bash
readelf -d myprogram | grep RPATH
```

6. **Deprecation**: Since `RUNPATH` offers more flexibility, many systems and applications are moving away from using `RPATH` in favor of `RUNPATH`.