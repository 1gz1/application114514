from tqdm.tk import trange
from Source.const import *

def progress():
    for i in trange(const['trange_n']):
        i += 1
