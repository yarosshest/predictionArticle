import numpy as np
import pandas as pd
import json
from scholarly import scholarly
import time
from scholarly import ProxyGenerator
pd.options.mode.chained_assignment = None
import json

if __name__ == '__main__':
    with open("dblp.v12.json", "r") as file:
        for line in file:
            print(line)