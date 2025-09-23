---
tags:
  - note
  - sw/nix
status: done
---
# Understanding Dependency Variables in Nix Derivations

In Nix, specifying dependencies correctly ensures that packages are built and run in the intended environments. Here's a concise guide to the key dependency variables, their aliases, when to use them, the build phases they affect, and insights on propagation.

## Key Dependency Variables

### `depsBuildBuild`

**Aliases:** None

**Description:** Dependencies needed **at build time** that run on the **build platform** and produce tools for the **build platform**.

**When to Use:** Include packages here if they are tools or libraries used during the build process to produce other build-time tools. For example, when building a compiler that compiles other compilers.

**Build Phases Affected:** Early build phases where build-time tools are generated.

---

### `nativeBuildInputs`

**Aliases:** Historically known as `depsBuildHost`

**Description:** Dependencies needed **at build time** that run on the **build platform** but produce artifacts for the **host platform**.

**When to Use:** Use this for build-time tools like `pkg-config`, `autoconf`, or `cmake` that assist in building your package but are not sensitive to the target platform.

**Build Phases Affected:** `configurePhase`, `buildPhase`, and any phase requiring build-time utilities.

---

### `depsBuildTarget`

**Aliases:** None

**Description:** Dependencies needed **at build time** that run on the **build platform** and produce code for the **target platform**.

**When to Use:** Rarely. Applicable when building cross-compilers or tools that generate code for a different platform than the one you're building on.

**Build Phases Affected:** Specialized phases in cross-compilation scenarios.

**Note:** Avoid using unless you're certain it's necessary, such as when packaging compilers for cross-compilation.

---

### `depsHostHost`

**Aliases:** None

**Description:** Dependencies needed **at build time** and **run time** that run on the **host platform**.

**When to Use:** For tools or libraries used during the build that must match the host environment, like macro processors or code generators that execute during the build.

**Build Phases Affected:** `buildPhase`, possibly `installPhase`, and runtime if included in the final package.

---

### `buildInputs`

**Aliases:** Historically known as `depsHostTarget`

**Description:** Dependencies needed **at run time** that run on the **host platform** and are intended for the **target platform**.

**When to Use:** Include libraries and programs your package needs to function after installation, such as shared libraries it links against.

**Build Phases Affected:** `buildPhase` (for linking) and runtime execution.

---

## Propagated Dependencies

Propagation ensures that certain dependencies are automatically included in packages that depend on yours.

### `propagatedNativeBuildInputs`

**Aliases:** Historically known as `depsBuildHostPropagated`

**Description:** Build-time dependencies on the **host platform** that are propagated to dependent packages.

**When to Use:** When your package provides tools necessary for the build process of dependent packages, and you want those tools to be included automatically.

**Build Phases Affected:** Build phases of packages that depend on yours.

**Caution:** Overuse can lead to bloated build environments. Propagate only when essential.

---

### `propagatedBuildInputs`

**Aliases:** Historically known as `depsHostTargetPropagated`

**Description:** Run-time dependencies on the **target platform** that are propagated to dependent packages.

**When to Use:** When your package's functionality relies on certain libraries or programs that must also be present in any package that depends on yours.

**Build Phases Affected:** Build and runtime phases of dependent packages.

**Caution:** Excessive propagation can increase closure sizes and obscure dependency chains. Use judiciously.

---

## Understanding Propagation

**Propagation** means that when another package depends on your package, it automatically includes the propagated dependencies without needing to declare them explicitly.

### What to Be Wary Of:

- **Dependency Bloat:** Propagated dependencies can unintentionally enlarge the dependency graph, leading to longer build times and larger outputs.
- **Hidden Dependencies:** It can make it harder to trace where certain dependencies are coming from, complicating maintenance and debugging.
- **Best Practices:** Only propagate dependencies that are strictly necessary for the dependent package to build or run correctly.

---

By carefully choosing the appropriate dependency variables and understanding their impact on the build process, you can create efficient and maintainable Nix packages.