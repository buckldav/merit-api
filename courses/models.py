from unicodedata import category
from django.db import models
from colorfield.fields import ColorField
from icons.names import FA_ICON_NAMES


class CourseTag(models.Model):
    tag = models.CharField(max_length=20, unique=True)
    content = models.CharField(max_length=20)
    color = ColorField()
    fa_icon_name = models.CharField(max_length=50, choices=FA_ICON_NAMES)

    def __str__(self):
        return self.tag


class Course(models.Model):
    COURSE_CATEGORIES = [
        ('GEN', 'Explorer General'),
        ('SPE', 'Explorer Specific'),
        ('COM', 'Completer')
    ]

    name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=10, choices=COURSE_CATEGORIES)
    semester = models.BooleanField()
    fullyear = models.BooleanField()
    dstudies = models.BooleanField()
    science = models.BooleanField()
    description = models.JSONField()
    units = models.JSONField()
    tags = models.ManyToManyField(to=CourseTag)
    prereqs = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
