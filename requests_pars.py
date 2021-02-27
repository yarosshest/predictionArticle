import numpy as np
import pandas as pd
import json
from scholarly import scholarly
import time
from scholarly import ProxyGenerator
import requests
pd.options.mode.chained_assignment = None

if __name__ == '__main__':
    bd = pd.read_pickle('bd')
    i = 0
    for article in bd.iloc:
        i += 1
        if article['num_citations'] is None:
            r = requests.get('https://scholar.google.com/scholar', params={'q':article['title']})
            count = r.text
            count[count.find('&#1062;&#1080;&#1090;&#1080;&#1088;&#1091;&#1077;&#1090;&#1089;&#1103;:'):]


            time.sleep(10)