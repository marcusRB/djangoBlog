from django.contrib import admin

# Register your models here.
from .models import Posts



class PostAdmin(admin.ModelAdmin):
	list_display = ["__str__", "data"]
	list_filter = ["data"]
	search_fields = ["title", "content"]
	prepopulated_fields = {"slug": ("title",)}

	class Meta:
		model = Posts


admin.site.register(Posts, PostAdmin)