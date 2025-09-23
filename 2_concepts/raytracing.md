# Raytracing

## Algorithm

- `Scene::Raytrace`
    - for pixel in image:
        - create ray from eye to pixel `Scene::eyeRay`
        - `hitinfo`
        - if `Scene::intersect`

- `Scene::intersect`
    - for 


- **Specification:** This part is not a restatement of the assignment specification. It should include any details or assumptions you made that were not included in the assignment. Tell us about any extra commands, options or features you added or any additional files you may have generated. If you have made any assumptions about the assignment specification or the objectives, state and justify them here.

## Compilation

- the program was compiled as such starting from the root directory:
```bash
# starting from repo root directory:
mkdir -p build # make build/ directory
cd build # go to build/ directory
cmake .. -DCMAKE_BUILD_TYPE=Debug # setup build
make # compile
cd .. # go back to repo root
./build/CS488 media/cornellbox.obj # run a command
```

- NOTE: I use `#define` macros to enable/disable shadows, lighting, and the environment mapping, so you will have to repeat the build steps above to modify them
    - they can be found in `consts.h` 
    - in order to reproduce my results you will have to recompile after __commenting/uncommenting__ the `#define`s for `ENVMAP`, `SHADOW`, and `LIGHTING`
    - the specific `#defines` for reproducing each result is specified below

## Specification

- Major refactoring was done to the `cs488.h` file:
    - I did my best to separate classes into their own headers, and made some attempts to split things up into header/source files
    - This was done mainly for my own understanding of the code and my programming style
    - There were some decisions made 


## Tasks


### Task 1: Triangle Intersection

- this can be reproduced by going to `consts.h` and __commenting out__ `#define`s for `ENVMAP`, `SHADOW`, and `LIGHTING`, recompiling and running: `./build/CS488 media/cornellbox.obj`
- this fulfills objectives:
    - 1. Ray-triangle intersection is returning correct hit/miss.

![](2_concepts/media/Pasted%20image%2020250606192934.png)

### Task 2: Shadow Tracing

- this can be reproduced by going to `consts.h` and __commenting out__ `#define ENVMAP`, making sure `#define`s for `SHADOW` and `LIGHTING` are __not commented__ out, recompiling and running: `./build/CS488 media/cornellbox.obj`
- this fulfills objectives:
    - 2. HitInfo is filled in properly.
    - 3. Shadow is properly rendered by shadow ray tracing.
    - 4. Specular reflection is working correctly.
    - 5. Specular refraction is working correctly.
    - 6. Environment map is loaded and used properly.

![](2_concepts/media/Pasted%20image%2020250606193320.png)

### Task 3: Specular reflection

- this can be reproduced by going to `consts.h` and __commenting out__ `#define`s for `ENVMAP`, `SHADOW`, and `LIGHTING`, recompiling and running: `./build/CS488 media/cornellbox-metal.obj`
- this fulfills objectives:
    - 4. Specular reflection is working correctly.

![](2_concepts/media/Pasted%20image%2020250606193530.png)

### Task 4: Specular Refraction

- this can be reproduced by going to `consts.h` and __commenting out__ `#define ENVMAP`, making sure `#define`s for `SHADOW` and `LIGHTING` are __not commented__ out, recompiling and running: `./build/CS488 media/testObj-glass.obj`
- this fulfills objectives:
    - 5. Specular refraction is working correctly.

![](2_concepts/media/Pasted%20image%2020250606193659.png)


### Task 5: Environment Mapping

- this can be reproduced by going to `consts.h`, making sure that `#define`s for `ENVMAP`, `SHADOW`, and `LIGHTING` are __not commented__ out, recompiling and running: `./build/CS488 media/cornellbox.obj`
- this fulfills objectives:
   - 6. Environment map is loaded and used properly.

![](2_concepts/media/Pasted%20image%2020250606203954.png)