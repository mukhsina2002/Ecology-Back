from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    description = models.TextField(null=True)
    description_ru = models.TextField(null=True)
    type = models.CharField(max_length=50)
    type_ru = models.CharField(max_length=50)
    image = models.ImageField(upload_to='animal_images/')
    background_image = models.ImageField(upload_to='animal_backgrounds/')
    link = models.TextField()

    def __str__(self):
        return self.name


class NaturalResources(models.Model):
    title = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    about = models.CharField(max_length=250)
    about_ru = models.CharField(max_length=250)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title


class Plant(models.Model):
    title = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    description = models.TextField(null=True)
    description_ru = models.TextField(null=True)
    type = models.CharField(max_length=50)
    type_ru = models.CharField(max_length=50)
    image = models.ImageField(upload_to='plant_images/')
    background_image = models.ImageField(upload_to='plant_backgrounds/')
    link = models.TextField()
    youtube_url = models.TextField()

    def __str__(self):
        return self.title


class Utilize(models.Model):
    title = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    type = models.CharField(null=True, max_length=50)
    type_ru = models.CharField(null=True, max_length=50)
    image = models.ImageField(upload_to='utilize_images/')
    description = models.TextField()
    description_ru = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.title
