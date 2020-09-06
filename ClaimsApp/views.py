import csv, datetime
from datetime import datetime
import git
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse
from .models import Claims
from django.contrib import messages

@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("bharatbezawada.pythonanywhere.com/")
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")


# Create your views here.
def index(request):
    return render(request, "ClaimsApp/body.html")


def buyer_data(request):
    all_buyers = Claims.objects.all()
    return render(request, "ClaimsApp/all_buyers.html", {'Buyers': all_buyers})


def add_data(request):
    print("Hello")
    Insured_Name = request.POST["InsuredName"]
    Buyer_name = request.POST["Buyer_Name"]
    PAN = request.POST["pan"]
    Default_Amt = request.POST["default"]
    Limit_Type = request.POST["Creditlimitcheck"]
    Report_date = request.POST["Report_date"]
    strDate = 'Report_date'

    claim_info = Claims(Insured_Name=Insured_Name, Buyer_name=Buyer_name, PAN=PAN, Default_Amt=Default_Amt,
                        Limit_Type=Limit_Type, Report_date=Report_date)
    claim_info.save()
    messages.success(request, 'NNP registered successfully')

    return render(request, "ClaimsApp/body.html")


def app_data(request):
    return HttpResponse("Hello World")


def export(request):
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(['Insured Name', 'Buyer Name', 'PAN', 'Default Amount', 'Limit Type', 'Report date','Claim Status'])

    for buyer in Claims.objects.all().values_list('Insured_Name', 'Buyer_name', 'PAN', 'Default_Amt', 'Limit_Type',
                                                  'Report_date','Claim_status'):
        writer.writerow(buyer)

    response['Content-Disposition'] = 'attachment; filename="NNP.csv"'
    return response


def search(request):
    query = request.GET.get("search")
    qs = Claims.objects.all()
    if query is not None:
        qs = qs.filter(Buyer_name__icontains = query )


    return render(request ,"ClaimsApp/body.html" , {'buyer_list':qs})

# buyers = Claims.object.all().filter(name__contains = search_term).values_list('Buyer_name')
# return render(request,'ClaimsApp/body.html', {'Buyers':buyers})
