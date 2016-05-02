import os

from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import Client


class Command(BaseCommand):

    OUTPUT_FILE_NAME = 'index.html'
    URL_NAME = 'footer_email'

    def handle(self, *args, **options):
        c = Client()
        response = c.get(reverse(self.URL_NAME))

        if not os.path.isdir(settings.STATIC_ROOT):
            os.makedirs(settings.STATIC_ROOT)

        output_file_path = os.path.join(os.path.dirname(settings.STATIC_ROOT),
                                        self.OUTPUT_FILE_NAME)
        with open(output_file_path, 'w') as output_fh:
            output_fh.write(response.content)
