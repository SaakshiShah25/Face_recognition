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
    path('add/table/counter',views.counter,name='counter'),
    path('add/table/manage',views.manage,name='manage'),
    path('add/table/remove_data',views.remove_data,name='remove_data'),
    path('add/table/manual',views.manual,name='manual'),
    path('add/table/update',views.update,name='update'),
    path('add/table/dict_update',views.dict_update,name='dict_update'),
    #path('add/table/final_csv',views.final_csv,name='final_csv'),

]
