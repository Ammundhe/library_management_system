from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name)

class student(models.Model):
    name=models.CharField(max_length=255)
    deparment=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)
