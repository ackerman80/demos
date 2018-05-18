from elasticsearch import Elasticsearch
es = Elasticsearch(['elasticsearch.default.svc.cluster.local:9200'])

print("Deleting Book 1")

res = es.delete(index="sidious", doc_type="tome", id=1)

print("Deleting Book 2")

res = es.delete(index="sidious", doc_type="tome", id=2)
