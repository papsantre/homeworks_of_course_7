from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils import timezone

from lms.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=25, verbose_name="Телефон", blank=True, null=True)
    city = models.CharField(max_length=25, verbose_name="Город", blank=True, null=True)
    avatar = models.ImageField(upload_to="users/avatars", verbose_name="Аватар", blank=True, null=True)
    last_login = models.DateTimeField(default=datetime.now, verbose_name="Время последнего посещения", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"


class Payments(models.Model):

    METHODS = (
        ("CASH", "Наличные"),
        ("TRANSFER", "Перевод")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    payments_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", blank=True, null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", blank=True, null=True)
    payment_amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=10, default="CASH", choices=METHODS, verbose_name="Способ оплаты")

    session_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Id сессии")
    payment_link = models.URLField(max_length=400, blank=True, null=True, verbose_name="Ссылка на оплату")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ("payments_date",)

    def __str__(self):
        return f"{self.user}"
