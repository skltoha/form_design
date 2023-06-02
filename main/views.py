from django.shortcuts import render, redirect
from . import models
from . models import userDetails
from django.db import IntegrityError
# Create your views here.



def userHome(request):
    return render(request, 'index.html')


def userform(request):
    return render(request, 'Entryform.html')


def userStore(request):
    if request.method=='POST':
        userID = request.POST.get('user_id')
        userPhone = request.POST.get('user_phone')
        if len(userPhone) != 11:
            return redirect('user-form')
        
        if userDetails.objects.filter(user_id=userID).exists():
            my_value = "Duplicate value found"
            return render(request, 'index.html', {'my_value': my_value})
        else:
            userID = request.POST.get('user_id')
            userName = request.POST.get('user_name')
            userAdd = request.POST.get('user_address')
            userEmail = request.POST.get('user_email')
            userPhone = request.POST.get('user_phone')
            
            # store   = models.userDetails()
            # store.user_id=userID
            # store.user_name=userName
            # store.user_address=userAdd
            # store.user_email=userEmail
            # store.user_phone=userPhone
            
            # store.save()
            userDetails.objects.create(user_id=userID, user_name=userName, user_address=userAdd, user_email=userEmail, user_phone=userPhone)
            my_value = "sussesfuly added value."
            return render(request, 'index.html', {'my_value': my_value})


def userRecord(request):
    data = userDetails.objects.all()
    return render(request, 'record.html', {'data': data})



# def userStore(request):
#     try:   
#         if request.method=='POST':
#             userID = request.POST.get('user_id')
#             if userDetails.objects.filter(user_id=userID).exists():
#                 my_value = "Duplicate value added"
#                 return render(request, 'index.html', {'my_value': my_value})
#             else:
#                 userID = request.POST.get('user_id')
#                 userName = request.POST.get('user_name')
#                 userAdd = request.POST.get('user_address')
#                 userEmail = request.POST.get('user_email')
#                 userPhone = request.POST.get('user_phone')
                
#                 store   = models.userDetails()
#                 store.user_id=userID
#                 store.user_name=userName
#                 store.user_address=userAdd
#                 store.user_email=userEmail
#                 store.user_phone=userPhone
                
#                 store.save()
#             # models.userInfo.objects.create(userID=user_ID)
#                 my_value = "sussesfuly added value."
#                 return render(request, 'index.html', {'my_value': my_value})
#     except IntegrityError:
#         my_value = "Duplicate value found"
#         return render(request, 'index.html', {'my_value': my_value})