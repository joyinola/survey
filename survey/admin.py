from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .resources import VoteResource,HeadlineResource
# Register your models here.
class UserAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	pass
admin.site.register(Utilizer,UserAdmin)

class VoteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	resource_class=VoteResource

admin.site.register(Vote,VoteAdmin)

class HeadlineAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	resource_class=HeadlineResource
admin.site.register(HeadLines,HeadlineAdmin)

admin.site.register(Generation)
