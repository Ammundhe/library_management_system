from django.db import models
from student.models import student



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
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name="bookCategory")
    name=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField()
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.name)

class Issue(models.Model):
    student=models.ForeignKey(student, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at=models.DateTimeField( auto_now=True)
    issued=models.BooleanField(default=False)
    issued_at=models.DateTimeField()
    returned=models.BooleanField()
    return_date=models.DateTimeField()
    def __str__(self) -> str:
        return str(self.student)

