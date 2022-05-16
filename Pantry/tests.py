from django.test import TestCase
from Home.models import Recipe
from Pantry.models import Ingredient
from django.contrib.auth.models import User

# Create your tests here.
class PantryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = 'test_user', password = 'abbacadabba')
        login = self.client.login(username = 'test_user', password = 'abbacadabba')
        Ingredient.objects.create(id = 0, name = 'peanut')

    def test_isingredient(self):
        ingred = "peanut"
        user_ingredients = Ingredient.objects.all()
        search_ingredients = user_ingredients.filter(name = ingred)
        self.assertEqual(search_ingredients.exists(), True)

    def test_isnotingredient(self):
        ingred = "p3anut"
        user_ingredients = Ingredient.objects.all()
        search_ingredients = user_ingredients.filter(name = ingred)
        self.assertEqual(search_ingredients.exists(), False)

    def test_blankingredient(self):
        ingred = ""
        user_ingredients = Ingredient.objects.all()
        search_ingredients = user_ingredients.filter(name = ingred)
        self.assertEqual(search_ingredients.exists(), False)

    def test_ischecked(self):
        ingredient = Ingredient.objects.get(id=0)
        self.assertEqual(ingredient.is_checked.count(), 0)
        user = self.user
        ingredient.is_checked.set([user])
        self.assertEqual(ingredient.is_checked.count(),1)
