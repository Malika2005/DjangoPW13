from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.get_comments, name='get_comments'),
    path('comments/<int:comment_id>/', views.get_comment, name='get_comment'),
    path('comments/delete/<int:sms_id>/', views.delete_comment_by_sms_id, name='delete_comment_by_sms_id'),
]