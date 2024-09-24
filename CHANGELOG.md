# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [5.3.0] - 2024-09-24

### Added

- Support for the `google.protobuf.Value` message


## [5.2.1] - 2024-09-24

### Changed

- The line `from typing import *` in most templates to `import typing` and now 
  references to classes an such from `typing` are explicit (i.e. `List` -> 
  `typing.List`) 

### Fixed

- Side-effects caused by `from typing import *` when messages/classes share a 
  name of classes in the `typing` package
- Bug where `datetime` was missing from imports in gRPC senders and receivers


## [5.2.0] - 2024-09-23

### Added

- Support for the `google.protobuf.Struct` message


## [5.1.2] - 2024-07-02

### Fixed

- An issue with the last fix where, if the build root is a relative path, we'll 
  end up getting an exception because we can't find how one path is relative to 7
  another if one of them is absolute and the other is relative.


## [5.1.1] - 2024-06-28

### Fixed

- An issue where the `__everything__.py` file was missing the first character of
  the package name if the build root ended with a slash (or backslash)


## [5.1.0] - 2024-04-30

### Added

- A class attribute called `__servicer_cls__` to any service interfaces (for 
  a gRPC build) with reference to that services `GrpcServicer` class
- Added a bunch of useful sub-tests to unittests

### Fixed

- A bunch of unittesting issues

## [5.0.0] - 2024-04-15

### Changed

- Moved this entire project over to Github 
- Bumped the version in order to not confuse older stuff that doesn't expect 
  protoplasm to exist in Pypi.org (if we end up migrating this there and 
  just open-sourcing the whole thing)
  - Also in case something changes in the API while migrating, cause I tend 
    to fiddle with the code and tidy up and refactor when moving stuff
