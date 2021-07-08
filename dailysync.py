#!/usr/bin/env python3
import subprocess
from multiprocessing import Pool
from functools import partial

src = "/home/student-04-1fe39127a0fc/data/prod/"
dest = "/home/student-04-1fe39127a0fc/data/prod_backup/"

src1 = src + "alpha/"
src2 = src + "beta/"
src3 = src + "delta/"
src4 = src + "gamma/"
src5 = src + "kappa/"
src6 = src + "omega/"
src7 = src + "sigma/"
srcs = [src1, src2, src3, src4, src5, src6, src7]

dest1 = dest + "alpha/"
dest2 = dest + "beta/"
dest3 = dest + "delta/"
dest4 = dest + "gamma/"
dest5 = dest + "kappa/"
dest6 = dest + "omega/"
dest7 = dest + "sigma/"
dests = [dest1, dest2, dest3, dest4, dest5, dest6, dest7]

def run(src, dest):
        subprocess.call(["rsync", "-arq", src, dest])

p = Pool(7)
A = p.starmap(run, zip(srcs, dests))
print(A)

