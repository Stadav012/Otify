from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    password = models.CharField(max_length=50)
    region = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class ComplainCategory(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Region(models.Model):
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.region


class Complaint(models.Model):
    category = models.ForeignKey(ComplainCategory, null=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    region = models.ForeignKey(Region, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.category.category + " --> " + self.region.region