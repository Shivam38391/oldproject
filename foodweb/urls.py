"""foodweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings

from django.contrib import admin
from django.urls import path , include, re_path
from users import views as users_views

# built in views rember these are Class based Views   , we alread have views dont need to create , we need to create templates
from django.contrib.auth import views as authenticate_views

from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include("food.urls") ),
    path('register/', users_views.register, name='register'),
    path('login/' , authenticate_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/' , authenticate_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('profile/', users_views.profilepage , name='profile'), 
    
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += [
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)