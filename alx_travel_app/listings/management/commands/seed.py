from django.core.management.base import BaseCommand
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        from listings.models import Listing  # ✅ Safe import here

        fake = Faker()
        for _ in range(10):
            Listing.objects.create(
                title=fake.company(),
                description=fake.paragraph(),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 300), 2),
                available=True
            )
        self.stdout.write(self.style.SUCCESS(
            "Successfully seeded 10 listings."))
