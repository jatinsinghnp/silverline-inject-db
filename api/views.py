from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
import psycopg2

print("connected ...")


def firsttable():
    conn = psycopg2.connect(
        f"host='localhost' dbname='silverline' user='postgres' password='root' port='5432' "
    )
    cur = conn.cursor()
    sql = """  
    select * from intbl_purchaserequisition;
    """
    try:
        cur.execute(sql)
        data = cur.fetchall()
    except Exception as e:
        print(e)
    return data


def secondtable(id):
    conn = psycopg2.connect(
        f"host='localhost' dbname='silverline' user='postgres' password='root' port='5432' "
    )
    cur = conn.cursor()
    sql2 = f"""
    
         select * from intbl_purchaserequisition_contract where "PurchaseReqID"={id};

    """
    try:
        cur.execute(sql2)
        data = cur.fetchall()
        print(json.loads(data))
    except Exception as e:
        print(e)
    return data


# dataf = [firsttable() + secondtable()]


# print(secondtable())

# Create your views here.
@api_view(["GET"])
def Apihome(request):
    data = firsttable()

    return JsonResponse({"purchaserequisition": data})


@api_view(["GET"])
def Api_details(request, id):

    data = secondtable(id)
    return JsonResponse({"intbl_purchaserequisition_contract": data})


@api_view(["POST"])
def Apisent(request):
    conn = psycopg2.connect(
        f"host='localhost' dbname='silverline' user='postgres' password='root' port='5432' "
    )
    cur = conn.cursor()

    body = request.body
    data = {}
    data = json.loads(body)

    # print(data)
    sql = f"""                                    
        INSERT INTO intbl_purchaserequisition
        ("IDIntbl_PurchaseRequisition","RequisitionType","Date","TotalAmount","TaxAmount","Company_Name","State","ReceivedDate","purchaseBillNumber","DiscountAmount","Outlet_Name")
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

    sql2 = f"""
        INSERT INTO intbl_purchaserequisition_contract
        ("ItemID","UnitsOrdered","PurchaseReqID","Rate","Name","BrandName","Code","UOM","StockType","Department","GroupName","ExpDate","Status","Taxable")
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    # VALUES ();
    try:

        cur.execute(
            sql,
            (
                data["PurchaseRequistionID"],
                data["RequisitionType"],
                data["Date"],
                data["TotalAmount"],
                data["TaxAmount"],
                data["Company_Name"],
                data["State"],
                data["ReceivedDate"],
                data["purchaseBillNumber"],
                data["DiscountAmount"],
                data["Outlet_Name"],
            ),
        )

        for data in data["RequisitionDetailsList"]:

            listdata = (
                data["ItemID"],
                data["UnitsOrdered"],
                data["PurchaseReqID"],
                data["Rate"],
                data["Name"],
                data["BrandName"],
                data["Code"],
                data["UOM"],
                data["StockType"],
                data["Department"],
                data["GroupName"],
                data["ExpDate"],
                data["Status"],
                data["Taxable"],
            )
            cur.execute(sql2, listdata)

        conn.commit()

        cur.close()
        conn.close()
        print("connection closed .....")

    except Exception as e:
        print(e)

    return JsonResponse(data)
