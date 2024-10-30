
from app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('settings/', views.settings, name='settings'),
    path('tag/<str:tag_name>', views.tag, name='tag'),
    path('ask/', views.ask, name='ask'),
    path('question/<int:question_id>', views.question, name='question'),
]
