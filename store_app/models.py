from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_check(value):
    if value <= 0:
        raise ValidationError('Value must be positive.')



class Supplier(models.Model):
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'Supplier'

    def __str__(self) -> str:
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2, 
                                validators=[validate_check] )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Product'


    def __str__(self) -> str:
        return f'Product: {self.name}. and Price {self.price}'