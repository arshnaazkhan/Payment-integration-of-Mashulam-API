import email
from unittest import result
from django.shortcuts import render,HttpResponse,redirect
from urllib.request import urlopen,Request
from urllib import request
from .models import payment
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from pay.serializers import PaySerializer,thankSerializer
import requests
from django.forms.models import model_to_dict
# Create your views here.
def index(request):
    return render(request,'index.html')

# def pay(request):
#     userId='f0bba422d1aee126'
#     pageCode='88da9f8ccf4b'
#     successUrl='http://127.0.0.1:8000/thank/'
#     cancelUrl='https://www.meshulam.biz'
#     if request.method=="POST":
#         userid=request.POST.get('userid')
#         fullName=request.POST.get('fullName')
#         phone=request.POST.get('phone')
#         email=request.POST.get('email')                                                                                                       
#         sum=request.POST.get('sum')

       
#     # result = 
#     print(fullName)
#     print(phone)
#     print(email)
#     print(sum)
#     headers = {'Content-Type': 'application/json'}
#     request = requests.post(f"https://sandbox.meshulam.co.il/api/light/server/1.0/createPaymentProcess/?pageCode={pageCode}&userId={userId}&apiKey=&sum={sum}&successUrl={successUrl}&cancelUrl={cancelUrl}&description=&paymentNum=&maxPaymentNum=&companyCommission=&saveCardToken=&cField1=?apiKey=&description=&paymentNum=&maxPaymentNum=&pageField[fullName]={fullName}&pageField[phone]={phone}&pageField[email]={email}&companyCommission=&saveCardToken=&cField1=", headers=headers)
#     # response_body = urlopen(request).read()
#     response_body = request.text
    
#     print (response_body)
#     # return render (request,'index.html')
#     return HttpResponse(response_body)


@api_view(['POST'])
def pay(request, format=None):
    serializer = PaySerializer(data=request.data)
    data = request.data

    print("feeded data===========",data)
    print("_________________________________________")
    print("serializer data===============",serializer)
    print("_________________________________________")
    
    userid = data['userid']
    print("userid:",userid)
    fullName = data['fullName']
    print("FullName:",fullName)
    phone = data['phone']
    print("phone:",phone)
    email = data['email']
    print("email:",email)
    sum = data['sum']
    print("sum:",sum)
    

    userId='f0bba422d1aee126'
    pageCode='88da9f8ccf4b'
    successUrl='http://127.0.0.1:8000/thank/userid='+userid
    cancelUrl='https://www.meshulam.biz'
    headers = {'Content-Type': 'application/json'}
    request = requests.get(f"https://sandbox.meshulam.co.il/api/light/server/1.0/createPaymentProcess/?pageCode={pageCode}&userId={userId}&apiKey=&sum={sum}&successUrl={successUrl}&cancelUrl={cancelUrl}&description=&paymentNum=&maxPaymentNum=&companyCommission=&saveCardToken=&cField1=?apiKey=&description=&paymentNum=&maxPaymentNum=&pageField[fullName]={fullName}&pageField[phone]={phone}&pageField[email]={email}&companyCommission=&saveCardToken=&cField1=", headers=headers)
    print("Request==============",request)
    print("___________________________________")
    data1 = request.json()
    print(data1)    
    data2 = data1['data']
    print("data::::::::",data2)                                                                                                    
    print("___________________________________")
    
    processId = data2['processId']
    print("processId:",processId)
    processToken = data2['processToken']
    print("processToken:",processToken)
    url = data2['url']
    print("url:",url)    
   
    # if request.method == 'POST':
   
    if serializer.is_valid():
        serializer.save(fullName=fullName,phone=phone,email=email,sum=sum, pageCode=pageCode,processId=processId,processToken=processToken)
        
    return redirect(url)  
    




def thank(request,userid):
    pi = payment.objects.get(userid=userid)
    print("pi=========================",pi)
    pi_dict =  model_to_dict(pi)
    print("pi_dict===============",pi_dict)
    # pi_serialized = json.dumps(pi_dict)
    # print("Json data pi serialized=================",pi_serialized)
    processId = pi_dict['processId']
    print("processId:=====",processId)                        
    processToken = pi_dict['processToken']
    print("processId:=====",processToken)
    pageCode = '88da9f8ccf4b'
    
    headers = {
        'Content-Type': 'application/json'
    }
    request = requests.get(f'https://sandbox.meshulam.co.il/api/light/server/1.0/getPaymentProcessInfo/?pageCode={pageCode}&processId={processId}&processToken={processToken}', headers=headers)
    # response_body = urlopen(request).read()
    return HttpResponse(request)
    # data4 = payment.objects.all()
    # cust = {
    #     "customer_profile": data4
    # }
    # return render("success.html", cust)

#     context = {
#     'items': payment.objects.all(),
#     'title': 'Items'
# }
    #return render(request, 'success.html')



   