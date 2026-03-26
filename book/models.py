from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField("Ism", max_length=100)
    last_name = models.CharField("Familya", max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField("Kitob nomi", max_length=200)
    description = models.TextField("Tavsif", blank=True)
    created_at = models.DateTimeField("Yaratilgan sana", auto_now_add=True)

    def __str__(self):
        return self.title