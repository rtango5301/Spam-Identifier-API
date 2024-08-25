from django.core.management.base import BaseCommand
from faker import Faker
from api.models import User, Contact

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create 10 users
        for _ in range(10):
            user = User.objects.create_user(
                phone_number=fake.phone_number(),
                name=fake.name(),
                password='password',
                email=fake.email()
            )
            user.save()

        # Create 50 contacts
        for _ in range(50):
            contact = Contact(
                name=fake.name(),
                phone_number=fake.phone_number(),
                marked_as_spam=fake.boolean(),
                spam_reports=fake.random_int(min=0, max=10)
            )
            contact.save()
