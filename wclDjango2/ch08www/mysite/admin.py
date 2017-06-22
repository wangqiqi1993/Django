from django.contrib import admin
from mysite import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('nickname','message','enabled','pub_time')
	ordering = ('-pub_time',)
	search_fields = ('nickname',)

admin.site.register(models.Mood)
admin.site.register(models.Post,PostAdmin)
