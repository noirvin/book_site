from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name       
class Book(models.Model):
    title = models.CharField(max_length=50)
    num_pages = models.IntegerField()
    date_published = models.DateField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
