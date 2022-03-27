from django.core.mail import EmailMessage
import os
from random import randint
from django import forms
from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime
from floral.models import customer,flower,Service,Order
from django.core.mail import send_mail
from django.http import HttpResponse
import hashlib
from easy_pdf.rendering import render_to_pdf


def greet(request):
 dt=datetime.datetime.now()
 name="Chetan"
 subjects=["PYT","CN","ATC"]
 return render(request,"dt.html",{"dt":dt,"name":name,"subjects":subjects})

def orderdetails(request):
 uname=request.COOKIES.get('usname')
 c=customer.objects.get(cust_name=uname)
 onos=request.GET.get('fid')
 orderd=Order.objects.filter(customer_id=c)
 istr='''
 <title>ORDER DETAILS </title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
 <script>
 function ord(ono) {
   $.get("http://localhost:8000/orderdetails", {ono:id}).done(function(data) 
   {
      alert(data);
      $("body").html(data)
   });
  }
  </script>
  <body class="bg-img background-image:url({% static 'img\bgtable.jpg' %});">
        <div class="name ">
            <h1>ORDER DETAILS :</h1>
        </div>
        <div class="button">

            <a href="http://localhost:8000/index/">
                <button style="
    margin-top: 20px;
    margin-left: 160px;"class="btn">BACK</button>
            </a>

        </div>
  <style>
@import url(https://fonts.googleapis.com/css?family=Roboto:300);
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: sans-serif;
}

.bg-img {
    background-image: url('/static/img/bgtable.jpg');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
}

.name {
    margin-top: 20px;
    background-color: rgba(0, 0, 0, 0.384);
    width: 450px;
    border-radius: 50px;
    margin-left: 550px;
}

.name h1 {
    font-family: "Roboto", sans-serif;
    font-size: 40px;
    text-align: center;
}

.button {
    position: relative;
    margin-bottom: 20px;
    margin-left: 480px;
}

.button button {
    font-family: "Roboto", sans-serif;
    font-size: 30px;
    font-weight: bolder;
    padding: 5px;
    width: 250px;
    height: 60px;
    margin-right: 30px;
    border-radius: 46px;
    color: black;
    background: #e5dcdc;
    box-shadow: inset 9px 9px 18px #d3caca, inset -9px -9px 18px #f7eeee;
    border: 0;
}

.button button:hover {
    background: #838380;
    background-image: -webkit-linear-gradient(top, #111111, #2b2a28);
    background-image: -moz-linear-gradient(top, #1d1d1c, #141413);
    background-image: -ms-linear-gradient(top, #3a3a38, #2b2b2b);
    background-image: -o-linear-gradient(top, #0c0c0b, #252524);
    background-image: linear-gradient(to bottom, #201f1f, #1f1e1d);
    color: rgb(255, 255, 255);
    border: 0;
    opacity: 1;
    font-size: 32px;
    padding: 10px 80px 10px 80px;
    text-decoration: bold;
}

.button button2 {
    margin-left: 700px;
    font-family: "Roboto", sans-serif;
    font-size: 30px;
    font-weight: bolder;
    padding: 5px;
    width: 250px;
    height: 60px;
    border-radius: 46px;
    color: black;
    background: #e5dcdc;
    box-shadow: inset 9px 9px 18px #d3caca, inset -9px -9px 18px #f7eeee;
    border: 0;
}

table {
    font-family: "Roboto", sans-serif;
    border-collapse: collapse;
    width: 1500px;
    margin-top: 30px;
    margin-bottom: 50px;
    margin-left: auto;
    margin-right: auto;
    table-layout: fixed;
    align-items: center;
    border-bottom: 0px solid #dddddd;
}

td,
th {
    border-bottom: 2px solid #dddddd;
    border-right: 2px solid #dddddd;
}

th {
    font-family: "Roboto", sans-serif;
    font-size: 25px;
    background-color: rgba(0, 0, 0, 0.596);
    text-align: center;
    padding: 10px;
    height: 50px;
    color: blanchedalmond;
}

td {
    text-align: center;
    font-weight:bold;
    font-size:20px;
    background-color: rgba(145, 140, 140, 0.24);
    height: 95px;
    width: 100%;
}

  </style>
  <table class="emp ">
    <tr>
      <th style="width:15% ">ID</th>
      <th>FLOWER_ID</th>
      <th>CUSTOMER</th>
      <th>DATE</th>
      <th>QUANTITY</th>
      <th>TOTAL PRICE</th>
    </tr>

 ''' 
 cnt=1 
 for ord in orderd:
  istr+="<tr><td>"+str(ord.id)+"</td><td>"+str(ord.flower_id)+"</td><td>"+str(ord.customer_id)+"</td><td>"+str(ord.Date)+"</td><td>"+str(ord.quantity)+"</td><td>"+str(ord.total)+"</td></tr>";
 return HttpResponse(istr)
    


def login(request):
 return render(request,'login.html',{})

def customerlogin(request):
 return render(request,'customerlogin.html')


def ucustomerlogin(request):
  uname=request.GET.get('usname')
  pwd=request.GET.get('pswd')
  print('innn')
  pwd=hashlib.md5(pwd.encode('utf-8')).hexdigest()
  print(uname,pwd)
  u=customer.objects.filter(cust_name=uname,password=pwd)
  if(u):
   print('Successfully logged in')
   response=render(request,'index.html')
   response.set_cookie('usname',uname)
   return response
  else:
    return render(request,'customerlogin.html')


def customersignin(request):
 return render(request,'customersignin.html')


def ucustomersignin(request):
    uname=request.GET.get('usrname')
    pwd=request.GET.get('psw')
    pwd=hashlib.md5(pwd.encode('utf-8')).hexdigest()
    address=request.GET.get('address')
    emails=request.GET.get('email')
    print(emails)
    Phone=request.GET.get('Phone')
    print(uname,pwd,address,emails,Phone)
    
    u=customer.objects.filter(email=emails)
    if u:
        return HttpResponse("duplicate entry")

    b=customer.objects.filter(cust_name=uname)
    if b:
        return HttpResponse("Username Already Exists")
    
    s=customer(cust_name=uname,password=pwd,address=address,email=emails,phone_no=Phone)
    s.save()
    u=customer.objects.get(email=emails)
    res = send_mail("Regsitration", "Congratulations!. Your registration is successfull and your customer id is "+str(u.customer_id), "djangodemo555@gmail.com", [emails])
    return render(request,'customerlogin.html')

def index(request):
 return render(request,'index.html',{})



def products(request):
 return render(request,'products.html',{})

def uproducts(request):
    pro_list=flower.objects.all()
    
    istr='''
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script>
    function pro(fid)
  {
     quantity=$("#quantity"+fid).val()
     alert('You have ordered '+quantity+' of flowers whose flower id is '+fid)
     $.get("http://localhost:8000/uorder/", {fid:fid,quantity:quantity}).done(function(data)
    {
      alert(data);
    });
  }
</script>
<header>
        <h1>FLOWER PRODUCTS IN STOCK</h1>
        <h5>want to avail our services ?</h5>
        <a href="http://localhost:8000/services">
            <button class="btn">SERVICES</button>
        </a>
 </header>
 '''
    cnt=1
    for fl in pro_list:
      
      istr+='''
  
        <div class="card" id="cd" style="height: 420px;">
          <img src="http://localhost:8000/static/img/'''+str(cnt)+'''.jpg" alt="Sandwich" class="bg-img" width="100%">
            <div class="content">
                <h4>'''+fl.flower_name+'''</h4>
                <p>Price of each flower =<span style="color: red; font-weight: bold;">'''+str(fl.price)+''' </span></p>
                <input id='''+"quantity"+str(fl.flower_id)+''' type="integer" placeholder="Quantity">
                <button onclick=pro('''+str(fl.flower_id)+''') type="submit">BUY</button>
</div>
        </div>
    
            '''
      cnt+=1
      #if cnt%5==0:
       # istr+='''''</div><div class="grid-row" style="display: grid; grid-gap: 20px;">'''''
    return HttpResponse(istr)


def uorder(request): 
  uname=request.COOKIES.get('usname')
  print(uname)
  onos=request.GET.get('fid')
  f=flower.objects.get(flower_id=onos)
  quantity=request.GET.get('quantity')
  c=customer.objects.get(cust_name=uname)
  f=flower.objects.get(flower_id=onos)
  p=f.price   
  int(p)
  total=0
  for i in range(int (quantity)):
   total=total+p
  print(total)
  o=Order(flower_id=f,customer_id=c,quantity=quantity,Date=datetime.date.today(),total=total)
  
  #f.first().order.add(c.first())
  o.save() 
  print(f)
  print(quantity)

   
  c=customer.objects.get(cust_name=uname)
  email=c.email
  f=flower.objects.get(flower_id=onos)
  p=f.price   
  int(p)
  total=0
  for i in range(int (quantity)):
   total=total+p
  print(total)
  fname=f.flower_name
  template = 'orderdetail.html'
  print(onos,fname,uname)
  context = {'ono' : onos,'flower_name':fname,'customer_name':uname,'Total':total}
  pdf = render_to_pdf(template, context)
  email = EmailMessage("order","Flower_Ordered","sjjo2411@gmail.com",[email])
  email.content_subtype = "pdf"
  email.attach('Flower_Ordered', pdf, 'application/pdf')
  res = email.send()
  return HttpResponse("done")
  
def services(request):
 return render(request,'services.html',{})

def uservices(request):
    ser_list=Service.objects.all()
    print(ser_list)
    istr='''
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
      <script>
      function ser(sid)
    {
       $.get("http://localhost:8000/uorders/", {sid:sid}).done(function(data)
     {
      alert(data);
     });
 }
</script>
<header>
        <h1>SERVICES AVAILABLE</h1>
        <h5>want to buy our products?</h5>
        <a href="http://localhost:8000/products">
            <button class="btn">PRODUCTS</button>
        </a>
 </header>
 '''
    cnt=1
    for se in ser_list:
      
      istr+='''
  
        <div class="cards">

            <img src="http://localhost:8000/static/img/s/'''+str(cnt)+'''.jpg" alt="Sandwich" class="bg-img" width="100%">
            <div class="content">
                <h4>'''+se.name_of_service+'''</h4>
                <p>Price of each flower =<span style="color: red; font-weight: bold;">'''+str(se.price)+''' </span></p>

                <button onclick=ser('''+str(se.purpose_id)+''') type="submit">BUY</button>
               
            </div>
        </div>
 
            '''
      cnt+=1
      #if cnt%5==0:
        #istr+='''''</div><div class="grid-row" style="display: grid; grid-gap: 20px;">'''''
    return HttpResponse(istr)
  
def uorders(request):
  uname=request.COOKIES.get('usname')
  print(uname)
  onos=request.GET.get('sid')
  s=Service.objects.filter(purpose_id=onos)
  c=customer.objects.filter(cust_name=uname)
  c.first().looksafter.add(s.first())
  c=customer.objects.get(cust_name=uname)

  email=c.email
  s=Service.objects.get(purpose_id=onos)
  fname=s.name_of_service
  template = 'ord.html'
  print(onos,fname,uname)
  context = {'ono' : onos,'service_name':fname,'customer_name':uname}
  pdf = render_to_pdf(template, context)
  email = EmailMessage("order","Flower_Ordered","sjjo2411@gmail.com",[email])
  email.content_subtype = "pdf"
  email.attach('Flower_Ordered', pdf, 'application/pdf')
  res = email.send()
  return HttpResponse("done")
  return HttpResponse("done")
 
def sendSimpleEmail(request):
   res = send_mail("hi", "Hope you are doing fine", "sjjo2411@gmail.com", ["sjjodha2482000@gmail.com"])
   return HttpResponse('%s'%res)




#Get OTP
def getotp(request):
    otp = randint(000000,999999) 
    email=request.GET.get('email') 
    file_exists = os.path.exists('enm.txt')
    ss=''
    if file_exists:
        f = open("enm.txt", "r")
        for fh in f:
            s=fh.split(":")
            em=s[0]
            if em==email:
                continue
            s+=fh
        f.close()        
    f = open("enm.txt", "w")
    ss+=email+":"+str(otp)
    f.write(ss)
    f.close()
    send_mail("OTP", "Your OTP is"+str(otp),"sjjo2411@gmail.com", [email])
    return HttpResponse('Mail sent')

def cpass(request):
    return render(request,"cpass.html")
    
def changepass(request):
    email=request.GET.get('email') 
    rotp=request.GET.get('rotp') 
    npsw=request.GET.get('npsw') 
    f = open("enm.txt", "r")
    for fh in f:
        s=fh.split(":")
        em=s[0]
        otp=s[1]
        if em==email and otp==rotp :
                c=customer.objects.get(email=email)
                npsw=hashlib.md5(npsw.encode('utf-8')).hexdigest()
                c.password=npsw
                c.save()
 
                return render(request,"customerlogin.html")
    return HttpResponse("OTP invalid")

def msearch(request):
    productnames=request.GET.get("productname")
    productlist=flower.objects.filter(flower_name__icontains=productnames)
    istr='''
    <br><br>
    <h2 class="tit">Flower Available:<h2/> 
    
     <style>
     
     



</style>
  
<table class="table">
            
                <tr class="w3-blue">
                    <th class="i">Flower Name</th>
                    <th class="i">Available colours</th>
                     <th class="i">Price per flower</th>
                    </tr>
                    

''' 
    for product in productlist:
     istr+="<tr><td>"+product.flower_name+"</td><td>"+product.color+"</td><td>"+str(product.price)+"<tr><td>";
    return HttpResponse(istr)

def search(request):
  return render(request,'search.html')

def usearch(request):
    productnames=request.GET.get("productname")
    productlist=Service.objects.filter(name_of_service__icontains=productnames)
    istr='''
    <br><br>
    <h2 class="tit">Service Available:<h2/> 
    
     
  
<table class="table">
            
                <tr class="w3-blue">
                    <th class="i">Purpose_id</th>
                    <th class="i">Service Name</th>
                     <th class="i">Price per service</th>
                    </tr>
                    

''' 
    for product in productlist:
     istr+="<tr><td>"+str(product.purpose_id)+"</td><td>"+product.name_of_service+"</td><td>"+str(product.price)+"<tr><td>";
    return HttpResponse(istr)

def searches(request):
   return render(request,'searches.html')
