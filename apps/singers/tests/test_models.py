from django.test import TestCase
from django.core.exceptions import ValidationError

from singer.models import Singer


class SingerModelTest(TestCase):
    
    def test_cannot_save_singer_without_name(self):
        singer = Singer()
        with self.assertRaises(ValidationError):
            singer.save()
            singer.full_clean() 

    def test_singers_with_same_names_invalid(self):
        singer1 = Singer(
            full_name="Singer"
        )
        singer2 = Singer(
            full_name="Singer"
        )
        singer1.save()
        with self.assertRaises(ValidationError):
            singer2.save()
            singer2.full_clean()

