from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(verify_certs=True)

INDEX = "index_gaurav5"
DOC = "doc_ex5"

# Create index and mapping
request_body = {
    'mappings': {
        DOC: {
            'properties': {
                "location": {
                    "type": "geo_shape",
                    "tree": "quadtree",
                    "precision": "1m"
                }
            }
        }
    }
}
result = es.indices.create(index=INDEX, body=request_body)
print("creating 'example_index' index..." + str(result))

data = []
b = {
    "location": {
        "type": "circle",
        "coordinates": [77.5942812, 12.9356356],
        "radius": "5000m"
    }
}
for i in range(0, 5):
    action = {
        "_index": INDEX,
        "_type": DOC,
        "_id": i,
        "_source": b
    }
    data.append(action)

helpers.bulk(es, data)
res = es.search(body={"query": {"match_all": {}}}, index=INDEX)
print(res)
