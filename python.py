from seleniumwire import webdriver
from seleniumwire.utils import decode
import json

def get_items():
    searchsite = 'https://www.vinted.com/catalog?search_text=adidas&order=newest_first'
    driver = webdriver.Chrome()
    driver.get(searchsite)
    for request in driver.requests:
        if request.response:
            if 'api/v2/catalog/items?' in request.url:
                response = request.response
                body = decode(response.body, response.headers.get('Content-Encoding', 'identity'))
                body_content = body.decode('utf-8')
                body_content = json.loads(body_content)
                with open("parsedFiles.json", "w") as write_file:
                    json.dump(body_content, write_file, indent=4)


print('ПРОГРАММА ПАРСИТСЯ. ПОЖАЛУЙСТА, НЕ ЗАКРЫВАЙТЕ БРАУЗЕР.')
get_items()
print('Готово!')