from os import name
from organizations.models import Organization, BlogAPIKey
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('organization_name', type=str)

        parser.add_argument(
            '--email',
            help='Email required for creating Blog key',
        )

    def handle(self, *args, **options):
        if options["organization_name"].title() == "Blog":
            org = Organization.objects.get_or_create(name=options["organization_name"])
            # Email required for creating Blog key
            api_key_name, key = BlogAPIKey.objects.create_key(
                name=f"Blog {options['email']}", email=options["email"], organization=org[0])
            print("Key Created!")
            print("Name:", api_key_name)
            print("Key:", key)
            print("Copy this key and store it safely. You will not see it again.")
        else:
            raise CommandError("The only valid Organization at this time is 'Blog'.")
