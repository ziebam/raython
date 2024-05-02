# raython

simple experiment to learn about Python and C interoperability. the bindings are in `raylib.py`, the code that calls the bindings is in `raython.py`.

# usage

1. clone [raylib](https://github.com/raysan5/raylib) and build it as a shared library (steps differ depending on the OS), e.g.

```
git clone https://github.com/raysan5/raylib.git raylib
cd raylib/src/
make PLATFORM=PLATFORM_DESKTOP RAYLIB_LIBTYPE=SHARED
```

2. move the `.dll` (Windows) or `.so` (Unix/Darwin) file to the raython root directory.
3. run with `python raython.py`.
