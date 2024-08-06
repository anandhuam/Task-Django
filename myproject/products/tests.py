# products/tests.py
from django.core.management import call_command
from django.test import TestCase
from io import StringIO
from products.models import Product

class DataLoadingTests(TestCase):

    def setUp(self):
        Product.objects.create(name='Test Product', price=10.00)

    def test_load_product_data_command(self):
        out = StringIO()
        call_command('load_product_data', stdout=out)
        output = out.getvalue()
        self.assertIn("Product: Test Product - $10.00", output)
