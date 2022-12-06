from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from datetime import datetime
import psycopg2
from dateutil import parser


print("connected ...")


def firsttable():
    conn = psycopg2.connect(
        f"host='localhost' dbname='silverline' user='postgres' password='root' port='5432' "
    )
    cur = conn.cursor()
    sql = """
    
    SELECT array_to_json(array_agg(row_to_json(r))) FROM public.intbl_purchaserequisition r;


    """
    try:
        cur.execute(sql)
        data = cur.fetchall()

    except Exception as e:
        print(e)
    return data


def secondtable():
    conn = psycopg2.connect(
        f"host='localhost' dbname='silverline' user='postgres' password='root' port='5432' "
    )
    cur = conn.cursor()
    sql2 = """
    
SELECT array_to_json(array_agg(row_to_json(r))) FROM public.intbl_purchaserequisition_contract r;
    """
    try:
        cur.execute(sql2)
        data = cur.fetchall()

    except Exception as e:
        print(e)
    return data


dataf = [firsttable() + secondtable()]


# print(secondtable())

# Create your views here.
@api_view(["GET"])
def Apihome(request):

    return JsonResponse({"data": dataf})


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

        cur.execute(
            sql2,
            (
                data["RequisitionDetailsList"][0]["ItemID"],
                data["RequisitionDetailsList"][0]["UnitsOrdered"],
                data["RequisitionDetailsList"][0]["PurchaseReqID"],
                data["RequisitionDetailsList"][0]["Rate"],
                data["RequisitionDetailsList"][0]["Name"],
                data["RequisitionDetailsList"][0]["BrandName"],
                data["RequisitionDetailsList"][0]["Code"],
                data["RequisitionDetailsList"][0]["UOM"],
                data["RequisitionDetailsList"][0]["StockType"],
                data["RequisitionDetailsList"][0]["Department"],
                data["RequisitionDetailsList"][0]["GroupName"],
                data["RequisitionDetailsList"][0]["ExpDate"],
                data["RequisitionDetailsList"][0]["Status"],
                data["RequisitionDetailsList"][0]["Taxable"],
            ),
        )

        conn.commit()

        cur.close()
        conn.close()
        print("connection closed .....")

    except Exception as e:
        print(e)

    return JsonResponse(data)
