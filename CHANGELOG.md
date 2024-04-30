# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


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
