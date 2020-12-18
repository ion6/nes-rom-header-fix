#!/usr/bin/env python

import argparse
import os
from   pathlib import Path
import subprocess

import lib

parser = argparse.ArgumentParser(description="Fix NES ROM headers.")
parser.add_argument('--path', required=True)
parser.add_argument('--ext', required=False)
parser.add_argument('--recursive', required=False, action="store_true")

args = parser.parse_args()

root_path       = Path(os.path.abspath(args.path))
extension       = args.ext
is_recursive    = args.recursive

if extension is None:
	extension = "nes"

if root_path.is_file():
    lib.fix_header(str(root_path))
else:
    lib.fix_headers(root_path, extension, is_recursive)
