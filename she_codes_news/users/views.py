from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from news.models import NewsStory, get_user_model

# Create your views here.

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class EditAccountView(LoginRequiredMixin,UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('login')
    template_name = 'users/editAccount.html'


# @login_required
# def profile_view(request,user_id):
#     print(request.user.id)
#     if request.user.id == user_id:
#         this_user=CustomUser.objects.get(pk=user_id)
#         return render(request, 'users/profile.html',context={'user':this_user})
#     else:
#         return redirect('news:index')


class UserProfileView(LoginRequiredMixin,generic.DetailView):
    # model = CustomUser
    model= get_user_model()
    template_name = 'users/profile.html'
    context_object_name = 'profile'

