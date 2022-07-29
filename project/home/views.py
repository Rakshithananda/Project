from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import (UserRegisterForm,
                    RevenueDistrictForm,
                    RevenueMandalForm,
                    RevenueVillageForm,
                    RevenueGSWSForm,
                    RevenueVROForm,
                    RegisterDistrictForm,
                    RegisterSROForm,
                    RegisterVillageForm)
from .models import (Revenue_District,
                    Revenue_Mandal, Revenue_VRO,
                    Revenue_Village,
                    Revenue_GSWS,
                    Revenue_VRO,
                    Register_District,
                    Register_SRO,
                    Register_Village)
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You arer ready to Log in')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request,'home/register.html',{'form':form})

#-------------------------------------------------------------------------------------
# Revenue District Table Contents
@login_required
def Add_Revenue_District(request):
    if request.method == 'POST':
        form = RevenueDistrictForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Data is Succesfully added!')
            return redirect('show-revenue-district')
    else:
        form = RevenueDistrictForm()
    return render(request,'home/add_table.html',{'form':form})

@login_required
def Show_Revenue_District(request):
    districts = Revenue_District.objects.all()
    return render(request,'home/show_revenue_district.html',{'districts':districts})

@login_required
def Update_Revenue_District(request,id):
    district = Revenue_District.objects.get(district_code = id)
    if request.method == 'POST':
        form = RevenueDistrictForm(request.POST, instance = district)
        if form.is_valid():     
            form.save()
            messages.success(request, f'Data Updated Succesfully !')  
            return redirect('show-revenue-district')
    else:
        form = RevenueDistrictForm(instance = district)
    return render(request, 'home/edit_table.html', {'form':form})

@login_required
def Delete_Revenue_District(request, id):  
    district = Revenue_District.objects.get(district_code = id)  
    district.delete()  
    return redirect('show-revenue-district')



#-------------------------------------------------------------------------------------
# Revenue Mandal Table Contents
@login_required
def Add_Revenue_Mandal(request):
    if request.method == 'POST':
        form = RevenueMandalForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, f'Your Data is Succesfully added!')
            return redirect('show-revenue-mandal')
    else:
        form = RevenueMandalForm()
    return render(request,'home/add_table.html',{'form':form})

@login_required
def Show_Revenue_Mandal(request):
    mandals = Revenue_Mandal.objects.all()
    return render(request,'home/show_revenue_mandal.html',{'mandals':mandals})

@login_required
def Update_Revenue_Mandal(request,id):
    mandal = Revenue_Mandal.objects.get(mandal_id = id)
    if request.method == 'POST':
        form = RevenueMandalForm(request.POST, instance = mandal)
        if form.is_valid():     
            form.save()
            messages.success(request, f'Data Updated Succesfully !')  
            return redirect('show-revenue-mandal')
    else:
        form = RevenueMandalForm(instance = mandal)
    return render(request, 'home/edit_table.html', {'form':form})

@login_required
def Delete_Revenue_Mandal(request, id):  
    mandal = Revenue_Mandal.objects.get(mandal_id = id)  
    mandal.delete()  
    return redirect('show-revenue-mandal')


#-------------------------------------------------------------------------------------
# Revenue Village Table Contents
@login_required
def Add_Revenue_Village(request):
    if request.method == 'POST':
        form = RevenueVillageForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, f'Your Data is Succesfully added!')
            return redirect('show-revenue-village')
    else:
        form = RevenueVillageForm()
    return render(request,'home/add_table.html',{'form':form})

@login_required
def Show_Revenue_Village(request):
    villages = Revenue_Village.objects.all()
    return render(request,'home/show_revenue_village.html',{'villages':villages})

@login_required
def Update_Revenue_Village(request,id):
    village = Revenue_Village.objects.get(village_id = id)
    if request.method == 'POST':
        form = RevenueVillageForm(request.POST, instance = village)
        if form.is_valid():     
            form.save()
            messages.success(request, f'Data Updated Succesfully !')  
            return redirect('show-revenue-village')
    else:
        form = RevenueVillageForm(instance = village)
    return render(request, 'home/edit_table.html', {'form':form})

@login_required
def Delete_Revenue_Village(request, id):  
    village = Revenue_Village.objects.get(village_id = id)  
    village.delete()  
    return redirect('show-revenue-village')


#-------------------------------------------------------------------------------------
# Revenue GSWS Table Contents
@login_required
def Add_Revenue_GSWS(request):
    if request.method == 'POST':
        form = RevenueGSWSForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, f'Your Data is Succesfully added!')
            return redirect('show-revenue-gsws')
    else:
        form = RevenueGSWSForm()
    return render(request,'home/add_table.html',{'form':form})

@login_required
def Show_Revenue_GSWS(request):
    gswss = Revenue_GSWS.objects.all()
    return render(request,'home/show_revenue_gsws.html',{'gswss':gswss})

@login_required
def Update_Revenue_GSWS(request,id):
    gsws = Revenue_GSWS.objects.get(gsws_id = id)
    if request.method == 'POST':
        form = RevenueGSWSForm(request.POST, instance = gsws)
        if form.is_valid():     
            form.save()
            messages.success(request, f'Data Updated Succesfully !')  
            return redirect('show-revenue-gsws')
    else:
        form = RevenueGSWSForm(instance = gsws)
    return render(request, 'home/edit_table.html', {'form':form})

@login_required
def Delete_Revenue_GSWS(request, id):  
    gsws = Revenue_GSWS.objects.get(gsws_id = id)  
    gsws.delete()  
    return redirect('show-revenue-gsws')



#-------------------------------------------------------------------------------------
# Revenue VRO Table Contents
@login_required
def Add_Revenue_VRO(request):
    if request.method == 'POST':
        form = RevenueVROForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, f'Your Data is Succesfully added!')
            return redirect('show-revenue-vro')
    else:
        form = RevenueVROForm()
    return render(request,'home/add_table.html',{'form':form})

@login_required
def Show_Revenue_VRO(request):
    vros = Revenue_VRO.objects.all()
    return render(request,'home/show_revenue_vro.html',{'vros':vros})

@login_required
def Update_Revenue_VRO(request,id):
    vro = Revenue_VRO.objects.get(vro_entry = id)
    if request.method == 'POST':
        form = RevenueVROForm(request.POST, instance = vro)
        if form.is_valid():     
            form.save()
            messages.success(request, f'Data Updated Succesfully !')  
            return redirect('show-revenue-vro')
    else:
        form = RevenueVROForm(instance = vro)
    return render(request, 'home/edit_table.html', {'form':form})

@login_required
def Delete_Revenue_VRO(request, id):  
    vro = Revenue_VRO.objects.get(vro_entry = id)  
    vro.delete()  
    return redirect('show-revenue-vro')



















#-------------------------------------------------------------------------------------
# Register District Table Contents
@login_required
def Add_Register_District(request):
    if request.method == 'POST':
        form = RegisterDistrictForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, f'Your Data is Succesfully added!')
            return redirect('show-register-district')
    else:
        form = RegisterDistrictForm()
    return render(request,'home/add_table.html',{'form':form})

@login_required
def Show_Register_District(request):
    districts = Register_District.objects.all()
    return render(request,'home/show_register_district.html',{'districts':districts})

@login_required
def Update_Register_District(request,id):
    district = Register_District.objects.get(district_code = id)
    if request.method == 'POST':
        form = RegisterDistrictForm(request.POST, instance = district)
        if form.is_valid():     
            form.save()
            messages.success(request, f'Data Updated Succesfully !')  
            return redirect('show-register-district')
    else:
        form = RegisterDistrictForm(instance = district)
    return render(request, 'home/edit_table.html', {'form':form})

@login_required
def Delete_Register_District(request, id):  
    district = Register_District.objects.get(district_code = id)  
    district.delete()  
    return redirect('show-register-district')


# Register SRO Table Contents
@login_required
def Add_Register_SRO(request):
    if request.method == 'POST':
        form = RegisterSROForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, f'Your Data is Succesfully added!')
            return redirect('show-register-sro')
    else:
        form = RegisterSROForm()
    return render(request,'home/add_table.html',{'form':form})

@login_required
def Show_Register_SRO(request):
    sros = Register_SRO.objects.all()
    return render(request,'home/show_register_sro.html',{'sros':sros})

@login_required
def Update_Register_SRO(request,id):
    sro = Register_SRO.objects.get(sro_id = id)
    if request.method == 'POST':
        form = RegisterSROForm(request.POST, instance = sro)
        if form.is_valid():     
            form.save()
            messages.success(request, f'Data Updated Succesfully !')  
            return redirect('show-register-sro')
    else:
        form = RegisterSROForm(instance = sro)
    return render(request, 'home/edit_table.html', {'form':form})

@login_required
def Delete_Register_SRO(request, id):  
    sro = Register_SRO.objects.get(sro_id = id)  
    sro.delete()  
    return redirect('show-register-sro')


# Register Village Table Contents
@login_required
def Add_Register_Village(request):
    if request.method == 'POST':
        form = RegisterVillageForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, f'Your Data is Succesfully added!')
            return redirect('show-register-village')
    else:
        form = RegisterVillageForm()
    return render(request,'home/add_table.html',{'form':form})

@login_required
def Show_Register_Village(request):
    villages = Register_Village.objects.all()
    return render(request,'home/show_register_village.html',{'villages':villages})

@login_required
def Update_Register_Village(request,id):
    village = Register_Village.objects.get(village_id = id)
    if request.method == 'POST':
        form = RegisterVillageForm(request.POST, instance = village)
        if form.is_valid():     
            form.save()
            messages.success(request, f'Data Updated Succesfully !')  
            return redirect('show-register-village')
    else:
        form = RegisterVillageForm(instance = village)
    return render(request, 'home/edit_table.html', {'form':form})

@login_required
def Delete_Register_Village(request, id):  
    village = Register_Village.objects.get(village_id = id)  
    village.delete()  
    return redirect('show-register-village')