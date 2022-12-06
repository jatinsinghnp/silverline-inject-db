from .models import intbl_purchaserequisition, intbl_purchaserequisition_contract
from rest_framework.serializers import ModelSerializer


class ModelPurchasereQuisitionSerializers(ModelSerializer):
    class Meta:
        model = intbl_purchaserequisition
        fields = "__all__"


class Modelpurchaserequisition_contract_Serilizers(ModelSerializer):
    model = intbl_purchaserequisition_contract
    fields = "__all__"
