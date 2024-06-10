from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from main.models import Product, Contact, NetworkLink
from main.serializers import ProductSerializer, ContactSerializer, ContactListDetailSerializer, NetworkLinkSerializer, \
    NetworkLinkListViewSerializer, NetworkLinkUpdateSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()

    default_serializer = ContactSerializer
    ListSerializers = {
        'list': ContactListDetailSerializer,
        'retrieve': ContactListDetailSerializer,
    }

    def get_serializer_class(self):
        return self.ListSerializers.get(self.action, self.default_serializer)


class NetworkLinkCreateAPIView(CreateAPIView):
    serializer_class = NetworkLinkSerializer


class NetworkLinkViewAPIView(RetrieveAPIView):
    serializer_class = NetworkLinkListViewSerializer
    queryset = NetworkLink.objects.all()


class NetworkLinkListAPIView(ListAPIView):
    serializer_class = NetworkLinkListViewSerializer
    queryset = NetworkLink.objects.all()


class NetworkLinkUpdateAPIView(UpdateAPIView):
    serializer_class = NetworkLinkUpdateSerializer
    queryset = NetworkLink.objects.all()


class NetworkLinkDeleteAPIView(DestroyAPIView):
    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()
