from rest_framework import serializers

from main.models import Product, Contact, NetworkLink
from main.validators import NetworkLinkValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactListDetailSerializer(serializers.ModelSerializer):
    network_link_name = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        exclude = ('network_link',)

    def get_network_link_name(self, obj):
        return obj.network_link.name if obj.network_link else None


class NetworkLinkSerializer(serializers.ModelSerializer):
    validators = [NetworkLinkValidator(),]

    class Meta:
        model = NetworkLink
        fields = '__all__'


class NetworkLinkUpdateSerializer(serializers.ModelSerializer):
    validators = [NetworkLinkValidator(),]

    class Meta:
        model = NetworkLink
        fields = '__all__'

    def validate(self, attrs):
        if 'debt' in attrs:
            raise serializers.ValidationError("Обновление поля запрещено!")
        return attrs


class NetworkLinkListViewSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display', read_only=True)
    addresses = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkLink
        fields = ('id', 'name', 'category', 'supplier', 'debt', 'tier', 'addresses', 'products',)

    def get_addresses(self, obj):
        contacts = obj.contact_set.all()
        return ContactSerializer(contacts, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = ProductSerializer(instance.products.all(), many=True).data
        return representation
