from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from utility import get_file_upload_location

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    roll_no = models.CharField(max_length=50)
    college_name = models.CharField(max_length=150)
    active = models.BooleanField(default=False)
    current_address = models.TextField(null=True, default=None, blank=True)
    permanent_address = models.TextField()
    current_number = models.CharField(max_length=20)
    alternate_email = models.EmailField(max_length=200, default=None, null=True, blank=True)
    current_status = models.TextField(default=None, null=True, blank=True)
    working_at = models.CharField(max_length=255, default=None, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.user
    class Meta:
        unique_together = ('roll_no','college_name')

class Content(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField(default=None, null=True, blank=True)
    owner = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField(default=None, null=True, blank=True)
    location = models.FileField(upload_to=get_file_upload_location)
    content = models.ForeignKey(Content, default=None, null=True, blank=True)
    uploaded_by = models.ForeignKey(User)
    album = models.ForeignKey(Album)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User)
    content = models.ForeignKey(Content)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.owner+'_'+self.content