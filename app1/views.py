from django.shortcuts import render,redirect
from .models import Customer,List,Rental
from django.contrib import messages

# Create your views here.
def add(request):
    # if request.method=='POST':
    #     name = request.POST.get('name')
    #     phone_no = request.POST.get('phone_no')
    #     email = request.POST.get('email')
    #     ab=Customer(customer_name=name,phone_no=phone_no,email=email)
    #     ab.save()
    return render(request, 'index.html')

def base(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        ab = Customer(customer_name=name, phone_no=phone_no, email=email)
        ab.save()
    return render(request,'base.html')

def inven(request):
    abc=List.objects.all()
    return render(request,'inventory.html',{'abc':abc})

def rental(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rental_date = request.POST.get('rental_date')
        return_date = request.POST.get('return_date')
        vehicle_name = request.POST.get('vehicle_name')
        abc = Rental(custom_name=name, rental_date=rental_date, return_date=return_date,vehicle_type=vehicle_name)
        abc.save()
    return render(request,'booking.html')

def invent(request,pk):
    try:
        obj=List.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return JsonResponse({"message":"Not found"})

def booked(request):
    ab = Rental.objects.all()
    return render(request,'booking_list.html',{'ab':ab})

def customer_list(request):
    abcd = Rental.objects.all()
    return render(request, 'customer_list.html',{'abcd':abcd})