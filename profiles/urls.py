from django.urls import path
from .views import (my_profile_view, 
invites_received_view, 
profiles_list_view,
invite_profiles_list_view, 
ProfileListView,
send_invitation,
remove_from_friends, 
accept_invatation, 
reject_invatation,
ProfileDetailView,)

app_name = 'profiles'   

urlpatterns=[
    path('',ProfileListView.as_view(),name='all-profiles-view'),
    path('myprofile/',my_profile_view,name='my-profile-view'),
    path('my-invites/',invites_received_view,name='my-invites-view'),
    path('allinvite-profiles/',invite_profiles_list_view,name='invite-profile-view'),
    path('send-invite/',send_invitation,name='send-invite'),
    path('remove-friend/',remove_from_friends,name='remove-friend'),
    path('<slug>/',ProfileDetailView.as_view(),name='profile-detail-view'),
    path('my-invites/accept-invatation/', accept_invatation,name='accept-invatation'),
    path('my-invites/reject-invatation/', reject_invatation, name='reject-invatation'),
]