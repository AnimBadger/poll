
from django.contrib import admin
from django.urls import path,include

from poll import views as poll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('results/<poll_id>/', poll_views.results, name='results'),
    path('delete/<poll_id>/', poll_views.delete_con, name='con-delete'),
    path('users/',include('users.urls')),
    path('users/',include('django.contrib.auth.urls'))
    ]

