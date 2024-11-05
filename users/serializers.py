
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payments, User


class PaymentsSerializer(ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
