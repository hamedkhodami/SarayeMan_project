from django.test import TestCase
from .models import PropertyModel
# Create your tests here.


class PropertyModelTest(TestCase):

    def setUp(self):
        PropertyModel.objects.create(
            title="Test Property",
            description="Test description",
            price=1000000,
            address="Test Address",
            area=120
        )

    def test_negative_price(self):
        properties=PropertyModel.objects.get(title="Test Property")
        self.assertEqual(properties.price,1000000)
        self.assertEqual(properties.area,120)

    def test_negative_price(self):

        with self.assertRaises(ValueError):
            properties=PropertyModel(
            title="Invalid Property",
            description="Test description",
            price=-1000,
            address="Test Address",
            area=120
            )
        properties.full_clean()
        properties.save()