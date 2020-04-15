from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('add/table/',views.table,name='table'),
    path('add/',views.add,name='add'),
    path('add/table/final_csv',views.final_csv,name='final_csv'),

]
