from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib.auth.models import User, Group
from .forms import *
from .models import *
from .serializers import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


















def post_detail(request, id):
    post = get_object_or_404(Post,id=id)
    print(id)
    
    return render(request,'details.html',{'post': post})






def index(request):

    # if not request.user.is_authenticated :
    #     return redirect('login')

    


    
    # paginator= paginator(posts,2)
    # page_number = request.GET.get('page', 1)
    # pp=paginator.page(page_number)



    post_list = Post.objects.all()    
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        
        posts = paginator.page(1)
    except EmptyPage:
        
        posts = paginator.page(paginator.num_pages)






    return render(request,"list.html",{"posts":posts},status=200)


















####################################################################################################
##################                  Authentication

#sign-up 
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



# login
def user_login(request):
    if request.user.is_authenticated:
        return redirect ('logout')
    if request.method == 'POST':
        

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
