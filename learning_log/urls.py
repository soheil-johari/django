
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('', include("learning_logs.urls")),
    
]
 
urlpatterns += staticfiles_urlpatterns()