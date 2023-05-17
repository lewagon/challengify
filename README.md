
generate challenges from solutions using code block delimiters

## install

``` bash
pip install challengify                 # from gemfury using `~/.pip/pip.conf`
pip uninstall -y challengify            # uninstall
alias cha="challengify $@"              # alias
```

## sub commands

| command | usage |
| --- | --- |
| [iterate](doc/README_iterate.md) | generate several challenge versions from a single codebase |
| [test](doc/README_test.md) | generate temporary challengified files |
| [generate](doc/README_generate.md) | create `~/.challengify.yaml` conf file |
| [inject](doc/README_inject.md) | deprecated |

## commands

generate challenges in destination directory from solutions files and directory trees within the provided scope

``` bash
challengify run --help                  # list options

challengify run sources                 # generate challenges from individual files and directory trees
challengify run --all                   # generate challenges from the current directory tree

challengify run --all --force           # force sync even if destination does not have a clean git status
challengify run -af

challengify run -d ../data-cha          # set path to the destination directory (from the root of the project)

challengify run -id test *              # generate challenges from the current directory tree in the test directory

challengify run --dry-run               # do not generate challenges
challengify run --verbose               # list file selection process (scope / expanded scope / git controlled / sync ignored)

challengify run --test                  # generate *test challengification* files for the scope (see the challengify test command)
```

behavior:
- the command can be run anywhere in the solutions directory tree
- the challenges are generated at the corresponding location in the destination directory (source and destination have identical structures)
- the challenges are not written if the git status of the destination directory is not clean, unless the force flag is used
- the files and directories listed in `**/.challengifyignore*` and `.syncignore` are ignored (wildcards supported: `**/*.pickle`)
- the files having a name containing uppercase `WIP`, `HIDDEN`, `ARCHIVE` or `OLD` are ignored
- replacements are handled depending on file extension: `.ipynb`, `.py`, `.rb` and notebook language (python, ruby)

assumptions:
- the user will verify the outcome and commit or revert the changes

## transformations

[challengify tranformations](public/README.md)

## transformations rollback

the destination directory is assumed to be git controlled

``` bash
git restore .                           # remove uncommitted changes in existing files

git clean -nfd                          # remove added files, dry run
# git clean -fd                         # actually remove added files
```
