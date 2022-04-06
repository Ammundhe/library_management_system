from django.shortcuts import redirect, render
from django.views import View
from library.models import Author, Book, category, Issue
from student.models import student, Department
from .modelForms import Issue_modelform
from datetime import datetime

class HomePage(View):
    template_name="HomePage.html"

    def get(self, request):
        categories=category.objects.all()
        author=Author.objects.all()
        context={
            "categories":categories,
            "author":author
        }
        return render(request, self.template_name, context)

class BookCategories(View):
    template_name="bookListing.html"
    
    def get(self, request, bookId=None):
        if bookId:
            books=Book.objects.filter(category_id=bookId)
            categories=category.objects.all()
            context={
                "categories":categories,
                "books":books,
            }
            return render(request, self.template_name, context)
        categories=category.objects.all()
        books=Book.objects.all()
        context={
            "categories":categories,
            "books":books,
        }
        return render(request, self.template_name, context)


class Student(View):
    template_name="student-list.html"

    def get(self, request, student_id=None):
        if student_id:
            categories=category.objects.all()
            Student=student.objects.filter(deparment_id=student_id)
            department=Department.objects.all()
            context={
                "categories":categories,
                "Student":Student,
                "department":department,
            }
            return render(request, self.template_name, context)
        categories=category.objects.all()
        Student=student.objects.all()
        department=Department.objects.all()
        context={
            "categories":categories,
            "Student":Student,
            "department":department,
        }
        return render(request, self.template_name, context)

class IssueDetails(View):
    template_name="Issue-details.html"
    categories=category.objects.all()
    form_class= Issue_modelform
    def get(self, request):
        form=self.form_class()
        context={
            "categories":self.categories,
            "form":form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        student=request.POST.get("student")
        book=request.POST.get("book")
        issued_value=request.POST.get("issued")
        returned_value=request.POST.get("returned")
        return_date=request.POST.get("return_date")
        if issued_value=="on":
            issued=True
        else:
            issued=False
        if returned_value=="on":
            returned=True
        else:
            returned=False
        Issue.objects.create(
            student_id=student,
            book_id=book,
            issued=issued,
            issued_at=datetime.now(),
            returned=returned,
            return_date=return_date
        )
        return redirect("BookCategories")

class IssueBooks(View):
    template_name="IssueBook.html"

    def get(self, request):
        issuedbooks=Issue.objects.all()
        categories=category.objects.all()

        context={
            "issuedbooks":issuedbooks,
            "categories":categories
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        if request.POST.get("returned"):
            Issued_id=request.POST.get("returned")
            Issuedbook=Issue.objects.get(id=Issued_id)
            Issuedbook.returned=True
            Issuedbook.save()
        if request.POST.get("delete"):
            Issued_id=request.POST.get("delete")
            Issuedbook=Issue.objects.get(id=Issued_id).delete()
        return redirect("IssueBooks")