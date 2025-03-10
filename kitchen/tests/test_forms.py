from django.test import TestCase
from kitchen.forms import (
    CookSearchForm,
    DishSearchForm,
    DishTypeSearchForm
)


class SearchFormTestCase(TestCase):

    def test_search_form(self):
        form_dish_type = {
            "name": "Test Name"
        }
        form = DishTypeSearchForm(data=form_dish_type)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_dish_type)

        form_dish = {
            "name": "Test Model"
        }
        form = DishSearchForm(data=form_dish)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_dish)

        form_cook = {
            "username": "Test Username"
        }
        form = CookSearchForm(data=form_cook)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_cook)
