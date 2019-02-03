from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')
def contact(request):
    return render(request,'personal/basic.html',{'content':['you could contact me at','savishbedi1@gmail.com']})
