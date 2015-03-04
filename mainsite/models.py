from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class BadaTest(models.Model):
	matter = models.TextField()
	def __unicode__(self):
		return str(self.id)

class Tag(models.Model):
	name = models.CharField(max_length = 100)
	def __unicode__(self):
		return str(self.name)

class Category(models.Model):
	name = models.CharField(max_length = 100)
	def __unicode__(self):
		return str(self.name)
		


						

class Video(models.Model):
	title = models.TextField()
	description = models.TextField()
	embed_link  = models.URLField()
	image_link  = models.URLField()
	thumb_link  = models.URLField()
	pub_date = models.DateTimeField()
	votes = models.IntegerField(default=0)
	tags = models.ManyToManyField('tag', blank = True)
	category = models.ForeignKey('category',null=True,blank = True)
	facebook_image = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return str(self.title)
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=15)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class HandpickedVideo(models.Model):
	number = models.IntegerField()
	video = models.ForeignKey('video', blank = True,null=True)