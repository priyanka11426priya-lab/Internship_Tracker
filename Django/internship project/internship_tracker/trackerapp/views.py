from django.shortcuts import render, redirect
from . import dbcon

def add(request):
    return render(request, 'add.html')
def addsave(request):
    regno = request.GET['regno']
    name = request.GET['name']
    department = request.GET['department']
    company = request.GET['company']
    duration = request.GET['duration']
    domain = request.GET['domain']
    mail = request.GET['mail']

    data = {
        "regno": regno,
        "name": name,
        "department": department,
        "company": company,
        "duration": duration,
        "domain": domain,
        "mail": mail,
    }
    dbcon.col.insert_one(data)
    return redirect('listdata')

def listdata(request):
    interns = dbcon.col.find()
    return render(request, 'list.html', {'var': interns})

def edit(request, regno):
    entry = dbcon.col.find_one({"regno": regno})  # fixed variable name from 'empty' to 'entry'
    if request.method == "POST":
        name = request.POST["name"]
        department = request.POST["department"]
        company = request.POST["company"]
        duration = request.POST["duration"]
        domain = request.POST["domain"]
        mail = request.POST["mail"]
        dbcon.col.update_one(
            {"regno": regno},
            {"$set": {
                "name": name,
                "department": department,
                "company": company,
                "duration": duration,
                "domain": domain,
                "mail": mail
            }}
        )
        return redirect('listdata')
    return render(request, "edit.html", {"entry": entry})

def delete(request, regno):
    dbcon.col.delete_one({"regno": regno})
    return redirect('listdata')
