from django.db import models

class Question(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    country = models.CharField(max_length=250)
    question = models.TextField()

    def __str__ (self):
        return self.name

class Testimony(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    country = models.CharField(max_length=250)
    testimony = models.TextField()

    class Meta:
        verbose_name_plural='Testimonies'

    def __str__(self):
        return self.name

class Prayer(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    country = models.CharField(max_length=250)
    prayer = models.TextField()

    def __str__(self):
        return self.name
