from django.db import models
from tinymce.models import HTMLField


class News(models.Model):
    title = HTMLField()
    source = models.CharField(max_length=255)
    image = models.ImageField(upload_to="news/")
    date_added = models.CharField(max_length=255)
    long_description = HTMLField()
    short_description = HTMLField()

    def __str__(self):
        return self.title


class AapatKalinSewa(models.Model):
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    contact_person_or_institute = models.CharField(max_length=255)

    def __str__(self):
        return self.phone_number


class Numbers(models.Model):
    parikshyan_gariyeko = models.CharField(max_length=255)
    sankraman_nadekhiyeko = models.CharField(max_length=255)
    sankraman_dekhiyeko = models.CharField(max_length=255)
    in_isolation = models.CharField(max_length=255)
    niko_bhayeko = models.CharField(max_length=255)
    mrityu_bhayeko = models.CharField(max_length=255)

    def __str__(self):
        return "Numbers"
