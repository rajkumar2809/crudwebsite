from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import signup_user
from django.http import JsonResponse
from django.db.models import Count

# Create your views here.


def index(request):
    return render(request,"index.html")

def signup2(request):


    all_data = signup_user.objects.all().order_by("-id")

    if request.method == "POST":
        nm = request.POST["name"]
        con = request.POST["contact"]
        rol = request.POST["roll"]
        sub = request.POST["subject"]
        data = signup_user(name=nm, contact_no=con, roll_no=rol,subject=sub)
        data.save()


        res = "Dear {} Thank you For register score is ".format(nm)
        return render(request, "signup.html", { "status":res,"messages": all_data})

    # to display feedback in another page Httpresponse has been used
    # return HttpResponse ("<h1 style = 'color:green' > Dear {} Data saved succesfully</h1>".format(nm))




    return render (request,"signup.html",{"messages":all_data})


def viewdata(request):
    all_data = signup_user.objects.all().order_by("-id")
    x=signup_user.objects.all().values('subject').annotate(total=Count('subject')).order_by('total')
    y={i.get('subject') : i.get("total")for i in x}
    subject=y.keys()
    count=y.values()
    print(subject,count)
    return render (request,"viewdata.html",{"messages": all_data,"subject":subject,"count":count})


def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        pi = signup_user.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse ({'status':0})




def edit_data (request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        student = signup_user.objects.get(pk=id)
        student_data = { "id" :student.id, "name" : student.name ,"contact":student.contact_no, "roll":student.roll_no , "subject":student.subject }
        return JsonResponse(student_data)


def update_data(request):
    all_data = signup_user.objects.all().order_by("-id")
    if request.method == "POST":
        sid = request.POST.get('stuid')
        nm = request.POST['name']
        con = request.POST['contact']
        roll = request.POST['roll']
        sub = request.POST['subject']




        if (sid == ''):
            data = signup_user(name=nm, contact_no=con, roll_no=roll, subject=sub )

        else:
            data = signup_user(id=sid ,name=nm, contact_no=con, roll_no=roll, subject=sub)

        data.save()
        return render(request,"viewdata.html",{ "messages":all_data})
        #print(id)
        #student = signup_user.objects.get(pk=id)
        #student_data = { "id" :student.id, "name" : student.name ,"contact":student.contact_no, "roll":student.roll_no , "subject":student.subject }


        #data = signup_user(name=nm, contact_no=con, roll_no=rol,subject=sub)
        #data.save()

        #res = "Dear {} Thank you For register".format(nm)
        #return render(request, "signup.html", { "status":res,"messages": all_data})

    # to display feedback in another page Httpresponse has been used
    # return HttpResponse ("<h1 style = 'color:green' > Dear {} Data saved succesfully</h1>".format(nm))




    #return render (request,"signup.html",{"messages":all_data})
    return render (request,"viewdata.html",{"messages": all_data})
