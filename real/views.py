from distutils import dep_util
from django.http import HttpResponse
from django.shortcuts import render
from .models import Teacher,Department
from django.views.decorators.csrf import csrf_exempt
from .form import TeacherForm

# Create your views here.
def other(req):
    tchs=Teacher.objects.filter(id=23).get()
    return render(req,"index.html",{'teacher':tchs})
def mult(req,mult1):


    return HttpResponse(mult1)
@csrf_exempt
def search_results(request):
    if request.method=="POST":
        dept_id= request.POST.get("dept_id")
        name= request.POST.get("name")
        dept_head= request.POST.get("dep_head")
        data=Department(dep_id=dept_id,dept_head=dept_head,name=name)
        data.save()
        dpts=Department.objects.all()
        return render(request,"departments.html",{'dpts':dpts})
    return HttpResponse("Data will be sent")


def add_teacher(request):
    form=TeacherForm()
    if request.method=="POST":
        form=TeacherForm(request.POST,request.FILES)
        print("We are sending Data")
        if form.is_valid():
            form.save()
        return HttpResponse("Data has been added Succesfully")
    return render(request,"teachers.html",{'form':form})
