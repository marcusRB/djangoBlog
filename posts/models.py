from django.db import models

# Create your models here.
class Posts(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	data = models.DateTimeField(auto_now=False, auto_now_add=True)
	slug = models.SlugField()

	def __str__(self):
		return self.title

