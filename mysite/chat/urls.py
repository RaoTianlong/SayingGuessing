from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register, name='register'),
    path("<str:room_name>/", views.room, name="room"), # 按顺序匹配，通配符得最后
]