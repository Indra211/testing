
from django.contrib import admin
from django.urls import path
from Demo.views import DetialsList,get_slots

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details', DetialsList.as_view()),
    path('slots',get_slots())
]
