import csv, datetime
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse
from .models import Claims
from django.contrib import messages


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

    qs = Claims.objects.all()
    if qs.filter(PAN__icontains=PAN).exists() and qs.filter(Insured_Name__icontains=Insured_Name).exists():
        messages.error(request, 'NNP Registered Already for the Insured')
        return render(request, "ClaimsApp/body.html")

    else:

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
    writer.writerow(
        ['Insured Name', 'Buyer Name', 'PAN', 'Default Amount', 'Limit Type', 'Report date', 'Claim Status'])

    for buyer in Claims.objects.all().values_list('Insured_Name', 'Buyer_name', 'PAN', 'Default_Amt', 'Limit_Type',
                                                  'Report_date', 'Claim_status'):
        writer.writerow(buyer)

    response['Content-Disposition'] = 'attachment; filename="NNP.csv"'
    return response


def search(request):
    query = request.GET.get("search")
    qs = Claims.objects.all()
    if query is not None:
        qs = qs.filter(Buyer_name__icontains=query)

    return render(request, "ClaimsApp/body.html", {'buyer_list': qs})

# buyers = Claims.object.all().filter(name__contains = search_term).values_list('Buyer_name')
# return render(request,'ClaimsApp/body.html', {'Buyers':buyers})
