from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from kitchen.models import DishType, Dish


class DishTypeTestViews(TestCase):

    def setUp(self):

        for number in range(10):
            DishType.objects.create(
                name=f"Dish type {number}"
            )
        self.user = get_user_model().objects.create(
            username="Test",
            password="1qazxsw",
        )
        self.client.force_login(self.user)

    def test_view_pagination_is_5(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(
            len(response.context["dish_type_list"]), 5
        )

    def test_view_correct_template(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "kitchen/dish_type_list.html"
        )

    def test_view_correct_context_data_with_data(self):
        response = self.client.get(reverse(
            "kitchen:dish-type-list"), {"name": "Test Dish Type"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("search_form", response.context)
        self.assertEqual(
            response.context["search_form"].initial["name"],
            "Test Dish Type"
        )

    def test_view_correct_context_data_without_data(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("search_form", response.context)
        self.assertEqual(response.context["search_form"].initial["name"], "")


class DishTestViews(TestCase):

    def setUp(self):
        for number in range(10):
            dish_type = DishType.objects.create(
                name=f"Dish type {number}",            )

            Dish.objects.create(
                name=f"Test Car {number}",
                price="15.00",
                description="zesty and creamy",
                dish_type=dish_type,
            )

        self.user = get_user_model().objects.create(
            username="Test",
            password="1qazxsw",
        )
        self.client.force_login(self.user)

    def test_view_correct_template(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_view_pagination_is_5(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)

        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["dish_list"]), 5)

    def test_view_correct_context_data_with_data(self):
        response = self.client.get(
            reverse("kitchen:dish-list"), {"name": "Test Dish"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("search_form", response.context)
        self.assertEqual(
            response.context["search_form"].initial["name"], "Test Dish"
        )

    def test_view_correct_context_data_without_data(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("search_form", response.context)
        self.assertEqual(response.context["search_form"].initial["name"], "")


class CookTestViews(TestCase):

    def setUp(self):
        user = get_user_model().objects.create(
            username="Test",
            first_name="First name",
            last_name="Last name",
            email="Email",
        )
        self.client.force_login(user)

    def test_view_correct_template(self):
        response = self.client.get(reverse("kitchen:cook-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_view_correct_context_data_with_data(self):
        response = self.client.get(
            reverse("kitchen:cook-list"), {"username": "Test Username"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("search_form", response.context)
        self.assertEqual(
            response.context["search_form"].initial["username"],
            "Test Username"
        )

    def test_view_correct_context_data_without_data(self):
        response = self.client.get(reverse("kitchen:cook-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("search_form", response.context)
        self.assertEqual(
            response.context["search_form"].initial["username"], ""
        )
