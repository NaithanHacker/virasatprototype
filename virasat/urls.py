"""
URL configuration for virasat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from info import views as i_f
from accounts import views as a_c
from dashboard import views as d_v
from home import views as h_v
from explore import views as e_v
from sell import views as s_v

urlpatterns = [
    path('', i_f.info_view, name='info'),
    path('register/', a_c.register, name='register'),
    path('login/', a_c.login, name='login'),
    path('dashboard/', d_v.dashboard_view, name='dashboard'),
    path('home/', h_v.home_view, name='home'),
    path('explore/', e_v.explore, name='explore'),
    path('artadd/', e_v.art_add, name='explore_add'),

    path('artsell/', s_v.art_add,name='artsell'),
    path('sell/', s_v.sell,name='sell'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)