from django.urls import path

from .views import *


urlpatterns = [
    path('v1/login', login, name='login'),
    path('v1/logout', Logout.as_view(), name='logout'),

    path('v1/registration', Registration.as_view(), name='registration'),
    path('v1/users_list', UserList.as_view(), name='users_list'),

    path('v1/groups_list', GroupsViewSet.as_view(), name='groups_list'),
    path('v1/news_list', NewsViewSet.as_view(), name='news_list'),
    path('v1/winners_list', LastWinnersViewSet.as_view(), name='winners_list'),
    path('v1/archive_list', ArchiveViewSet.as_view(), name='archive_list'),

    path('v1/command', CommandCreateViewSet.as_view(), name='create_command'),
    path('v1/command_list', CommandViewSet.as_view(), name='command_list'),

    path('v1/duel_list', DuelViewSet.as_view(), name='duel_list'),
    path('v1/add_duel', AddDuelViewSet.as_view(), name='add_duel'),
    path('v1/update_duel/<int:pk>/', UpdateDuelViewSet.as_view(), name='update_duel'),
    path('v1/delete_duel/<int:pk>/', DeleteDuelViewSet.as_view(), name='delete_duel'),
]
