from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views import ProductViewSet, NetworkLinkListAPIView, NetworkLinkCreateAPIView, NetworkLinkUpdateAPIView, \
    NetworkLinkViewAPIView, NetworkLinkDeleteAPIView, ContactViewSet

app_name = MainConfig.name

router_product = DefaultRouter()
router_product.register('product', ProductViewSet, basename='product')
router_contact = DefaultRouter()
router_contact.register('contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('netlink/', NetworkLinkListAPIView.as_view(), name='netlink_list'),
    path('netlink/create/', NetworkLinkCreateAPIView.as_view(), name='netlink_create'),
    path('netlink/update/<int:pk>/', NetworkLinkUpdateAPIView.as_view(), name='netlink_update'),
    path('netlink/view/<int:pk>/', NetworkLinkViewAPIView.as_view(), name='netlink_view'),
    path('netlink/delete/<int:pk>/', NetworkLinkDeleteAPIView.as_view(), name='netlink_delete'),

    path('', include(router_product.urls)),
    path('', include(router_contact.urls)),
]
