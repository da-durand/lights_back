from django.core.management.base import BaseCommand, CommandError
from light.models import Light
import random

class Command(BaseCommand):

    def handle(self, *args, **options):

        for i in range(100):
            random_number = random.randint(0,16777215)
            hex_number = str(hex(random_number))
            hex_number ='#'+ hex_number[2:]

            choice = [True, False]

            Light.objects.create(activate=random.choice(choice), color=hex_number)