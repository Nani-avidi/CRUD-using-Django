from django.shortcuts import render
from crudapp.models import Student
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def crud_op(request):
    if request.method == 'GET':
        b=request.GET['b']
        if b == "Add":
            resp =insert_data(request)
            return resp
        elif b == "Update":
            res= update_data(request)
            return res
        elif b== "Delete":
            res = delete_data(request)
            return res
        elif b == "Result":
            res= result(request)
            return res

def insert_data(request):
    rno = request.GET.get("rno")
    s1 = request.GET.get("sub1")
    s2 = request.GET.get("sub2")
    s3 = Student(rollno = rno, Sub1 = s1, Sub2 = s2)
    s3.save()
    msg = {'msg' :"Marks are added"}
    r = render(request,"home.html",context=msg)
    return r
    
def update_data(request):
    rno = request.GET.get("rno")
    try:
        stud = Student.objects.get(rollno = rno)
        stud.rollno = rno
        stud.Sub1 = request.GET.get("sub1")
        stud.Sub2 = request.GET.get("sub2")
        stud.save()
        msg={'msg': "Marks updated"}
    except ObjectDoesNotExist:
        msg = {'msg': "Invalid Roll Number"}

    return render(request, "home.html", context=msg)
def delete_data(request):
    rno = request.GET.get("rno")
    try:
        stud = Student.objects.get(rollno=rno)
        stud.delete()
        msg = {'msg': "Marks Deleted Successfully"}
    except ObjectDoesNotExist:
        msg = {'msg': "Invalid Roll Number - Cannot Delete"}

    return render(request, "home.html", context=msg)
from django.core.exceptions import ObjectDoesNotExist

def result(request):
    rno = request.GET.get("rno")

    if not rno:
        msg = {'msg': "Please enter Roll Number"}
        return render(request, "home.html", context=msg)

    try:
        ro = Student.objects.get(rollno=rno)
        sub1 = int(ro.Sub1)
        sub2 = int(ro.Sub2)

        res = "PASS" if sub1 >= 40 and sub2 >= 40 else "FAIL"
        context = {
            'rno': rno,
            'sub1': sub1,
            'sub2': sub2,
            'status': res,
        }
        return render(request, "result.html", context)

    except ValueError:
        msg = {'msg': "Invalid Marks Found - Contact Admin"}
        return render(request, "home.html", context=msg)

    except ObjectDoesNotExist:
        msg = {'msg': "Invalid Roll Number - No Result Found"}
        return render(request, "home.html", context=msg)


def home(request):
    r=render(request,"home.html")
    return r
