import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from django.db import models
from datacenter.models import Passcard 

if __name__ == '__main__':
    active_posts = Passcard.objects.filter(is_active=True)
    print('Всего пропусков:', Passcard.objects.count())
    print('Активных пропусков', len(active_posts))
