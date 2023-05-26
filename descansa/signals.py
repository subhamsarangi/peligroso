from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Author
from .utils import generate_unique_slug

@receiver(pre_save, sender=Author)
def author_signal(sender, instance, **kwargs):
    if not instance.slug:
        instance.status = 'act'
        instance.slug = generate_unique_slug(str(instance))
