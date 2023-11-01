from django.db import models

# Create your models here.

class Canal10(models.Model):
    
    link = models.CharField(max_length=100)

    
    def __str__(self):
        return "URL"

    class Meta():
        verbose_name="Canal10"
        verbose_name_plural="Canal10"

class Canal26(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return "URL"

    class Meta():
        verbose_name="Canal26"
        verbose_name_plural="Canal26"

class C5N(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return "URL"

    class Meta():
        verbose_name="C5N"
        verbose_name_plural="C5N"


class Cronica(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return "URL"

    class Meta():
        verbose_name="Cronica"
        verbose_name_plural="Cronica"


class DTV(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return "URL"

    class Meta():
        verbose_name="DTV"
        verbose_name_plural="DTV"

class LN(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return "URL"

    class Meta():
        verbose_name="LN"
        verbose_name_plural="LN"

class Telefe(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return "URL"

    class Meta():
        verbose_name="Telefe"
        verbose_name_plural="Telefe"

class TN(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return "URL"

    class Meta():
        verbose_name="TN"
        verbose_name_plural="TN"

class TVP(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self):
        return "URL"

    class Meta():
        verbose_name="TVP"
        verbose_name_plural="TVP"
    