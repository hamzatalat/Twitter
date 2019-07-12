from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('signup/', include('signup.urls')),
    path('admin/', admin.site.urls),
]
