#!/usr/bin/python3
# 101-safe_function.py
# wakjira Bekele <wakjirabekele2018@gmail.com>

#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    return result
