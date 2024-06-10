from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from main.models import NetworkLink, Product, Contact


@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier_link', 'debt', 'tier', 'created_date',)
    filter_horizontal = ('products',)
    list_filter = ('category', 'supplier', 'contact__city',)
    actions = ('clear_debt',)

    def clear_debt(self, request, queryset):
        """ Метод очищает задолженность перед поставщиком в админ-панели"""
        for network_link in queryset:
            network_link.debt = 0
            network_link.save()
        self.message_user(request, 'Задолженность перед поставщиком удалена')
    clear_debt.short_description = "Удалить задолженность перед поставщиком"

    def supplier_link(self, obj):
        """ Метод показывает в табличной части админ-панели ссылку на поставщика"""
        if obj.supplier:
            link = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),
                           args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier.name)
        else:
            return "None"
    supplier_link.short_description = "Поставщик"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'launch_date',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('network_link', 'email', 'country',)
