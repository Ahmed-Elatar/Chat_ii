from django.urls import path
from .views import *

urlpatterns = [
    
    path('', index ,name="index"),
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    path('signup/',user_signup,name="signup"),
    path('<int:id>/', post_detail, name='post_detail'),
    path('post/<int:id>/',post_comment,name="post_comment")
    

]
