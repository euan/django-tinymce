from django.db import models
from django.contrib import admin

from filebrowser.fields import FileBrowseField

from util import custom_fields

class Publication(models.Model):
    image = FileBrowseField("Image", max_length=200, blank=True, null=True)
    image_initialdir = FileBrowseField("Image (Initial Directory)", max_length=200, directory="images/", blank=True, null=True)
    image_extensions = FileBrowseField("Image (Extensions)", max_length=200, extensions=['.jpg'], help_text="Only jpg-Images allowed.", blank=True, null=True)
    image_format = FileBrowseField("Image (Format)", max_length=200, format='Image', blank=True, null=True)
    pdf = FileBrowseField("PDF", max_length=200, directory="documents/", extensions=['.pdf'], format='Document', blank=True, null=True)
    
    my_field = custom_fields.HTMLField()

admin.site.register(Publication)