
import ast
import SQL
import ujson
import io

if __name__ == '__main__':
    db = SQL.createBd()
    with io.open("dblp.v12.json",encoding='utf-8') as file:
        for line in file:
            if line != '[\n':
                if line[0] == ',':
                    line = line[1:]
                d = ujson.loads(line)
                p = SQL.Papers()
                p.id_in_bd = d['id']
                p.title = d['title']

                if 'authors' in d:
                    p.authors = d['authors']
                    for author in d['authors']:
                        a = SQL.Authors()
                        a.name = author["name"]
                        if "org" in author:
                            a.org = author["org"]
                        if "id" in author:
                            a.id_in_bd = author['id']
                            db.addAuthor(a)

                if "venue" in d:
                    p.venue_raw = d["venue"]['raw']
                    if 'id' in d["venue"]:
                        p.venue_id = d["venue"]['id']
                    if 'type' in d['venue']:
                        p.venue_type = d['venue']['type']
                if "year" in d:
                    p.year = int(d['year'])

                if "fos" in d:
                    p.keywords = d["fos"]

                if 'n_citation' in d:
                   p.n_citation = d['n_citation']

                if 'references' in d:
                    p.references = d['references']

                if "doc_type" in d:
                    if 'doc_type' != '':
                        p.doc_type = d['doc_type']

                if 'lang' in d:
                    if 'lang' != '':
                        p.lang = d['lang']

                if "publisher" in d:
                    if 'publisher' != '':
                        p.publisher = d['publisher']

                if 'abstract' in d:
                    p.abstract = d['abstract']

                if 'indexed_abstract' in d:
                    p.indexed_abstract = d['indexed_abstract']

                if 'issn' in d:
                    p.issn = d['issn']

                if 'isbn' in d:
                    p.isbn = d['isbn']

                if 'doi' in d:
                    p.isbn = d['doi']

                if 'pdf' in d:
                    p.isbn = d['pdf']

                if 'url' in d:
                    p.isbn = d['url']
                db.addPaper(p)

                if 'authors' in d:
                    for author in d['authors']:
                        if "id" in author:
                            db.addAuthorship(str(author["id"]), str(d['id']))
                print((str(d['id']) + "done"))
                print((str(d['id']) + "already"))