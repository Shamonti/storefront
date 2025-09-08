from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import CartItem, Product, Customer, Order, OrderItem, Address


def say_hello(request):
    # keyword=value
    queryset = Product.objects.filter(title__icontains="coffee")

    # Get all products with inventory less than 10.
    low_stock = Product.objects.filter(inventory__lt=10)

    # Retrieve all customers with membership = GOLD.
    gold_members = Customer.objects.filter(membership__icontains="g")

    # Get all orders that are still pending.
    pending_orders = Order.objects.filter(payment_status__contains="P")

    # Find all customers whose first name starts with “J”.
    named_customers = Customer.objects.filter(first_name__startswith="J")

    # Get all products priced between 20 and 50.
    products_range = Product.objects.filter(unit_price__range=(20, 50))

    # Retrieve all orders placed in 2021.
    orders_year = Order.objects.filter(placed_at__year=2021)

    # Get all customers without a birthdate.
    customers_birth = Customer.objects.filter(birth_date__isnull=True)

    # Get all products in the Pets collection.
    pet_products = Product.objects.filter(collection__title="Pets")

    # Retrieve all orders that include a product with unit_price > 90.
    expensive_orders = Order.objects.filter(
        orderitem__product__unit_price__gte=90
    ).distinct()

    # Find all addresses for customers with membership = SILVER.
    silver_address = Address.objects.filter(
        customer__membership=Customer.MEMBERSHIP_SILVER
    )

    # Get all cart items for a specific cart (id = 5).
    cart_items = CartItem.objects.filter(cart__id=5).distinct()

    # Find all orders that are (pending OR failed) AND belong to a GOLD member.

    return render(
        request,
        "hello.html",
        {
            "name": "Shamonti",
            "orders": list(expensive_orders),
            "cartItems": list(cart_items),
        },
    )
