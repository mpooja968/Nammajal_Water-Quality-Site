# frontend/urls.py

from django.urls import path
from . import views
from .views import forgot_password

#READ ALOUD
from .views import read_aloud


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signin/', views.signin, name='signin'),
    path('ngo-interface/', views.ngo_interface, name='ngo_interface'),
    path('create-account/', views.create_account, name='create_account'),
    path('ngo-interface/', views.signin, name='ngo_interface'),  # Redirect to signin
    path('public-interface/', views.user_interface, name='user_interface'),  # Public Interface view
    #path('test-email/', test_email, name='test_email'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<str:token>/', views.reset_password, name='reset_password'),
    path('logout/', views.user_logout, name='user_logout'),
    path('insights/', views.insights_view, name='insights'),
    #path('search/', views.search_lake, name='search_lake'),
    
    #path('welcome/', views.welcome, name='welcome'),
    path('user-interface/', views.user_interface, name='user_interface'),
    path('insights1/', views.user_interface1, name='insights1'),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path('contact/', views.submit_contact1, name='submit_contact1'),
    path('contact/', views.submit_contact, name='submit_contact'),
    path('search_lake/', views.search_lake, name='search_lake'),
    path('lakes_nearby/', views.lakes_nearby, name='lakes_nearby'),
    

#read aloud
   path('read-aloud/', views.read_aloud, name='read_aloud'),   
]
