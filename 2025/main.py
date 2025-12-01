#!/usr/bin/env python

import argparse
import os
from contextlib import chdir

argParser = argparse.ArgumentParser()
argParser.add_argument(
    "day", type=int, help="Day to run"
)

argParser.add_argument(
    "part", type=int, help="Part to run", choices=[1,2]
)

args = argParser.parse_args()

if args.day < 1 or args.day > 12:
    print("Invalid day")
    exit(1)

directory = f"{args.day}"
filename = f"{args.day}_{args.part}.py"

if  not os.path.exists(directory) or not os.path.exists(directory + "/" + filename):
    print(f"Day {args.day} part {args.part} hasn't been done")
    exit(1)

with chdir(directory):
    exec(open(filename).read())
