from django.db import models

from config.settings import AUTH_USER_MODEL


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to="lms/courses", verbose_name="Превью", blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата последнего обновления")
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Владелец")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    preview = models.ImageField(
        upload_to="lms/lessons", verbose_name="Превью", blank=True, null=True
    )
    url = models.CharField(
        max_length=100, verbose_name="Ссылка на видео", blank=True, null=True
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", blank=True, null=True)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Владелец")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Курс')
    sign_of_subscription = models.BooleanField(default=False, verbose_name='Признак подписки')

    def __str__(self):
        return f'{self.user}: ({self.course})'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
