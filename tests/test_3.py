# import pytest
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# service = Service()
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

# class TestBrowser1(LiveServerTestCase):
#     def test_example(self):
#         driver = webdriver.Chrome()
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title
        
# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Chrome(options=options)
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title

# @pytest.fixture(scope="class")
# def chrome_driver_init(request):
#     options = 