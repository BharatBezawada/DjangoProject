from django.contrib import admin
from .models import Claims, CreditLimits


# Register your models here.

class ClaimsAdmin(admin.ModelAdmin):
    list_display = ('Insured_Name', 'Buyer_name', 'PAN', 'Claim_status')
    search_fields = ('Buyer_name', 'Insured_Name', 'PAN')


class CreditLimitsAdmin(admin.ModelAdmin):
    list_display = ('Insured_Name', 'Buyer_name','PAN','CLA','CLD','CLA_Date','CLD_Date')
    search_fields = ('Buyer_name', 'Insured_Name', 'PAN')


admin.site.register(Claims, ClaimsAdmin)
admin.site.register(CreditLimits, CreditLimitsAdmin)
