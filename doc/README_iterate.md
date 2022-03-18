
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

## code file delimiters

| start | end | versions presence |
| --- | --- | --- |
| `# $ONLY_TO_version_BEGIN` | `# $ONLY_TO_version_END` | up to `version` (included) |
| `# $ONLY_FOR_version_BEGIN` | `# $ONLY_FOR_version_END` | only for version `version` |
| `# $ONLY_FROM_version_BEGIN` | `# $ONLY_FROM_version_END` | from `version` (included) |

### delimiter generator delimiters

| start | end | versions presence |
| --- | --- | --- |
| `# $CHA_ONLY_TO_version_BEGIN` | `# $CHA_ONLY_TO_version_END` | `challengify` up to `version` (included) |
| `# $CHA_ONLY_FOR_version_BEGIN` | `# $CHA_ONLY_FOR_version_END` | `challengify` only for version `version` |
| `# $CHA_ONLY_FROM_version_BEGIN` | `# $CHA_ONLY_FROM_version_END` | `challengify` from `version` (included) |
| `# $DEL_ONLY_TO_version_BEGIN` | `# $DEL_ONLY_TO_version_END` | `delete`  up to `version` (included) |
| `# $DEL_ONLY_FOR_version_BEGIN` | `# $DEL_ONLY_FOR_version_END` | `delete`  only for version `version` |
| `# $DEL_ONLY_FROM_version_BEGIN` | `# $DEL_ONLY_FROM_version_END` | `delete`  from `version` (included) |
| `# $ERASE_ONLY_TO_version_BEGIN` | `# $ERASE_ONLY_TO_version_END` | `erase` up to `version` (included) |
| `# $ERASE_ONLY_FOR_version_BEGIN` | `# $ERASE_ONLY_FOR_version_END` | `erase` only for version `version` |
| `# $ERASE_ONLY_FROM_version_BEGIN` | `# $ERASE_ONLY_FROM_version_END` | `erase` from `version` (included) |
| `# $WIPE_ONLY_TO_version_BEGIN` | `# $WIPE_ONLY_TO_version_END` | `wipe` up to `version` (included) |
| `# $WIPE_ONLY_FOR_version_BEGIN` | `# $WIPE_ONLY_FOR_version_END` | `wipe` only for version `version` |
| `# $WIPE_ONLY_FROM_version_BEGIN` | `# $WIPE_ONLY_FROM_version_END` | `wipe` from `version` (included) |
| `# $IMPLODE_ONLY_TO_version_BEGIN` | `# $IMPLODE_ONLY_TO_version_END` | `implode` up to `version` (included) |
| `# $IMPLODE_ONLY_FOR_version_BEGIN` | `# $IMPLODE_ONLY_FOR_version_END` | `implode` only for version `version` |
| `# $IMPLODE_ONLY_FROM_version_BEGIN` | `# $IMPLODE_ONLY_FROM_version_END` | `implode` from `version` (included) |

example:
``` python
# $ONLY_FOR_api_BEGIN
# content only available for version api of the challenge
# $ONLY_FOR_api_END
```

troubleshoot: a delimiter having a version (`12`) outside of the range of versions defined in the conf file (`14` to `15`) will be ignored
