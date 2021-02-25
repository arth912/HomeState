from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import new_p,slides
import numpy as np
import joblib
import json
import os
# Create your views here.
def index(request):

    nps =new_p.objects.all()

    s1=slides()
    s1.name = 'New House in Bangalore, INDIA'
    s1.img = 'img-1.jpg'
    s1.desc = 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'
    s1.sq =  2000
    s1.price = 15000
    s1.bath =3
    s1.bed =4
    s1.rent= True
    s1.sale=False

    s2=slides()
    s2.name = 'New House in Vadodara, INDIA'
    s2.img = 'img-2.jpg'
    s2.desc = 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'
    s2.sq =  2000
    s2.price = 8000
    s2.bath =3
    s2.bed =4
    s2.rent= False
    s2.sale=True

    s3=slides()
    s3.name = 'New House in Bangalore, INDIA'
    s3.img = 'img-3.jpg'
    s3.desc = 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'
    s3.sq =  2000
    s3.price = 14000
    s3.bath =3
    s3.bed =4
    s3.rent= True
    s3.sale=False

    slide =[ s1 ,s2 ,s3]


    return render(request,'index.html',{'nps':nps,'slide':slide});

def agent(request):
    return render(request,'agent.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):    
    return render(request,'contact.html')


def prediction(request):
    
    return render(request,'prediction.html')

def buy_property(request):
   

    nps =new_p.objects.all()
    return render(request,'buy_property.html',{'nps':nps});

def sell_property(request):

    if request.method =='POST' :
        name = request.POST['name']
        img = request.POST['img']
        desc = request.POST['desc']
        sq = request.POST['area']
        price =  request.POST['price']
        bath =  request.POST['bathroom']
        bed = request.POST['bedroom']
        address = request.POST['address']
        sale = request.POST['p_status']

        print(name, desc ,sq ,price, bath ,bed ,address ,sale,img)
        
        sell=new_p.objects.create(name=name,img=img ,desc=desc ,sq=sq , price=price, bath=bath, bed=bed, address=address ,sale=sale)
        sell.save();
        print('add successfully')
        return redirect('/')
    else:
        return render(request,'sell_property.html');

def predict_price(lis):
    curr_work_dir = os.getcwd()
    file_path = os.path.join(curr_work_dir,"homestate/data_columns.json")
    print(file_path)
    with open(file_path) as f:
        data = json.load(f)
    columns = data["data_columns"]

    loc_idx = columns.index(lis[0])
    
    sqft = lis[1] 
    bath = lis[2]
    bhk = lis[3]

    x = np.zeros(len(columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_idx >= 0:
        x[loc_idx] = 1

    lr_clf=joblib.load('final.sav')
    
    return lr_clf.predict([x])[0]

def result(request):
    
    
    
    lis =[]
    lis.append(request.GET['loc'])
    lis.append(request.GET['area'])
    lis.append(request.GET['bedroom'])
    lis.append(request.GET['bathroom'])

    print(lis)
    loc=lis[0]
    sq=lis[1]
    bed=lis[2]
    bath=lis[3]
    # print(len(lis))

    ans = predict_price(lis)

    # lis1=np.array(lis)
    # lis2=lis1.reshape(1,-1)
    # ans=lr_cls.predict(lis2)

    return render(request,'result.html',{'ans':ans,'loc':loc,'sq':sq,'bed':bed,'bath':bath})