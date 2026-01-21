# Changelog

## [2.0.0] - 2026-01-21

### Changed
- **BREAKING**: Updated to Node.js 16+ compatibility
- Upgraded C++ standard from C++11 to C++17 (required for Node.js 20+)
- Updated macOS deployment target from 10.8 to 10.14
- Upgraded dependencies:
  - `uuid`: ^3.3.2 → ^10.0.0 (fixes deprecation warnings)
  - `nan`: ^2.13.2 → ^2.20.0
  - `node-gyp`: ^4.0.0 → ^10.0.0
  - `bindings`: ^1.2.1 → ^1.5.0
  - `event-target-shim`: ^1.1.1 → ^6.0.2

### Fixed
- Fixed compilation errors with Node.js 20+ (std::optional compatibility)
- Fixed uuid import for v10 (now uses destructured import)
- Fixed EventTarget import for event-target-shim v6
- Added C++17 compilation flags to binding.gyp

### Added
- Node.js engine requirement (>=16.0.0)
- MIT license field in package.json
- Contributor information

## [1.2.0] - Previous

Original version by Charlie Hess
