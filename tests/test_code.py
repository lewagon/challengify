""" this is a sample python challenge file """

import pandas as pd

# $DELETE_BEGIN
import numpy as np
# $DELETE_END


def function():
    """
    return the answer to life the universe and everything
    """
    # $CHALLENGIFY_BEGIN
    return 42
    # $CHALLENGIFY_END


this_is_not_removed = True

# $DELETE_BEGIN
this_is_removed = True
# $DELETE_END

this_is_not_removed_either = True

# inline replacement# $DELETE_BEGIN for code or text # $DELETE_END sample
if __name__ == '__main__':
    # $CHALLENGIFY_BEGIN
    res = function()
    print(res)
    # $CHALLENGIFY_END
