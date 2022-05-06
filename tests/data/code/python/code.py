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

    # $CODE_BEGIN
    return 42
    # $CODE_END


def new_cha_delimiter():
    # $CHA_BEGIN
    return 42
    # $CHA_END

# $CODE_BEGIN
return 42
# $CODE_END


this_is_not_removed = True

# $DELETE_BEGIN
this_is_removed = True
# $DELETE_END

# $DEL_BEGIN
new_del_delimiter = True
# $DEL_END

this_is_not_removed_either = True

# the delete delimiters do not consume the line of the block
# before the block
# $DEL_BEGIN
tralala = True
# $DEL_END
# after the block

# the erase delimiters consume the line of the block
# before the block
# $ERASE_BEGIN
trololo = True
# $ERASE_END
# after the block

# the wipe delimiters consume the line of the block and the line after
# in order to keep outer blocks evenly spaced
# before the block

# $WIPE_BEGIN
trilili = True
# $WIPE_END

# after the block

# the implode delimiters consume the line of the block and the lines around the block
# in order to remove outer blocks spacing
# before the block

# $IMPLODE_BEGIN
trululu = True
# $IMPLODE_END

# after the block

    # the delete delimiters do not consume the line of the block
    # before the block
    # $DEL_BEGIN
    tralala = True
    # $DEL_END# <-- indentation still there
    # after the block

    # the erase delimiters consume the line of the block
    # before the block
    # $ERASE_BEGIN
    trololo = True
    # $ERASE_END
    # after the block

    # the wipe delimiters consume the line of the block and the line after
    # in order to keep outer blocks evenly spaced
    # before the block

    # $WIPE_BEGIN
    trilili = True
    # $WIPE_END

    # after the block

    # the implode delimiters consume the line of the block and the lines around the block
    # in order to remove outer blocks spacing
    # before the block

    # $IMPLODE_BEGIN
    trululu = True
    # $IMPLODE_END

    # after the block

# inline replacement# $DELETE_BEGIN for code or text # $DELETE_END sample
if __name__ == '__main__':
    # $CHALLENGIFY_BEGIN
    res = function()
    print(res)
    # $CHALLENGIFY_END
