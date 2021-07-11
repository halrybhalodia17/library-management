from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login),
    path('dashboard/',views.dashboard),
    path('add_stud',views.add_stud),
    path('add_book',views.add_book),
    path('remove_book',views.remove_book),
    path('search',views.search),
    path('issue_return',views.issue_return),
    path('return_book',views.return_book),
    path('return1/<email>',views.return1),
    path('error',views.error)
]