from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):

    """
    Creates products
    """

    def handle(self, *args, **options):
        self.stdout.write("Creates products")
        products_names = [
            "Laptop",
            "Desctop",
            "Smartphone",
        ]
        for products_name in products_names:
            product, created = Product.objects.get_or_create(name=products_name)
            self.stdout.write(f"Created product {products_name}")
        self.stdout.write(self.style.SUCCESS("Products created"))
