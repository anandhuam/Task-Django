# products/management/commands/load_product_data.py
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Load product data'

    def handle(self, *args, **options):
        products = Product.objects.all()
        for product in products:
            self.stdout.write(f"Product: {product.name} - ${product.price:.2f}")
