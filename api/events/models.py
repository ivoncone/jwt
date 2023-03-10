from django.db import models

# Create your models here.
class Events(models.Model):
	event_name = models.CharField(max_length=250)
	event_description = models.TextField()
	place = models.CharField(max_length=250)
	contact = models.CharField(max_length=250)
	reservation = models.URLField(max_length=20)
	date = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'eventos'
		ordering = ["-updated_at"]

	def __str__(self):
		return str(self.event_name)
