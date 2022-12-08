# BazelSeleniumSample

template for bazel+python+selenium+gazelle.
Tested on M1Pro macbook.

# Run test

`bazel run //:browser_test_chromium-local`

# Browsers

- `//browsers:chromium-local-no-headless`: chromium for debug
- ` @io_bazel_rules_webtesting//browsers:chromium-local`: headless chromium

# Useful commands

- `bazel run //:gazelle`: generate `BUILD.bazel` from python source codes.
- `bazel run //:gazelle_python_manifest.update`: Should be run after [requirements_lock.txt](requirements_lock.txt)
  updated.
