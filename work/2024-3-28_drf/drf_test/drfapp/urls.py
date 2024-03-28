from django.urls import path
from drfapp import views

urlpatterns = [
    path("fn/list/",views.course_list),
    path("fn/detial/<int:pk>/",views.course_detial),
]
