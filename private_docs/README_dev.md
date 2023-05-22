
## generate code profile

``` bash
python -m cProfile -o file.prof ../challengify/wagon_sync/run_iterate.py
```

## profiling viz using snakeviz

``` bash
pip install snakeviz

snakeviz file.prof                                          # visualise profile
```

## profiling viz using graphviz + gprof2dot

``` bash
pip install graphviz gprof2dot

gprof2dot -f pstats file.prof | dot -Tpng -o output.png     # visualise profile
```
