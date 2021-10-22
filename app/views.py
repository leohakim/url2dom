import datetime

import validators
from flask import request, jsonify
from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException, WebDriverException
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


@app.route('/', methods=['POST'])
def home():
    url = request.json.get('url')
    xpath = request.json.get('xpath')
    _datetime = datetime.datetime.now().isoformat()
    if not url or not validators.url(url):
        return {
                   "datetime": _datetime,
                   "status": "Error",
                   "error": "URL not valid"
               }, 400
    with webdriver.Chrome(options=opts, executable_path=executable) as browser:
        try:
            browser.get(url)
        except WebDriverException as e:
            return {
                       "datetime": _datetime,
                       "status": "Error",
                       "error": f"{e}"
                   }, 400
        if not xpath:
            return {
                "datetime": _datetime,
                "status": "Ok",
                "data": browser.page_source,
            }
        data = dict()
        all_failed = True
        for element in xpath:
            try:
                value = browser.find_element_by_xpath(f"{element}").text
                all_failed = False
            except (InvalidSelectorException, NoSuchElementException) as e:
                value = f"{e}"
            data.update({element: value})

        retorno = {
            "datetime": _datetime,
            "status": "Error" if all_failed else "Ok",
            "data": data
        }

        return jsonify(retorno)
