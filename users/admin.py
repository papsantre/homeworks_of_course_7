from django.contrib import admin

from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
    )
    list_filter = ("email",)
    search_fields = (
        "email",
    )


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "payments_date",
        "payment_amount",
        "payment_method",
    )
    list_filter = ("user",)
    search_fields = (
        "user",
    )
