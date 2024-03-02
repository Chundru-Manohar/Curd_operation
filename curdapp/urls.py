from . import views
from django.urls import path

urlpatterns = [
    path('',views.display),
    path('post/',views.post),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
    path('views/<int:id>/',views.viewss),
]
