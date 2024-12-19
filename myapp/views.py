from django.shortcuts import render
from myapp.Forms import Studentform

# Create your views here.
def Formview(request):
    f=Studentform()
    if request.method=="POST":
    	f=Studentform(request.POST)
    	if f.is_valid():
    		name=f.cleaned_data['name']
    		usn=f.cleaned_data['usn']
    		mob=f.cleaned_data['mob']
    		branch=f.cleaned_data['branch']
    		email=f.cleaned_data['email']
    		d={'name':name,'usn':usn,'mob':mob,'branch':branch,'email':email}
    		return render(request,'htmlpage/output.html',d)
    d={'form':f}
    return render(request,'htmlpage/input.html',d)

