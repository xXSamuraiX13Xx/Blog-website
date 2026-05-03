from django.contrib import admin

# Register your models here.
from .models import Post

class Customize(admin.ModelAdmin):
	list_display = ['title', 'author', 'created_date', 'id', ]
	list_filter = ['created_date']
	search_fields = ['title']
	list_display_links = ['author']
	list_editable = ['title', 'created_date']
	prepopulated_fields = {"slug": ("title",)}

	class Meta:
		model = Post
admin.site.register(Post, Customize)
