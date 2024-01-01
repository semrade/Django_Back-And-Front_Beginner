from django.db import models

# Create your models here.
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    graduation_year = models.PositiveIntegerField()

    def __str__(self):
        return self.degree

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.job_title