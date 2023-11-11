from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AdminPageTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Safari()
        admin_user = get_user_model().objects.create_user(
            username='admin',
            password='admin'
        )
        admin_user.is_superuser = True
        admin_user.is_staff= True
        admin_user.save()
        self.browser.get(self.live_server_url + '/admin')
        self.login()

    def tearDown(self):
        self.browser.quit()

    def login(self):
        username_input = self.browser.find_element(By.ID, 'id_username')
        password_input = self.browser.find_element(By.ID, 'id_password')
        username_input.send_keys('admin')
        password_input.send_keys('admin')
        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    def test_models_attached_to_admin_page(self):
        self.assertIn(self.browser.page_source, 'Song')
        self.assertIn(self.browser.page_source, 'Singer')


