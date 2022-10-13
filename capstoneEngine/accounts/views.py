from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib import messages

from .models import Profile
from .forms import UserProfileForm, UserForm


class SignUpView(SuccessMessageMixin, CreateView):
    model = Profile
    form_class = UserProfileForm
    user_form_class = UserForm
    template_name = "registration/signup.html"
    success_message = "Profile created successfully"
    success_url = reverse_lazy('login')

    def get(self, request):
        profile_form = self.form_class()
        user_form = self.user_form_class()
        return render(request, self.template_name, {'profile_form': profile_form, 'user_form': user_form})

    def post(self, request, *args, **kwargs):
        profile_form = self.form_class(request.POST)
        user_form = self.user_form_class(request.POST)
        if all([profile_form.is_valid(), user_form.is_valid()]):
            my_user = user_form.save()
            profile_form = self.form_class(request.POST, instance=Profile.objects.get(user=my_user))
            profile = profile_form.save(commit=False)
            profile.user = my_user
            profile.save()
            messages.success(request, self.success_message)
        else:
            return render(request, self.template_name, {'profile_form': profile_form, 'user_form': user_form})
        return HttpResponseRedirect(self.success_url)

def displayProfile(request):
    curruser = request.user.profile
    return render(request, 'userprofile.html', {'curruser': curruser,}) 
    
