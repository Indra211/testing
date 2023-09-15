
from django.contrib import admin
from django.urls import path
from Demo.views import DetialsList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details', DetialsList.as_view())

]
