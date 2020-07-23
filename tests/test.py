from django.test import TestCase
from django.urls import resolve
from django.test import Client

class Test(TestCase):

    """
        I was not able to implement Selenium test (Third-party package) due to this issue
        'selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH'

        Due to lack of time I did not get to implement another useful Third-party package - pip install coverage. It is used for measuring
        the effectiveness of tests, showing the percentage of your codebase covered by tests
    """


    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_result_1(self):

        response = self.client.get('/result/?fulltext')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'result.html')

    def test_result_2(self):

        resolver = resolve('/result/')
        self.assertEqual(resolver.view_name, 'result')

    def test_result_3(self):
        c = Client()
        response = c.get('/result/', {'fulltext': '1 2 3 4 5'}, HTTP_X_REQUESTED_WITH = 'XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_result_4(self):
        c = Client()
        input_text = "python manage.py runserver"
        count_text = len(input_text.split())
        response = c.get('/result/', {'fulltext': input_text}, HTTP_X_REQUESTED_WITH = 'XMLHttpRequest')
        self.assertEqual(response.context['count'], count_text)

    def test_result_5(self):
        c = Client()
        input_text = "python manage.py runserver"
        response = c.get('/result/', {'fulltext': input_text}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.context['fulltext'], input_text)
