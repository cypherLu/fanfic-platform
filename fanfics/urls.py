from django.urls import path
from . import views

urlpatterns=[
    path('', views.kilig, name='kilig'),
    path('fanfic/<int:id>', views.fanficView, name='fanfic-view'),
    path('newfanfic/', views.newFanfic, name='new-fanfic'),
    path('edit/<int:id>', views.editfanfic, name='edit-fanfic'),
    path('delete/<int:id>', views.deletefanfic, name='delete-fanfic'),
    path('fanfic/<int:id>/newchapter/', views.newchapter, name='new-chapter'),
    path('fanfic/<int:fanfic_id>/chapter/<int:chapter_order>/', views.read_chapter, name='read-chapter'),
    path('like/<int:id>/', views.toggle_like, name='like'),
    path('bookmark/<int:id>/', views.toggle_bookmark, name='bookmark'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/<str:username>/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
]