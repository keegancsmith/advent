#!/usr/bin/env python

import json
import sys

def f(x):
    if isinstance(x, dict):
        if "red" in x.values():
            return 0
        return sum(f(v) for k, v in x.items())
    elif isinstance(x, list):
        return sum(f(y) for y in x)
    else:
        try:
            return int(x)
        except:
            return 0

x = json.load(sys.stdin)
print f(x)

