
import pandas as pd

if __name__ == '__main__':
    json_arhive = pd.read_json('arxiv-metadata-oai-snapshot.json',lines=True)
    df = json_arhive.filter(['title','categories'], axis=1)
    df.to_pickle('bd')
    print("yes")