"""Behave environment: starts / stops the Selenium browser"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

WAIT_SECONDS = int(os.getenv("WAIT_SECONDS", "30"))
BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")


def before_all(context):
    """Executed once before all tests"""
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(context.wait_seconds)
    context.config.setup_logging()


def after_all(context):
    """Executed after all tests"""
    context.driver.quit()
