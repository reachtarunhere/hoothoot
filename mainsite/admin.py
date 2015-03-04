
from mainsite.models import *
# Register your models here.
from django import forms
from django.contrib import admin
from ckeditor.fields import RichTextFormField


class VideoAdminForm(forms.ModelForm):
    description = RichTextFormField()
    class Meta:
        model = Video


class VideoAdmin(admin.ModelAdmin):
    form = VideoAdminForm


admin.site.register(Tag)
admin.site.register(Video, VideoAdmin)
admin.site.register(Category)
admin.site.register(HandpickedVideo)
