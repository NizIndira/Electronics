from django.db import models

from config.settings import NULLABLE


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель', **NULLABLE)
    launch_date = models.DateField(verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class NetworkLink(models.Model):
    CATEGORY_CHOICES = (
        ('Factory', 'завод'),
        ('Retail', 'розничная сеть'),
        ('Entrepreneur', 'индивидуальный предприниматель')
    )
    name = models.CharField(max_length=100, verbose_name='название')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=12, verbose_name='категория')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    products = models.ManyToManyField(Product, verbose_name='продукты')
    debt = models.DecimalField(default=0, max_digits=10, decimal_places=2,
                               verbose_name='задолженность', **NULLABLE)
    tier = models.PositiveSmallIntegerField(default=0, verbose_name='уровень поставщика')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.name} - {self.get_category_display()}'

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'


class Contact(models.Model):
    network_link = models.ForeignKey(NetworkLink, on_delete=models.CASCADE, verbose_name='название')
    email = models.EmailField(verbose_name='почта', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    building_number = models.CharField(max_length=50, verbose_name='номер дома', **NULLABLE)

    def __str__(self):
        return f'{self.network_link.name} - {self.country}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
