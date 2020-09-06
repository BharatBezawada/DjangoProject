from django.db import models

# Create your models here.

class Claims(models.Model):
     Insured_Name = models.CharField(max_length=20)
     Buyer_name = models.CharField(max_length=20)
     PAN = models.CharField(max_length=20)
     Default_Amt = models.CharField(max_length=20)
     Limit_Type = models.CharField(max_length=20,default=0)
     Report_date = models.DateField()
     Claim_status = models.CharField(max_length=20,default=0)

     def __str__(self):
         return self.Buyer_name

class Meta:
          verbose_name = "Claim"







