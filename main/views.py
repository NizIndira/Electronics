import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from main.models import Product, Contact, NetworkLink
from main.permissions import IsActive
from main.serializers import ProductSerializer, ContactSerializer, ContactListDetailSerializer, NetworkLinkSerializer, \
    NetworkLinkListViewSerializer, NetworkLinkUpdateSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActive]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [IsActive]

    default_serializer = ContactSerializer
    ListSerializers = {
        'list': ContactListDetailSerializer,
        'retrieve': ContactListDetailSerializer,
    }

    def get_serializer_class(self):
        return self.ListSerializers.get(self.action, self.default_serializer)


class NetworkLinkCreateAPIView(CreateAPIView):
    serializer_class = NetworkLinkSerializer
    permission_classes = [IsActive]


class NetworkLinkViewAPIView(RetrieveAPIView):
    serializer_class = NetworkLinkListViewSerializer
    queryset = NetworkLink.objects.all()
    permission_classes = [IsActive]


class NetworkLinkFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='contact__country', lookup_expr='exact')

    class Meta:
        model = NetworkLink
        fields = ['country']


class NetworkLinkListAPIView(ListAPIView):
    serializer_class = NetworkLinkListViewSerializer
    queryset = NetworkLink.objects.all()
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NetworkLinkFilter


class NetworkLinkUpdateAPIView(UpdateAPIView):
    serializer_class = NetworkLinkUpdateSerializer
    queryset = NetworkLink.objects.all()
    permission_classes = [IsActive]


class NetworkLinkDeleteAPIView(DestroyAPIView):
    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()
    permission_classes = [IsActive]
