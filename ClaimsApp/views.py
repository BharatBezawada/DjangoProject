import csv, datetime, io
import datetime

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse
from .models import Claims, CreditLimits
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
    Limit_Type = request.POST.get("Creditlimitcheck")
    Report_date = request.POST["Report_date"]
    Limit_Withdrawal = request.POST["Limit_Withdrawal"]
    Claim_Extension = request.POST["Claim_Extension"]
    Claim_Extension_Number = request.POST["Number_of_extensions"]

    if Limit_Type is None or Report_date == "2017-01-01" or Limit_Withdrawal == "2017-01-01":
        messages.error(request, 'All fields are Mandatory Except Claim Extension')
        return render(request, "ClaimsApp/body.html")

    qs = Claims.objects.all()
    if qs.filter(PAN__icontains=PAN).exists() and qs.filter(Insured_Name__icontains=Insured_Name).exists():
        messages.error(request, 'NNP Registered Already for the Insured')
        return render(request, "ClaimsApp/body.html")

    else:

        claim_info = Claims(Insured_Name=Insured_Name, Buyer_name=Buyer_name, PAN=PAN, Default_Amt=Default_Amt,
                            Limit_Type=Limit_Type, Report_date=Report_date, Limit_Withdrawal=Limit_Withdrawal,
                            Claim_Extension=Claim_Extension,
                            Claim_Extension_Number=Claim_Extension_Number)
        claim_info.save()
        messages.success(request, 'NNP registered successfully')
        return render(request, "ClaimsApp/body.html")


def app_data(request):
    return HttpResponse("Hello World")


def export(request):
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(
        ['Insured Name', 'Buyer Name', 'PAN', 'Default Amount', 'Limit Type', 'Report date', 'Limit Withdrawal Date',
         'Claim Filing Extension', 'Claim Filing Extension No', 'Claim Status'])

    for buyer in Claims.objects.all().values_list('Insured_Name', 'Buyer_name', 'PAN', 'Default_Amt', 'Limit_Type',
                                                  'Report_date', 'Limit_Withdrawal', 'Claim_Extension',
                                                  'Claim_Extension_Number', 'Claim_status'):
        writer.writerow(buyer)

    response['Content-Disposition'] = 'attachment; filename="NNP.csv"'
    return response


def search(request):
    query = request.GET.get("search")
    qs = Claims.objects.all()
    if query is not None:

        if qs.filter(Buyer_name__contains=query) is None:
            qs = qs.filter(PAN__istartswith=query)
        else:
            qs = qs.filter(Buyer_name__contains=query)

    return render(request, "ClaimsApp/body.html", {'buyer_list': qs})


# buyers = Claims.object.all().filter(name__contains = search_term).values_list('Buyer_name')
# return render(request,'ClaimsApp/body.html', {'Buyers':buyers})

def CreditLimit(request):
    template = "ClaimsApp/CreditLimits.html"
    data = CreditLimits.objects.all()
    prompt = {'order': 'Order of the CSV should be Insured,PAN,Insured, Buyername,Address,CLA,CLD,CLA Date,CLD Date,'
                       'Effective Date',
              'profiles': data}
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = CreditLimits.objects.update_or_create(
            Insured_Name=column[0],
            PAN=column[1],
            Insured_ref=column[2],
            Buyer_name=column[3],
            CLA=column[5],
            CLD=column[6],
            CLA_Date=column[7],
            CLD_Date=column[8],
            Effective_Date=column[9],

        )
    context = {}
    return render(request, template, context)


def search_limit(request):
    query = request.GET.get("search")
    qs = CreditLimits.objects.all()
    if query is not None:

        if qs.filter(Buyer_name__contains=query) is None:
            qs = qs.filter(PAN__istartswith=query)
        else:
            qs = qs.filter(Buyer_name__contains=query)

    return render(request, "ClaimsApp/body.html", {'credit_list': qs})
