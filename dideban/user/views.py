from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import LoginForm


class LoginView(TemplateView):
    template_name = 'user/login.html'

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            if not (user := authenticate(request, **form.cleaned_data)):
                return render(
                    request,
                    self.template_name,
                    {'errors': _("User not found")}
                )
            login(request, user)
            return redirect('profile')
        else:
            return render(request, self.template_name, {'errors': form.errors})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'
