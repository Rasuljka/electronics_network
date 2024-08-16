from django.db import models


class ContactInfo(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        """Возвращает контактную информацию"""
        return f"{self.street}, {self.city}, {self.country} - {self.house_number}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        """Возвращает название продукта"""
        return f"{self.name} ({self.model})"


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=100)
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    supplier = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL
    )
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает название узла сети"""
        return self.name


class ProductStock(models.Model):
    node = models.ForeignKey(
        NetworkNode, related_name="products", on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        """Возвращает информацию о наличии продукта в узле сети"""
        return f"{self.product} at {self.node}"
