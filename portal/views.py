from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import *

User = get_user_model()

class home(View):
    model = User
    template_name = 'portal/home.html'

    def get(self, request):

        return render(request, self.template_name)


class UserCreationFormView(View):
    form_class = UserCreationForm
    template_name = 'portal/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
            user = form.save()

            reg_no = form.cleaned_data['reg_no']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(reg_no=reg_no, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('portal:login')

        return render(request, self.template_name, {'form': form})




class LoginUser(View):
    template_name = 'portal/login_form.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        reg_no = request.POST['reg_no']
        password = request.POST['password']



        user = authenticate(reg_no=reg_no, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('portal:home')

        return render(request, self.template_name, {'form': form})
