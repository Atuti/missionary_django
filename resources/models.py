from django.db import models
from django.conf import settings


class Ebooks(models.Model):
    title = models.CharField(max_length=350)
    ebook = models.FileField(upload_to='ebooks', blank=False, null=False)

    class Meta:
        verbose_name_plural='Ebooks'

    def get_ebook(self):
        return settings.WEBSITE_URL + self.ebook.url


