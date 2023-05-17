
## transformations

### notebook cell tags

the tags can be viewed using the menu `View > Cell Toolbar > Tags`

| tag | usage |
| --- | --- |
| `delete` | the cell is deleted |
| `delete_begin` | delete all further cells, including this one |
| `delete_end` | last cell to be deleted by `delete_begin` |
| `challengify` | the content of the cell is replaced |
| `steps` | single line comments are kept, everything else after the first comment is replaced |
| `clear_output` | the output and standard error of the cell are emptied (only valid if the `keep_output` notebook metadata option is set to True) |

### notebook cell content delimiters

| start | end | content |
| --- | --- | --- |
| `$CHALLENGIFY_BEGIN` | `$CHALLENGIFY_END` | replaced by pass comment |
| `$DELETE_BEGIN` | `$DELETE_END` | deleted |

### notebook metadata

the output and standard error of all cells is deleted unless the following conf is added to the notebook metadata

the notebook metadata can be edited using the menu `Edit > Edit Notebook Metadata`

``` json
  "challengify": {
    "keep_output": true
  },
```

### text file delimiters

| start | end | content usage |
| --- | --- | --- |
| `# $CHALLENGIFY_BEGIN` | `# $CHALLENGIFY_END` | replaced by pass comment |
| `# $CHA_BEGIN` | `# $CHA_END` | replaced by pass comment |
| `# $DELETE_BEGIN` | `# $DELETE_END` | deleted |
| `# $DEL_BEGIN` | `# $DEL_END` | deleted |
| `# $ERASE_BEGIN` | `# $ERASE_END` | block newline is consumed |
| `# $WIPE_BEGIN` | `# $WIPE_END` | block newline + following newline are consumed |
| `# $IMPLODE_BEGIN` | `# $IMPLODE_END` | block newline + surrounding newlines are consumed |

`challengify` keeps indentation

<img src="img/cha.png" alt="cha" width="700"/>

`delete` does not consume the block newline

<img src="img/del.png" alt="del" width="700"/>

`erase` consumes the block newline

<img src="img/erase.png" alt="erase" width="700"/>

`wipe` consumes the block newline and the following one in order to keep outer blocks evenly spaced

<img src="img/wipe.png" alt="wipe" width="700"/>

`implode` consumes the block newline and the surrounding newlines in order to remove outer blocks spacing

<img src="img/implode.png" alt="implode" width="700"/>

## replacements

notebook replacements occur depending on cell type (markdown or code) and metadata declared language

text file replacements occur depending on the language (file extension)

| language | replacement |
| --- | --- |
| notebook markdown | `> YOUR ANSWER HERE` |
| python | `pass  # YOUR CODE HERE` |
| other | `# YOUR CODE HERE` |
