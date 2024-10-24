from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICES = (
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('SP', 'SPICY'),
        ('CH', 'CHILLI'),
        ('SP', 'SWEET'),
        ('FR', 'FRUIT'),
        ('OR', 'ORANGE'),
        ('BG', 'BAGELS'),
    )
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='')

    def __str__(self):
        return self.name