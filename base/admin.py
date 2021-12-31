from django.contrib import admin

# Register your models here.

from .models import Profiles, Resumes

class profileAdmin(admin.ModelAdmin):
    list_display=['id','name']

class resumeAdmin(admin.ModelAdmin):
    list_display=['id','file','profile_id']

admin.site.register(Profiles, profileAdmin)
admin.site.register(Resumes, resumeAdmin)
