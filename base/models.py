from django.db import models
# from django.db.models.base import Model
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


# Create your models here.

class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteModel(models.Model):

    is_deleted = models.BooleanField(default=False)
    objects = models.Manager()
    undeleted_objects = SoftDeleteManager()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class Profiles(SoftDeleteModel):

    # profile_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)
    summary=models.TextField()
    # MiddleName=models.CharField(null=True, blank=True, max_length=500)
    # LastName=models.CharField(max_length=500)
    # Resumes=models.CharField(max_length=500)
    # isDelete=models.BooleanField()  # for soft delete purpose, 
    #                                 # True means the profile was deleted by the user.

    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

# One to many relationships.
# One profile can have several resumes.
class Resumes(models.Model):
    def nameFile(instance, filename):
        # hash = random.getrandbits(128)
        return '/'.join(['resumes', str(instance.profile), filename[:-4]+str(datetime.now())+".pdf"])
        # I am only allowing pdf file uploads.
        # the Frontend should be responsible for uploading only pdf documents.

    # name = models.CharField(max_length=500)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profiles,on_delete=models.CASCADE)
    file = models.FileField(upload_to=nameFile)

    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)