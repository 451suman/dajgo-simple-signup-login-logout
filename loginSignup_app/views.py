from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(View):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class DemoView(LoginRequiredMixin, View):
    template_name = 'demo.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    