
`challengify iterate` generates iterative solution exercices based on a `.challengify_iterate.yml` conf file

## commands

``` bash
challengify iterate .                   # generate iterative solution exercices

challengify iterate . -c base..api      # generate challenge version from base to api
challengify iterate . -c base..         # generate challenge version from base
challengify iterate . -c ..api          # generate challenge version to api
challengify iterate . -c api            # generate challenge version api
challengify iterate . -c 1..3           # generate challenge versions from 1 to 3 included
```

## conf file

``` yaml
iterate:

  # list of files and directories to process (currently only supports one)
  source: taxifare

  # path to the destination directory from the root of the project
  destination: ../data-solutions/07-ML-Ops

  # list of challenge versions to process along with target directory relative to the `destination`
  versions:
    base: 01-Train-at-scale/04-Investigating-bottlenecks
    api: 04-Predict-in-production/01-Build-your-API
    docker_image: 04-Predict-in-production/02-Docker-image
    docker_prod: 04-Predict-in-production/03-Deploy-to-Cloud-Run
    api_advanced: 04-Predict-in-production/04-API-advanced

  # list of directories containing versioned files along with the versioned files target directory relative to the challenge version `target directory`
  versioned:
    versioned/01:         .             # root of challenge version `target directory`
    versioned/02:         taxifare      # path inside of challenge version `target directory`

  # list of rules defining on which versions of the challenge a file is present
  only:
    to:
      api:
        - taxifare/introduction.md
    for:
      api:
        - taxifare/notebooks/api_boilerplate.ipynb
        - taxifare/notebooks/api_usage.ipynb
    from:
      api:
        - taxifare/api/__init__.py
        - taxifare/api/fast.py
      docker_image:
        - taxifare/Dockerfile
        - taxifare/Dockerfile_intel
        - taxifare/Dockerfile_silicon
        - taxifare/requirements_intel.txt
        - taxifare/requirements_silicon.txt
```

![version rules](challengify-iterate.png)

## notebook delimiters

currently not supported

## code file delimiters (version tags)

| start | end | versions presence |
| --- | --- | --- |
| `# $ONLY_TO_version_BEGIN` | `# $ONLY_TO_version_END` | up to `version` (included) |
| `# $ONLY_FOR_version_BEGIN` | `# $ONLY_FOR_version_END` | only for version `version` |
| `# $ONLY_FROM_version_BEGIN` | `# $ONLY_FROM_version_END` | from `version` (included) |

example:
``` python
# $ONLY_FOR_api_BEGIN
# content only available for version api of the challenge
# $ONLY_FOR_api_END
```

troubleshoot: a delimiter having a version (`12`) outside of the range of versions defined in the conf file (`14` to `15`) will be ignored

## delimiter generators (version meta tags)

generates a `verb` delimiter (`CHALLENGIFY`, `CHA`, `DELETE`, `DEL`, `ERASE`, `WIPE`, `IMPLODE`) for the version

| start | end | versions presence |
| --- | --- | --- |
| `# $verb_ONLY_FOR_version_BEGIN` | `# $verb_ONLY_FOR_version_END` | `verb` only for version `version` |

example:
``` python
# $CHA_ONLY_FOR_api_BEGIN
# content challengified for version api of the challenge and available as is for other versions
# $CHA_ONLY_FOR_api_END
```

## versioned files

versioned files allow to reference multiple files with colliding generation path (such as `README.md`) in several challenge versions

they are useful in the eventuality that a file massively changes from a challenge version to another, as is typically the case with `README.md` files

versioned files are identified by their location in one of the directories listed in the `versioned` conf key and their matching of the versioned file naming convention

the `versioned` conf key references a list of directories containing versioned files along with the location in the generated challenge version in which to generate them

the number and depth of directories containing versioned files does not matter at all and is there only for organisational purposes

the versioned file should follow the pattern `number_baseroot_versionextension` (such as `01_README_api.md`), which generates the `target_directory/baserootextension` file (such as `./README.md`):
- `number` can  be any list of integers such as `0123`
- `baseroot` can  be any file root such as `README`
- `version` can  be any challenge version
- `extension` can be a file extension such as `.md` or can be empty
- `target_directory` can be any nested path or `.` for the root of the generated challenge version

by essence versioned files are distributed to a single challenge version:
- annotating the content with version tags or meta tags works but does not make sense
- annotating the content with challengify tags works and makes sense if necessary

with the following configuration:

``` yaml
  versioned:
    versioned/01:         .
    versioned/02:         taxifare
```

the following files will be processed only for the `api` challenge version:
- `versioned/01/01_README_api.md` will generate a `README.md` at the root of the challenge version
- `versioned/02/123_Dockerfile_api` will generate a `taxifare/Dockerfile` in the challenge version
