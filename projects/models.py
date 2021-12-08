from django.db import models


class Project(models.Model):
    WEBSITE = 'W'
    WEBGL_GAME = 'G'
    REPL = 'R'

    TYPES = [
        ('REPL', 'Repl Console App'),
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

    def __str__(self):
        return f"{self.title} - {self.author}"
