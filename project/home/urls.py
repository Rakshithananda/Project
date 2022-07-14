import django
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from home import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',auth_views.LoginView.as_view(template_name = 'home/home.html'),name='home'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'home/logout.html'),name='logout'),
    path('register/',views.register,name = 'register'),

    # Revenue District
    path('show_revenue_dist/',views.Show_Revenue_Dist,name = 'show-revenue-dist'),
    path('add_revenue_dist/',views.Add_Revenue_Dist,name = 'add-revenue-dist'),
    path('update_revenue_dist/<int:id>', views.Update_Revenue_Dist),  
    path('delete_revenue_dist/<int:id>', views.Delete_Revenue_Dist),

    # Revenue Mandal
    path('show_revenue_mandal/',views.Show_Revenue_Mandal,name = 'show-revenue-mandal'),
    path('add_revenue_mandal/',views.Add_Revenue_Mandal,name = 'add-revenue-mandal'),
    path('update_revenue_mandal/<int:id>', views.Update_Revenue_Mandal),  
    path('delete_revenue_mandal/<int:id>', views.Delete_Revenue_Mandal),

    # Revenue Village
    path('show_revenue_village/',views.Show_Revenue_Village,name = 'show-revenue-village'),
    path('add_revenue_village/',views.Add_Revenue_Village,name = 'add-revenue-village'),
    path('update_revenue_village/<int:id>', views.Update_Revenue_Village),  
    path('delete_revenue_village/<int:id>', views.Delete_Revenue_Village),
]