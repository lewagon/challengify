
# 0.3.10 2023-01-19

### Added

- Adds support for `.xml` file type

# 0.3.9 2022-11-25

### Added

- Adds support for file deletion: remove from the destination the input sources that shoud not exist
- Adds repository related default destination parameter: a `*-solutions` respository will have a `*-challenges` default destination parameter

# 0.3.8 2022-07-01

### Added

- Adds support for `.proto` file type

# 0.3.7 2022-06-20

### Added

- Adds support for `.conf` file type

# 0.3.6 2022-06-14

### Added

- Adds support for `.dbml` file type

# 0.3.5 2022-06-14

### Fixed

- Corrects use for `.sql` file type

# 0.3.4 2022-05-30

### Added

- Adds support for `.yml`, `.yaml`, `.toml` and extensionless file types
- Adds support for `IMPORT` verb

# 0.3.3 2022-05-17

### Added

#### Challengify iterate

- Adds support for version and position macros
- Adds support for globbing patterns in iterate only for/from/to rules
- Adds support for several sources in conf file
- Adds support for versioned files conf in `.challengify_iterate.yml`
- Adds version only delimiter generators `# $verb_ONLY_FOR_version_BEGIN` and `# $verb_ONLY_FOR_version_END` for verbs `CHALLENGIFY`, `CHA`, `DELETE`, `DEL`, `ERASE`, `WIPE`, `IMPLODE`
- Adds support for `CODE` verb
- Replaces numeric versions with ordered text versions in `.challengify_iterate.yml`
- Allows the use of prefixes for the `iterate` command through wagon_common AliasedGroup (i.e. `challengify ite` instead of `challengify iterate`)
- Allows to generate a specific or a range of challenge versions through the `-c` option (i.e. `-c api`, `-c api..api_advanced`, `-c api..`, `-c ..api`, `-c 3`, -c `3..4`, `-c 3..`, `-c ..3`, `-c 0..api`)
- Adds a `destination` directory in the conf file for the root of the generated challenge versions
- Adds the `iterate` command conf file param `only.for`
- Adds `# $ONLY_xxx_version_BEGIN` and `# $ONLY_xxx_version_END` code delimiters for `challengify iterate` with option to `ERASE`, `WIPE` (default) or `IMPLODE`
- Generates a per challenge version `.lewagon/.challengify_generated.txt` containing the list of generated files
- Adds `--ignore-metadata` option to ignore metadata file generation
- Adds functional test

#### Challengify run

- Adds support for `.html`, `.css`, `.js`, `.html.erb` and `.js.erb` file types
- Adds `# $CHA_BEGIN` / `# $CHA_END` delimiter aliases
- Adds `# $DEL_BEGIN` / `# $DEL_END` delimiters aliases
- Adds `# $ERASE_BEGIN` / `# $ERASE_END` delimiters consuming block newline
- Adds `# $WIPE_BEGIN` / `# $WIPE_END` delimiters consuming block newline + following newline
- Adds `# $IMPLODE_BEGIN` / `# $IMPLODE_END` delimiters consuming block newline + surrounding newlines
- Adds support for indented delimiters (consumes leading whitespaces for `ERASE`, `WIPE` and `IMPLODE`)
- `--dry-run` now lists the destination path of the files that would be generated
- Adds tests for code transformations

### Fixed

#### Challengify iterate

- Does not consume anymore the delimiters of the `run` command
- Corrects the path of the generated challenge files

### Changed

#### Challengify iterate

- Add a `--format` option to use an autoformatter (default False), previously the autoformatter always ran
- Refactor the code handling version generation
- Renames the `iterate` command conf file params `ignore.before` and `ignore.after` into `only.from` and `only.to`
- Renames the conf file for the `iterate` command from `.challengify_iterate.yaml` to `.challengify_iterate.yml`
- Renames the conf file `destinations` param to `versions`
- Refactores the code in order to use a version iterator
- Removes unnecessary `project_name` param in conf file
