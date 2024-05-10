from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
