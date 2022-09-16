from unicodedata import category
from django.db import models

class Portfolio(models.Model):
    order = models.IntegerField(default='1')
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    portfolio_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Portfolio'

class Gallery(models.Model):
    order = models.IntegerField(default='1')
    title = models.CharField(max_length=255, blank=True)
    gallery_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Gallery'

class Project1(models.Model):
    order = models.IntegerField(default='1')
    category = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    project_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Cultural History'

class Project2(models.Model):
    order = models.IntegerField(default='1')
    category = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    project_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Natural History'

class Project3(models.Model):
    order = models.IntegerField(default='1')
    category = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    project_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Park Information'

class Project4(models.Model):
    order = models.IntegerField(default='1')
    category = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    project_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Resource Management'


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email