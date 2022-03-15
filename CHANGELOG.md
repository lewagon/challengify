
# 0.3.2 (TBD)

### Added

- Replaces numeric versions with ordered text versions in `.challengify_iterate.yml`
- Allows the use of prefixes for the `iterate` command through wagon_common AliasedGroup (i.e. `challengify ite` instead of `challengify iterate`)
- Allows to generate a specific or a range of challenge versions through the `-c` option (i.e. `-c api`, `-c api..api_advanced`, `-c api..`, `-c ..api`, `-c 3`, -c 3..4`, `-c 3..`, `-c ..3`, `-c 0..api`)
- Adds the `iterate` command conf file param `only.for`
- Adds `# $ONLY_number_BEGIN` and `# $ONLY_number_END` code delimiters for `challengify iterate`
- Add tests for code transformations
- `--dry-run` now lists the destination path of the files that would be generated

### Fixed

- Does not consume anymore the delimiters of the `run` command
- Corrects the path of the generated challenge files

### Changed

- Renames the `iterate` command conf file params `ignore.before` and `ignore.after` into `only.from` and `only.to`
- Renames the conf file for the `iterate` command from `.challengify_iterate.yaml` to `.challengify_iterate.yml`
- Refactores the code in order to use a version iterator
