from django.db import models


class Project(models.Model):
    GOOGLE_SITE = 'GOOG'
    REPL = 'REPL'
    WEB_APP = 'APP'
    WEBGL_GAME = 'GAME'
    WEBSITE = 'SITE'

    TYPES = [
        ('GOOGLE_SITE', 'Google Site'),
        ('REPL', 'Repl Console App'),
        ('WEB_APP', 'Web App'),
        ('WEBGL_GAME', 'WebGL Game'),
        ('WEBSITE', 'Website'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(default="A project I made at Merit Academy.")
    url = models.URLField(max_length=200)
    project_type = models.CharField(
        max_length=20,
        choices=TYPES,
        default=REPL,
    )
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
