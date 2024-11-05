
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
# from rest_framework.viewsets import ModelViewSet

from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer, PaymentSerializer
from users.services import convert_rub_to_dol, create_stripe_price, create_stripe_session, create_stripe_product


class PaymentsListApiView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["payment_method"]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["payment_method"]
    ordering_fields = ["payments_date"]


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        stripe_product_id = create_stripe_product(payment)
        amount_in_doll = convert_rub_to_dol(payment.payment_amount)
        price = create_stripe_price(stripe_product_id, amount_in_doll)
        session_id, payment_link = create_stripe_session(price)

        payment.session_id = session_id
        payment.payment_link = payment_link
        payment.save()
