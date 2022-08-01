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
    path('show_revenue_district/',views.Show_Revenue_District,name = 'show-revenue-district'),
    path('add_revenue_district/',views.Add_Revenue_District,name = 'add-revenue-district'),
    path('update_revenue_district/<int:id>', views.Update_Revenue_District),  
    path('delete_revenue_district/<int:id>', views.Delete_Revenue_District),

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

    # Revenue GSWS
    path('show_revenue_gsws/',views.Show_Revenue_GSWS,name = 'show-revenue-gsws'),
    path('add_revenue_gsws/',views.Add_Revenue_GSWS,name = 'add-revenue-gsws'),
    path('update_revenue_gsws/<int:id>', views.Update_Revenue_GSWS),  
    path('delete_revenue_gsws/<int:id>', views.Delete_Revenue_GSWS),

    # Revenue VRO
    path('show_revenue_vro/',views.Show_Revenue_VRO,name = 'show-revenue-vro'),
    path('add_revenue_vro/',views.Add_Revenue_VRO,name = 'add-revenue-vro'),
    path('update_revenue_vro/<int:id>', views.Update_Revenue_VRO),  
    path('delete_revenue_vro/<int:id>', views.Delete_Revenue_VRO),

    # Revenue VRO Details
    path('show_revenue_vro_details/',views.Show_Revenue_VRO_Details,name = 'show-revenue-vro-details'),
    path('add_revenue_vro_details/',views.Add_Revenue_VRO_Details,name = 'add-revenue-vro-details'),
    path('update_revenue_vro_details/<int:id>', views.Update_Revenue_VRO_Details),  
    path('delete_revenue_vro_details/<int:id>', views.Delete_Revenue_VRO_Details),

    # Revenue Claiment
    path('show_revenue_claiment/',views.Show_Revenue_Claiment,name = 'show-revenue-claiment'),
    path('add_revenue_claiment/',views.Add_Revenue_Claiment,name = 'add-revenue-claiment'),
    path('update_revenue_claiment/<int:id>', views.Update_Revenue_Claiment),  
    path('delete_revenue_claiment/<int:id>', views.Delete_Revenue_Claiment),

    # Schedule Entry
    path('show_schedule_entry/',views.Show_Schedule_Entry,name = 'show-schedule-entry'),
    path('add_schedule_entry/',views.Add_Schedule_Entry,name = 'add-schedule-entry'),
    path('update_schedule_entry/<int:id>', views.Update_Schedule_Entry),  
    path('delete_schedule_entry/<int:id>', views.Delete_Schedule_Entry),
    
    
    
    #----------------------------------------------------------------------------------------------
    # Register District
    path('show_register_district/',views.Show_Register_District,name = 'show-register-district'),
    path('add_register_district/',views.Add_Register_District,name = 'add-register-district'),
    path('update_register_district/<int:id>', views.Update_Register_District),  
    path('delete_register_district/<int:id>', views.Delete_Register_District),

    # Register SRO
    path('show_register_sro/',views.Show_Register_SRO,name = 'show-register-sro'),
    path('add_register_sro/',views.Add_Register_SRO,name = 'add-register-sro'),
    path('update_register_sro/<int:id>', views.Update_Register_SRO),  
    path('delete_register_sro/<int:id>', views.Delete_Register_SRO),

    # Register Village
    path('show_register_village/',views.Show_Register_Village,name = 'show-register-village'),
    path('add_register_village/',views.Add_Register_Village,name = 'add-register-village'),
    path('update_register_village/<int:id>', views.Update_Register_Village),  
    path('delete_register_village/<int:id>', views.Delete_Register_Village),
]