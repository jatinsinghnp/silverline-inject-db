from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
intbl_purchaserequisition = {}
parser = reqparse.RequestParser()
parser.add_argument("RequisitionType", type=str, help="string name")
parser.add_argument("Date", type=str, help="date field")
parser.add_argument("TotalAmount", type=int, help="totalamount")
parser.add_argument("TaxAmount", type=float, help="taxamount")
parser.add_argument("Company_Name", type=str, help="name of comapny")
parser.add_argument("State", type=str, help="enter state")
parser.add_argument("ReceivedDate", type=str, help="Recive date state")
parser.add_argument("purchaseBillNumber", type=int, help="purchaseBillNumber")
parser.add_argument("DiscountAmount", type=int, help="DiscountAmount")

args = parser.parse_args()


class SentDataToServer(Resource):
    def get(self):
        return {"hello": "world"}

    # def post(self):
    #     args=parser.parse_args()


api.add_resource(SentDataToServer, "/")

if __name__ == "__main__":
    app.run(debug=True)
