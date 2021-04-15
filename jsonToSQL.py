import gc

import pandas as pd
from sqlalchemy.types import Integer, Text, String, DateTime
from sqlalchemy import create_engine, DateTime, func, Boolean, Float, PickleType
from os import environ
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('sqlite:///Papers', echo=False)
    for i in range(24,25):
        jobs_df = pd.read_json('dblp.v12_split/dblp.v12_%d.json'% i)
        jobs_df.to_sql(
            "Papers",
            engine,
            index=False,
            chunksize=500,
            if_exists="append",
            dtype={
                "id": Integer,
                "authors": PickleType,
                "title": String,
                "year": Integer,
                "n_citation": Integer,
                "page_start": Integer,
                "page_end": Integer,
                "doc_type": String,
                "publisher": String,
                "volume": Integer,
                "issue": Integer,
                "references": PickleType,
                "indexed_abstract": PickleType,
                "fos": PickleType,
                "venue": PickleType,
                "alias_ids": PickleType
            }
        )
        gc.collect()
        print("Done %d" % i)