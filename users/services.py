
import stripe
from config.settings import STRIPE_API_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """ Создаем stripe продукт. """
    # print(stripe.api_key)
    # print(STRIPE_API_KEY)
    # print(f"{instance.paid_course}")

    title_product = f"{instance.paid_course}" if instance.paid_course else instance.paid_lesson
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get("id")


def convert_rub_to_dol(amount):
    """ Конвертируем рубли в доллары. """
    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    result = int(amount * rate)
    return result


def create_stripe_price(amount, stripe_product_id):
    """ Создаем цену. """
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Payment"},
        product=stripe_product_id,
    )


def create_stripe_session(price):
    """ Создаем сессию. """
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
