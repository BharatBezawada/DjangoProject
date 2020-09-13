from django.db import models
from django.conf import settings

# Create your models here.



class Claims(models.Model):
    Insured_Name = models.CharField(max_length=50)
    Buyer_name = models.CharField(max_length=50)
    PAN = models.CharField(max_length=20)
    Default_Amt = models.CharField(max_length=20)
    Limit_Type = models.CharField(max_length=20, default=0)
    Report_date = models.DateField()
    Claim_status = models.CharField(max_length=1000, default="NNP", choices=[('NNP', 'NNP'), ('Claim', 'Claim'), (
        'Claim Under Process', 'Claim Under Process'),
                                                                             ('Repudiated', 'Repudiated'),
                                                                             ('Disputed', 'Disputed'),
                                                                             ('Paid and Closed', 'Paid and Closed'),
                                                                             ('Overdue Cleared', 'Overdue Cleared'), (
                                                                                 'Overdue Cleared and Reinstated',
                                                                                 'Overdue Cleared and Reinstated')])
    Limit_Withdrawal = models.DateField()
    Claim_Extension = models.DateField()
    Claim_Extension_Number = models.CharField(max_length=50, default="NIL",
                                              choices=[('NIL', 'NIL'), ('FIRST', 'FIRST'), ('SECOND', 'SECOND'),
                                                       ('THIRD', 'THIRD'), ('FOURTH', 'FOURTH'), ('FIFTH', 'FIFTH')])

    def __str__(self):
        return self.Buyer_name

    class Meta:
        verbose_name = "Claim"


class CreditLimits(models.Model):
    Insured_Name = models.CharField(max_length=100,blank=True)
    PAN = models.CharField(max_length=20,default=0,blank=True)
    Insured_ref = models.CharField(max_length=100,default=0,blank=True)
    Buyer_name = models.CharField(max_length=200,default=0,blank=True)
    Address = models.CharField(max_length=200,default=0,blank=True)
    CLA = models.CharField(max_length=100,default=0,blank=True)
    CLD = models.CharField(max_length=100,default=0,blank=True)
    CLA_Date = models.DateField()
    CLD_Date = models.DateField()
    Effective_Date = models.DateField()

    def __str__(self):
        return self.Buyer_name

    class Meta:
        verbose_name = "CreditLimit"
