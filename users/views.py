from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm

from django.contrib.auth.decorators import login_required
# Create your views here.


# def register(request):
#     # when u submit the data , request method is going to be post, hence this code is executed
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():  # this valid take care of unique users
#             form.save() # to save the user 
            
#             username = form.cleaned_data.get('username')
#             messages.success(request,f'Welcome {username}, your account is created')
#             return redirect('food:index')
        
#     else:  
#     # when request is not going to post and we get the form on our webpage
#         form = UserCreationForm() 
#     return render(request, 'users/register.html', {'form': form})


def register(request):
    # when u submit the data , request method is going to be post, hence this code is executed
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():  # this valid take care of unique users
            form.save() # to save the user 
            
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('food:index')
        
    else:  
    # when request is not going to post and we get the form on our webpage
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})



@login_required # when u want to restricted a url without login
def profilepage(request):
    return render(request, 'users/profile.html')