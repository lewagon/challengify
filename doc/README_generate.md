
## generate

generate default parameters conf file in `~/.challengify.yaml`:

``` bash
challengify gen                         # generate conf file
challengify gen --force                 # override existing conf file
```

default conf file:

``` yaml
run:
  destination: ../data-challenges
  force: False
  dry_run: False
  verbose: False
  all: False
```
