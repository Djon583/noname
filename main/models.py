from django.db import models
from django.contrib.auth.models import User

""" ========= Category =========================== """
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, default='', verbose_name="Название")
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
    def __str__(self):
        return self.name


""" ========= Products =============================== """
class Products(models.Model):
    name = models.CharField(max_length=100, null=False, default='', verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    details = models.CharField(max_length=100, null=False, default='', verbose_name="Характеристика")
    category_id = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE, verbose_name="Категория")
    link_img = models.ImageField(blank=False, null=True, verbose_name="Картинки")
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'
    def __str__(self):
        return self.name


""" ========= ListOrders =============================== """
class ListOrders(models.Model):
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, verbose_name="Пользователь ID")
    product_id = models.ForeignKey('Products', related_name='product_order', on_delete=models.CASCADE, verbose_name="Продукт ID")
    class Meta:
        verbose_name = 'Список заказов'
        verbose_name_plural = 'Список заказов'
    def __str__(self):
        return 'Список заказов'


""" ========= Comments =============================== """
class Comments(models.Model):
    status = models.IntegerField(default='0', verbose_name="Статус");
    product_id = models.ForeignKey('Products', related_name='product', on_delete=models.CASCADE, verbose_name="Продукт ID")
    user_id = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE, verbose_name="Пользователь ID")
    text = models.CharField(max_length=200, null=False, default='', verbose_name="Комментария")
    class Meta:
        verbose_name = 'Комментария'
        verbose_name_plural = 'Коментария'
    def __str__(self):
        return 'Комментария'
