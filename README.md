# NeoBuilder

Builds Neobuf Packages from Protobuf files using Protoplasm! :D

## Useful info

Installing this package creates a command line executable called `neobuild` (or 
`neobuild.exe` in Windows) in Python's `Scripts` folder so you just run the 
`neobuild` command from a console.

## Usage

Assuming you've got a package called `sandbox` and you're storing your protobuf 
files in a directory called `proto` and you want to spit out the build into the 
directory `build` just go:

```
neobuild sandbox 
```

## Versioning Your Package

If you place a plain text file called `VERSION` in the root of your proto 
package (e.g. `/proto/sandbox/VERSION` from the example above) and skip any 
versioning parameters (the `--major`, `-m`, `--patch` and `-p` guys) Neobuilder
will use that file for versioning.

The first line in the file should be the semantic version number `x.y.z.a`

## More stuff

```
usage: neobuild [-h] [-m | -p] [-b [BUILDROOT]] [-v] package [protopath]

Builds neobuf packages with protoplasm.

positional arguments:
  package               Package name
  protopath             Path to the root of the protobuf files (default="./proto")

options:
  -h, --help            show this help message and exit
  -m, --major           Bump the major version number instead of the minor
  -p, --patch           Bump the patch version number instead of the minor
  -b [BUILDROOT], --buildroot [BUILDROOT]
                        Path to the root of the output build files (default="./build")
  -v, --verbose         Spits out DEBUG level logs
```