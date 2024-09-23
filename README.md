# NeoBuilder

Builds Neobuf Packages from Protobuf files using Protoplasm! :D

## Super Important Info

Neobuilder releases are NOT guaranteed to be backwards compatible with older 
versions of Protoplasm and trying to run Neobuilder built code in a Protoplasm 
release who's major and/or minor versions lag behind will more often than not 
just break.

A difference in the patch version should most often be fine, as should using a 
Protoplasm release that's one or more minor versions ahead of the Neobuilder 
used to build code. 

## Versioning

The versioning of Neobuilder and Protoplasm (major and minor versions) go hand 
in hand; i.e. when Protoplasm's major of minor versions bump, a new NeoBuilder 
should also be released with the same major and minor version, even if there's 
no actual code change needed in NeoBuilder to support whatever changed in 
Protoplasm.

Note that in order to simplify and ease this synchronous development, release 
and versioning, the NeoBuilder package for the latest Protoplasm should 
generally NOT be dependent on any new features added to that package, so that 
the NeoBuilder package can be built and released FIRST and it can build code for
its corresponding Protoplasm version, withing having that latest version 
actually installed.

This is done in order to not create a circular dependency on features between 
the two but instead have NeoBuilder only depend on the previous version of 
Protoplasm, especially for its pre-release unit-tests, and instead allow 
Protoplasm to fully depend on the latest NeoBuilder for its unit-tests.

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