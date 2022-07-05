from django.shortcuts import render
from django.views import generic

from django.urls import reverse_lazy
from .forms import SignUpForm,ProfilePageForm
from .models import Profile

from django.views.generic import CreateView

class UserRegisterView(generic.CreateView):

    form_class = SignUpForm
    template_name ='registration/register.html'
    success_url = reverse_lazy('login')

class CreateProfilePageView(CreateView):

    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

