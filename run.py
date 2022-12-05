# Adapted from https://stackoverflow.com/a/54956419

from sys import stdin, argv
from importlib import util as importlib_util

file_path = argv[1]
lines = [line.strip() for line in stdin]

spec = importlib_util.spec_from_file_location('solver', file_path)
module = importlib_util.module_from_spec(spec)
spec.loader.exec_module(module)

# check if it's all there..
# def bla(mod):
#     print(dir(mod))
# bla(module)

module.solve(lines)
