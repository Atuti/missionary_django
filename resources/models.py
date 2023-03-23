from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class Ebooks(models.Model):
    title = models.CharField(max_length=350)
    ebook = models.FileField(upload_to='ebooks', blank=False, null=False)

    class Meta:
        verbose_name_plural='Ebooks'

    def get_ebook(self):
        return settings.WEBSITE_URL + self.ebook.url

    def __str__(self):
        return self.title

class Tracts(models.Model):
    title = models.CharField(max_length=350)
    tract = models.FileField(upload_to='tracts', blank=False, null=False)

    class Meta:
        verbose_name_plural='Tracts'

    def get_tract(self):
        return settings.WEBSITE_URL + self.tract.url

    def __str__(self):
        return self.title

class SabbathArchiveVideoLinks(models.Model):
    link = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    date_filed = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Links'

    def __str__(self):
        return self.title

class StudyToShowVideoLinks(models.Model):
    link = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    description = RichTextField(blank=False, null=False)

    class Meta:
        verbose_name_plural='StudyVideoLinks'

    def __str__(self):
        return self.title

class StudyGuides(models.Model):
    title = models.CharField(max_length=500)
    guide = models.FileField(upload_to='guides', blank=False, null=False)

    class Meta:
        verbose_name_plural='StudyGuides'

    def get_guide(self):
        return settings.WEBSITE_URL + self.guide.url

    def __str__(self):
        return self.title

class Events(models.Model):
    title = models.CharField(max_length=350)
    date = models.DateTimeField(auto_now_add=True)
    info = RichTextField(blank=False, null=False)
    image = models.ImageField(upload_to='events_images', blank=False, null=False)

    class Meta:
        verbose_name_plural='Events'

    def __str__ (self):
        return self.title
    
    def get_image(self):
        return settings.WEBSITE_URL + self.image.url