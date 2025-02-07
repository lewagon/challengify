
generate challenges from solutions using code block delimiters

## content creators

the tool is private but is actionable by the content creators through the [challengify publication workflows](https://github.com/lewagon/.github/tree/main/workflow-deployer/configuration_files/challengify) deployed on the [solutions repositories](https://github.com/lewagon/.github/blob/main/workflow-deployer/params/deployments.yml)

the [public documentation](https://lewagon.github.io/challengify/) only covers the features used by the content creators:
- `challengify run` code file delimiters
- `challengify run` notebook tags

## project structure

```
docs                          public documentation depoyed through the `gh-pages` branch
private_docs                  internal documentation (private)
_config.yml                   jekyll theme for the github page
```

## install

``` bash
pip install git+https://github.com/lewagon/challengify
pip uninstall -y challengify            # uninstall
alias cha="challengify $@"              # alias
```

## sub commands

| command | usage |
| --- | --- |
| [iterate](private_docs/README_iterate.md) | generate several challenge versions from a single codebase |
| [test](private_docs/README_test.md) | generate temporary challengified files |
| [generate](private_docs/README_generate.md) | create `~/.challengify.yaml` conf file |
| [inject](private_docs/README_inject.md) | deprecated |

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

[challengify tranformations](docs/README.md)

## transformations rollback

the destination directory is assumed to be git controlled

``` bash
git restore .                           # remove uncommitted changes in existing files

git clean -nfd                          # remove added files, dry run
# git clean -fd                         # actually remove added files
```
