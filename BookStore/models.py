from django.db import models

# Create your models here.



class Book(models.Model):
    title =  models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length= 50)
    page_count = models.IntegerField()
    cover_image = models.ImageField(upload_to='cover_image')
    language = models.CharField(max_length= 50)


    def __str__(self) -> str:
        return self.title