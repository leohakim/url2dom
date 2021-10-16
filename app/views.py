import datetime

import validators
from flask import request
from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.chrome.options import Options

from app import app

executable = r'/usr/bin/chromedriver'

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--disable-infobars")
opts.add_argument("--start-maximized")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument("--disable-gpu")


@app.route('/')
def home():
    with webdriver.Chrome(options=opts, executable_path=executable) as browser:
        url = request.args.get('url')
        xpath = request.args.get('xpath')
        if not url or not validators.url(url):
            return "URL not valid", 400
        browser.get(url)
        if not xpath:
            return {
                "datetime": datetime.datetime.now(),
                "data": browser.page_source,
                "status": "Ok",
            }
        if xpath:
            try:
                data = browser.find_element_by_xpath(f"{xpath}")
                if data:
                    return {
                        "status": "Okaaa",
                        "data": data.text
                    }
            except InvalidSelectorException as e:
                return f"{e}", 400
