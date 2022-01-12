from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=60)
    designation = models.CharField(max_length=60)
    salary = models.IntegerField()
    city = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name
    