from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Sum
from store.models import CartItem, Product, Customer, Order, OrderItem, Address


def say_hello(request):
    # keyword=value
    queryset = Product.objects.filter(title__icontains="coffee")

    # Level 1 – Basic Filters
    # Get all products with inventory less than 10.
    low_stock = Product.objects.filter(inventory__lt=10)

    # Retrieve all customers with membership = GOLD.
    gold_members = Customer.objects.filter(membership__icontains="g")

    # Get all orders that are still pending.
    pending_orders = Order.objects.filter(payment_status__contains="P")

    # Level 2 – Lookups
    # Find all customers whose first name starts with “J”.
    named_customers = Customer.objects.filter(first_name__startswith="J")

    # Get all products priced between 20 and 50.
    products_range = Product.objects.filter(unit_price__range=(20, 50))

    # Retrieve all orders placed in 2021.
    orders_year = Order.objects.filter(placed_at__year=2021)

    # Get all customers without a birthdate.
    customers_birth = Customer.objects.filter(birth_date__isnull=True)

    # Level 3 – Relationships
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

    # Level 4 – Complex Queries (Q Objects)
    # Get all customers who are GOLD OR born before 1990.
    gold_customers = Customer.objects.filter(
        Q(membership=Customer.MEMBERSHIP_GOLD) | Q(birth_date__lt="1990-01-01")
    )

    # Retrieve all products that are out of stock OR priced below 5.
    cheap_products = Product.objects.filter(Q(inventory=0) | Q(unit_price__lt=5))

    # Find all orders that are (pending OR failed) AND belong to a GOLD member.
    statuses = [Order.PAYMENT_STATUS_PENDING, Order.PAYMENT_STATUS_FAILED]
    gold_orders = Order.objects.filter(
        payment_status__in=statuses,
        customer__membership=Customer.MEMBERSHIP_GOLD,
    )

    # Level 5 – Aggregations + Filtering
    # Find all customers who have never placed an order.
    new_customers = Customer.objects.filter(order__isnull=True)

    # Get all products ordered more than 10 times (total quantity).
    large_orders = Product.objects.annotate(
        total_sold=Sum("orderitem__quantity")
    ).filter(total_sold__gt=10)

    # Retrieve the most recent order for each customer.
    recent_orders = Order.objects.order_by("customer", "-placed_at").distinct()

    # Get the top 5 best-selling products.
    best_sellers = Product.objects.annotate(
        total_sold=Sum("orderitem__quantity")
    ).order_by("-total_sold")[:5]

    # Select products that have been ordered and sort them by title
    products_queryset = Product.objects.filter(
        id__in=(OrderItem.objects.values("product_id").distinct())
    ).order_by("title")

    return render(
        request,
        "hello.html",
        {
            "name": "Shamonti",
            "orders": list(expensive_orders),
            "products": list(products_queryset),
        },
    )
