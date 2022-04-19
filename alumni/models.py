from django.db import models


class College(models.Model):
    name = models.CharField(max_length=50, primary_key=True)  # pk

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=50, primary_key=True)  # pk

    def __str__(self):
        return self.name


class Achievement(models.Model):
    name = models.CharField(max_length=50, primary_key=True)  # pk

    def __str__(self):
        return self.name


class Alum(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    grad_year = models.PositiveIntegerField()
    college = models.ForeignKey(to=College, null=True, blank=True, on_delete=models.SET_NULL)
    job = models.ForeignKey(to=Job, null=True, blank=True, on_delete=models.SET_NULL)
    achievements = models.ManyToManyField(to=Achievement, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
