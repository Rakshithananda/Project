import imp
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,RevenueDistrictForm,RevenueMandalForm,RevenueVillageForm
from .models import Revenue_District,Revenue_Mandal,Revenue_Village
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
def Add_Revenue_Dist(request):
    if request.method == 'POST':
        form = RevenueDistrictForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, f'Your Data is Succesfully added!')
            return redirect('show-revenue-dist')
    else:
        form = RevenueDistrictForm()
    return render(request,'home/add_table.html',{'form':form})

@login_required
def Show_Revenue_Dist(request):
    districts = Revenue_District.objects.all()
    return render(request,'home/show_revenue_dist.html',{'districts':districts})

@login_required
def Update_Revenue_Dist(request,id):
    district = Revenue_District.objects.get(id = id)
    if request.method == 'POST':
        form = RevenueDistrictForm(request.POST, instance = district)
        if form.is_valid():     
            form.save()
            messages.success(request, f'Data Updated Succesfully !')  
            return redirect('show-revenue-dist')
    else:
        form = RevenueDistrictForm(instance = district)
    return render(request, 'home/edit_table.html', {'form':form})

@login_required
def Delete_Revenue_Dist(request, id):  
    district = Revenue_District.objects.get(id = id)  
    district.delete()  
    return redirect('show-revenue-dist')



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
    mandal = Revenue_Mandal.objects.get(id = id)
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
    mandal = Revenue_Mandal.objects.get(id = id)  
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
    village = Revenue_Village.objects.get(id = id)
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
    village = Revenue_Village.objects.get(id = id)  
    village.delete()  
    return redirect('show-revenue-village')

