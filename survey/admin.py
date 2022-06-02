from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .resources import VoteResource,HeadlineResource
from django import forms
from django.db.models import Q
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
class GenerationForm(forms.ModelForm):

	class Meta:
		model=Generation
		fields=['name','is_active','prev_gen']
	def clean(self):
		cleaned_data=self.cleaned_data
		if cleaned_data.get('is_active')==True:
			if Generation.objects.filter(Q(is_active=True),~Q(name=cleaned_data.get('name'))):
				raise forms.ValidationError('An active generation already exists')
		return self.cleaned_data
class GenerationAdmin(admin.ModelAdmin):
	form=GenerationForm
	fields=['name','is_active','prev_gen']
admin.site.register(Generation,GenerationAdmin)