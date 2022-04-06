from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as Authlogin, authenticate
from django.contrib.auth import logout as Authlogout
from library.models import category
from .modelForms import User_modelForms
from django.contrib.auth import get_user_model
User = get_user_model()


class Login(View):

    template_name='login.html'
    form_class=AuthenticationForm
    categories=category.objects.all()

    def get(self,request):
        form=self.form_class()
        context={
            'categories':self.categories,
            'form':form,
        }
        return render(request, self.template_name,context )

    def post(self, request):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            Authlogin(request, form.get_user())
            return redirect('HomePage')
       
        context={
            'categories':self.categories,
            'form':form,
            }
        return render(request, self.template_name,context )

def Logout(request):
    Authlogout(request)
    return redirect('HomePage')

class create_account(View):
    template_name='createAccount.html'
    form_class=User_modelForms
    categories=category.objects.all()


    def get(self, request):
        create_userForm=self.form_class()
        context={
            'categories':self.categories,
            'form':create_userForm,
        }
        
        return render(request, self.template_name, context)

    def post(self, request):
        new_account=self.form_class(request.POST)
        if new_account.is_valid():
            first_name=new_account.cleaned_data.get('first_name')
            last_name=new_account.cleaned_data.get('last_name')
            email=new_account.cleaned_data.get('email')
            password=new_account.cleaned_data.get('password')
            user=User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.set_password(password)
            user.save()
            user_auth=authenticate(email=email, password=password)
            Authlogin(request, user_auth)
            return redirect("HomePage")
        else:
            new_account=self.form_class()
        return redirect("Create_account")