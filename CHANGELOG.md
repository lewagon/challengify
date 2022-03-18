
# 0.3.2 (TBD)

### Added

#### Challengify iterate

- Replaces numeric versions with ordered text versions in `.challengify_iterate.yml`
- Allows the use of prefixes for the `iterate` command through wagon_common AliasedGroup (i.e. `challengify ite` instead of `challengify iterate`)
- Allows to generate a specific or a range of challenge versions through the `-c` option (i.e. `-c api`, `-c api..api_advanced`, `-c api..`, `-c ..api`, `-c 3`, -c 3..4`, `-c 3..`, `-c ..3`, `-c 0..api`)
- Adds a `target` directory in the conf file for the root of the generated challenge versions
- Adds the `iterate` command conf file param `only.for`
- Adds `# $ONLY_xxx_version_BEGIN` and `# $ONLY_xxx_version_END` code delimiters for `challengify iterate`
- Generates a per challenge version `.lewagon/.challengify_generated.txt` containing the list of generated files
- Adds `--ignore-metadata` option to ignore metadata file generation

#### Challengify run

- Adds `# $CHA_BEGIN` / `# $CHA_END` delimiter aliases
- Adds `# $DEL_BEGIN` / `# $DEL_END` delimiters aliases
- Adds `# $ERASE_BEGIN` / `# $ERASE_END` delimiters consuming block newline
- Adds `# $WIPE_BEGIN` / `# $WIPE_END` delimiters consuming block newline + following newline
- Adds `# $IMPLODE_BEGIN` / `# $IMPLODE_END` delimiters consuming block newline + surrounding newlines
- `--dry-run` now lists the destination path of the files that would be generated
- Adds tests for code transformations

### Fixed

#### Challengify iterate

- Does not consume anymore the delimiters of the `run` command
- Corrects the path of the generated challenge files

### Changed

#### Challengify iterate

- Refactor the code handling version generation
- Renames the `iterate` command conf file params `ignore.before` and `ignore.after` into `only.from` and `only.to`
- Renames the conf file for the `iterate` command from `.challengify_iterate.yaml` to `.challengify_iterate.yml`
- Refactores the code in order to use a version iterator
- Removes unnecessary `project_name` param in conf file
