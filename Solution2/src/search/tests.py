from django.test import TestCase
from django.urls import resolve
from search.views import search_page,get_json_data, search
from django.http import HttpRequest


class SearchPageTest(TestCase):

	def test_root_url_resolves_to_search_page_view(self):
		found = resolve('/search/')
		self.assertEqual(found.func, search_page)

	def test_search_page_returns_correct_html(self):
		request = HttpRequest()
		response = search_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>RolePoint App</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))

	def test_get_json_data_returns_correct_data(self):
		response = get_json_data()
		self.assertTrue(dir.__class__, response.__class__)

	def test_search_name_should_return_correct_data(self):
		request = HttpRequest()
		response = search(request, 'david')
		self.assertIn( 'david', str(response.content).lower())

	def test_search_company_name_should_return_correct_data(self):
		request = HttpRequest()
		response = search(request, 'vitae')
		self.assertIn( 'vitae', str(response.content).lower())
