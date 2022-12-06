# Note: the module name is psycopg, not psycopg3
import psycopg
import json


"""

INSERT INTO intbl_purchaserequisition("RequisitionType","Date","TotalAmount","TaxAmount","Company_Name","State","ReceivedDate","purchaseBillNumber","DiscountAmount")VALUES ('hellow','2001-07-13'::date,9000,12233,'testcompany','hellowstatw','2001-07-13'::date,11222,1122221);

"""


"""
INSERT INTO intbl_purchaserequisition_contract
("ItemID","UnitsOrdered","PurchaseReqID","Rate","Name","BrandName","Code","UOM","StockType","Department","GroupName","ExpDate","Status","Taxable")
VALUES (1,12,1,11,123,1,'hellowname','testbarnd','1234','jfkljsdfdkjfldjsf','testgroupname',now()::date,'true','true');



"""
# Connect to an existing database
with psycopg.connect(
    f"host='localhost' dbname='silverline' user='postgres' password='root' port='5432' "
) as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        sql = f"insert into table RequisitionType"
        try:
            cur.execute(f'SELECT * FROM "intbl_purchaserequisition"')
        except Exception as E:
            print(E)
        cur.fetchone()
        print(cur.fetchall())
        conn.commit()
