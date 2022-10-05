import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def password(request):

    # a~z
    chars = [chr(c) for c in range(97,123)]
    # None ==> False
    if request.GET.get('uppercase'):
        chars+=[chr(c).upper() for c in range(97,123)]

    if request.GET.get('numbers'):
        chars+=list('0123456789')

    if request.GET.get('special'):
        chars+=list('!@#$%^&*')

    print(chars)
    # input_length=request.GET.get('input-length')
    # print(input_length,type(input_length))
    # if input_length=='':
    #     input_length=request.GET.get('length')
    #     print(input_length)
    # 取得輸入的長度
    length=eval(request.GET.get('length')) if request.GET.get('input-length')=='' \
        else eval(request.GET.get('input-length'))

    # 樣本數(不會重複，但不能取樣超過容器大小)
    #print(random.sample(chars,length))
    password=''.join([random.choice(chars) for i in range(length)])

    # 變成字串
    print(password)
    print(length)

    return render(request,'./password.html',{'password':password})

def index(request):
    print('Hello Django')

    return render(request,'./index.html')