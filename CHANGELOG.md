
# 0.3.2 (2022-01-19)

* Added
- Allows the use of prefixes for the `iterate` command through wagon_common AliasedGroup (i.e. `challengify ite` instead of `challengify iterate`)
- Allows to generate a specific or a range of challenge versions through the `-c` option
- Adds the `iterate` command conf file param `only.for`
* Fixed
- Does not consume anymore the delimiters of the `run` command
- Corrects the path of the generated challenge files
* Changed
- Renames the `iterate` command conf file params `ignore.before` and `ignore.after` into `only.from` and `only.to`
- Renames the conf file for the `iterate` command from `.challengify_iterate.yaml` to `.challengify_iterate.yml`
