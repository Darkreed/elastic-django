from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Integer, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection(hosts=['localhost'])
class DeviceTypeIndex(Document):    
	manufacturer_id = Text()
	solutiontype_id = Text()
	devicetype_id = Text()
	device_name = Text()
	active = Integer()
	
	# class Meta:        
	# 	index = 'devicetype-index'
	class Index:
		name = 'devicetype'
		settings = {
			"number_of_shards": 2,
		}

	def save(self, ** kwargs):

		return super(DeviceTypeIndex, self).save(** kwargs)

def bulk_indexing():    
	DeviceTypeIndex.init()    
	es = Elasticsearch()    
	bulk(client=es, actions=(b.indexing() for b in models.DeviceType.objects.all().iterator()))

def search_devtypeid(searchterm):
	client = Elasticsearch()
	s = Search(index='devicetype').using(client).query("match", devicetype_id=searchterm)

	response = s.execute()
	print(s.to_dict())
	for hit in s:
		print(hit.device_name)


# DeviceTypeIndex.init()


# devtype = DeviceTypeIndex(meta={'id': 42}, manufacturer_id='fe3e0c84-237f-11eb-871b-45a2479be20e', active=1)
# # devtype.body = ''' looong text '''
# devtype.save()

# devtype = DeviceTypeIndex.get(id=42)
# print(devtype.manufacturer_id)

# # Display cluster health
# print(connections.get_connection().cluster.health())