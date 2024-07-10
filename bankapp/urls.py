from django.urls import path
from .views import index,signup,signin,account_dashboard,logout,privacy_setting,dashboard_manu,home_page,calendar,horizontal_menu,horizontal_top_menu,two_sidebar,vertical_top_menu,transfer,transfer_options



urlpatterns = [
    path('', index, name='index'),
    path('account/register', signup, name='signup'),
    path('account/login', signin, name='signin'),
    path('logout', logout, name='logout'),
    path('account/login/dashboard', account_dashboard, name='account_dashboard'),
    path('account/login/setting', privacy_setting, name='privacy_setting'),
    path('account/login/setting/dashboard_manu', dashboard_manu, name='dashboard_manu'),
    path('account/login/dashboard/dashboard_manu', dashboard_manu, name='dashboard_manu'),
    path('account/login/home', home_page, name='home_page'),
    path('account/login/home/calendar', calendar, name='calendar'),
    path('account/login/home/horizontal_menu', horizontal_menu, name='horizontal_menu'),
    path('account/login/home/horizontal_top_menu', horizontal_top_menu, name='horizontal_top_menu'),
    path('account/login/home/two_sidebar', two_sidebar, name='two_sidebar'),
    path('account/login/home/vertical_top_menu', vertical_top_menu, name='vertical_top_menu'),
    path('account/login/dashboard/transfer', transfer, name='transfer'),
    path('account/login/dashboard/transfer/transfer_options', transfer_options, name='transfer_options'), 
    
]