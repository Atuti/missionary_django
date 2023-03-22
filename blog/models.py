from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=350)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField()
    blog = RichTextField(blank=False, null=False)
    intro = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image_uploads', blank=False, null=False)

    def __str__ (self):
        return self.title

    def get_image(self):
        return settings.WEBSITE_URL + self.image.url

class News(models.Model):
    title = models.CharField(max_length=350)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    news = RichTextField(blank=False, null=False)
    intro = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='news_images', blank=False, null=False)

    class Meta:
        verbose_name_plural='News'

    def __str__ (self):
        return self.title
    
    def get_image(self):
        return settings.WEBSITE_URL + self.image.url

class Comment(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length= 200)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=False, null=False)

    def __str__ (self):
        return self.name