from django.urls import path
from .views import task


urlpatterns = [
    path('task/', task.as_view(), name='task'),
]
