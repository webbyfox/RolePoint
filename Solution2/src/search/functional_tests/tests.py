from selenium import webdriver
import unittest


class HomepageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.brower.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_homepage_load(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('RolePoint App', self.browser.title)
		self.fail('Finish the Test!')

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')