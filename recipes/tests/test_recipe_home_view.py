from unittest.mock import patch

from django.urls import resolve, reverse

from recipes.views import site

from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func.view_class, site.RecipeListViewHome)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode(encoding='utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        # check if one recipe exist
        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_publisehd(self):
        # test recipe is_published False dont show
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        # check if one recipe exist
        self.assertIn(
            'No recipes found here',
            response.content.decode(encoding='utf-8')
        )

    @patch('recipes.views.site.PER_PAGE', new=2)
    def test_recipe_home_is_paginated(self):
        self.make_recipe_in_batch(qtd=10)

        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes']
        paginator = recipes.paginator

        self.assertEqual(paginator.num_pages, 5)

    def test_invalid_page_query_uses_page_one(self):
        self.make_recipe_in_batch(qtd=8)

        with patch('recipes.views.site.PER_PAGE', new=3):
            response = self.client.get(reverse('recipes:home') + '?page=12A')
            self.assertEqual(
                response.context['recipes'].number,
                1
            )
            response = self.client.get(reverse('recipes:home') + '?page=2')
            self.assertEqual(
                response.context['recipes'].number,
                2
            )
            response = self.client.get(reverse('recipes:home') + '?page=3')
            self.assertEqual(
                response.context['recipes'].number,
                3
            )
