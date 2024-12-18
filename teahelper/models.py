from django.db import models
from django.contrib.auth.models import User

class Tea(models.Model):
    TEA_CHOICE = [
        ('black_tea', 'Черный чай'),
        ('white_tea', 'Белый чай'),
        ('green_tea', 'Зеленый чай'),
        ('red_tea', 'Красный чай'),
    ]
    
    name = models.CharField(max_length=55, choices=TEA_CHOICE, unique=True, verbose_name='Наименование чая')
    
    def __str__(self):
        return self.get_name_display();
    
    class Meta:
        verbose_name = 'Чай'
        verbose_name_plural = 'Чаи'
        
        
class Request(models.Model):
    PAY_CHOICES = [
        ('offline', 'Наличные'),
        ('online', 'Картой'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    contact_info = models.CharField(max_length=150, verbose_name='Контактная информация')
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE, verbose_name='Чай', null=True)
    pay_type = models.CharField(max_length=15, choices=PAY_CHOICES, verbose_name='Тип оплаты')
    
    def __str__(self):
        return f"{self.user.username} - {self.contact_info.get_name_display()}" 
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    