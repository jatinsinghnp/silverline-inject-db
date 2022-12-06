from django.db import models

# Create your models here.
class intbl_purchaserequisition(models.Model):
    IDIntbl_PurchaseRequisition = models.IntegerField(primary_key=True)
    RequisitionType = models.CharField(max_length=50)
    Date = models.CharField(max_length=100)
    TotalAmount = models.FloatField()
    TaxAmount = models.FloatField()
    Company_Name = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    ReceivedDate = models.CharField(max_length=200)
    purchaseBillNumber = models.IntegerField()
    DiscountAmount = models.FloatField()
    Outlet_Name = models.CharField(max_length=200)


class intbl_purchaserequisition_contract(models.Model):
    IDIntbl_PurchaseRequisition_Contract = models.CharField(max_length=200)
    ItemID = models.IntegerField()
    UnitsOrdered = models.IntegerField()
    PurchaseReqID = models.ForeignKey(
        intbl_purchaserequisition, on_delete=models.CASCADE
    )
    Rate = models.FloatField()
    Name = models.CharField(max_length=200)
    BrandName = models.CharField(max_length=200)
    Code = models.CharField(max_length=200)
    UOM = models.CharField(max_length=200)
    StockType = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    GroupName = models.CharField(max_length=200)
    ExpDate = models.CharField(max_length=200)
    Status = models.CharField(max_length=200)
    Taxable = models.CharField(max_length=200)
