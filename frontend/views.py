from django.shortcuts import render
from django.views import View
from library.models import Author, Book, category

class HomePage(View):
    template_name="HomePage.html"

    def get(self, request):
        return render(request, self.template_name)
