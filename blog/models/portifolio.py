from django.db import models

class Projeto(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.URLField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
