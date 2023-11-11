import time

from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10


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

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_models_attached_to_admin_page(self):
        self.wait_for(lambda: self.assertIn('Song', self.browser.page_source))
        self.wait_for(lambda: self.assertIn('Singer', self.browser.page_source))

