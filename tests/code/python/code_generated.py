""" this is a sample python challenge file """

import pandas as pd




def function():
    """
    return the answer to life the universe and everything
    """
    pass  # YOUR CODE HERE


def new_cha_delimiter():
    # $CHA_BEGIN
    return 42
    # $CHA_END


this_is_not_removed = True



# $DEL_BEGIN
new_del_delimiter = True
# $DEL_END

this_is_not_removed_either = True

# the delete delimiters do not consume the line of the block
# before the block
# $DEL_BEGIN
# $DEL_END
# after the block

# the erase delimiters consume the line of the block
# before the block
# $ERASE_BEGIN
tralala = True
# $ERASE_END
# after the block

# the wipe delimiters consume the line of the block and the line after
# in order to keep outer blocks evenly spaced
# before the block

# $WIPE_BEGIN
trololo = True
# $WIPE_END

# after the block

# the implode delimiters consume the line of the block and the lines around the block
# in order to remove outer blocks spacing
# before the block

# $IMPLODE_BEGIN
trilili = True
# $IMPLODE_END

# after the block

# inline replacement sample
if __name__ == '__main__':
    pass  # YOUR CODE HERE
