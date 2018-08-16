#!/usr/bin/env python

import fileinput
import re

tool_pattern=re.compile(r"^\s*(T[0-9])")

for line in fileinput.input(inplace=True, backup='.bak'):
    print tool_pattern.sub('A602 \g<1>', line),