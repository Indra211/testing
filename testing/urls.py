
from django.contrib import admin
from django.urls import path
from Demo.views import DetialsList,SlotsList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details', DetialsList.as_view()),
    path('slots',SlotsList.as_view())
]
