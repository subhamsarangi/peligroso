from django.utils.text import slugify
import random
import string

object_statuses = (
    ('act', 'active'),
    ('inc', 'inactive'),
    ('del', 'delete'),
)

reading_statuses = (
    ('10', 'started'),
    ('11', 'halfway or more'),
    ('12', 'finished'),
    ('13', 'cancelled'),
    ('14', 'paused'),
    ('15', 'restarted'),
    ('21', 'planned'),
    
)

def generate_unique_slug(value, length=6):
    unique_slug = slugify(value)
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    unique_slug += f"-{suffix}"
    return unique_slug