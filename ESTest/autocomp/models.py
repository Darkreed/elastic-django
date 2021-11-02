from django.db import models
from .search import DeviceTypeIndex

# Create your models here.

class DeviceType(models.Model):
	manufacturer_id=models.CharField(max_length=50)
	solutiontype_id=models.CharField(max_length=50)
	devicetype_id=models.CharField(max_length=50)
	device_name=models.CharField(max_length=20)
	active=models.IntegerField()

	def indexing(self):   
		obj = DeviceTypeIndex(
		meta={'id': self.id},
		manufacturer_id=self.manufacturer_id,
		solutiontype_id=self.solutiontype_id,
		devicetype_id=self.devicetype_id,
		device_name=self.device_name,
		active=self.active,
		)
		obj.save()
		return obj.to_dict(include_meta=True)