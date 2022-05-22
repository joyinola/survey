from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .resources import VoteResource
# Register your models here.
class UserAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	pass
admin.site.register(Utilizer,UserAdmin)

class VoteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	resource_class=VoteResource
admin.site.register(Vote,VoteAdmin)
class VoteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	resource_class=HeadlinesResource
admin.site.register(HeadLines)
