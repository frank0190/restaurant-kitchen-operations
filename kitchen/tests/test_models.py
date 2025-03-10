from django.test import TestCase

from kitchen.models import Cook, Dish, DishType


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        dish_type = DishType.objects.create(
            name="bread",
        )

        cook = Cook.objects.create(
            username="Bento",
            first_name="Benny",
            last_name="Hrozhyn",
        )

        dish = Dish.objects.create(
            name="Focaccia",
            description="fizzy and gutsy",
            price="15.00",
            dish_type=dish_type,
        )
        dish.cooks.add(cook)

    def test_dish_type_str(self):
        dish_type = DishType.objects.get(id=1)
        self.assertEqual(str(dish_type),
                         f"{dish_type.name}")

    def test_cook_str(self):
        cook = Cook.objects.get(id=1)
        self.assertEqual(str(cook),
                         f"{cook.username} "
                         f"({cook.first_name} {cook.last_name})")

    def test_dish_str(self):
        dish = Dish.objects.get(id=1)
        self.assertEqual(str(dish), dish.name)
