import numpy as np
import pandas as pd
import json
from scholarly import scholarly
import time
from scholarly import ProxyGenerator
pd.options.mode.chained_assignment = None

if __name__ == '__main__':
    pg = ProxyGenerator()
    pg.Tor_Internal(tor_cmd='C:\\Users\\yaros\\OneDrive\\Desktop\\TorBrowser\\Browser\\TorBrowser\\Tor\\tor.exe')
    scholarly.use_proxy(pg)

    bd = pd.read_pickle('bd')
    i = 0
    for article in bd.iloc:
        i += 1
        if article['num_citations'] is None:
            search_query = scholarly.search_pubs(article['title'])
            Response = next(search_query)
            article['num_citations'] = Response['num_citations']
            bd.to_pickle('bd')
            print("done: " +str(i) +'of 1796911' )
            time.sleep(10)