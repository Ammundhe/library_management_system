from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=255)
    descriptions=models.TextField()

    def __str__(self) -> str:
        return str(self.name)
class category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return str(self.name)

class Book(models.Model):
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField()
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.name)