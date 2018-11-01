from selenium import webdriver
from selenium import webdriver
from time import sleep
from pprint import pprint
import pandas as pd



def scrape():
    for p in driver.find_elements_by_xpath('//div[@class="list-item flex flex-adapt"]'):
        link = p.find_element_by_xpath('.//a[contains(@href, "products")]')
        price = p.find_element_by_xpath('.//div[@class="list-item-price"]').text
        brand = p.find_element_by_xpath('.//span[@itemprop="brand"]').text
        name = p.find_element_by_xpath('.//span[@itemprop="name"]').text

        try:
            clearance = p.find_element_by_xpath('.//div[contains(text(), "Clearance")]')
            clearance = 'Clearanced Item'
        except:
            clearance = 'Regular Item'

        try:
            stock_status = p.find_element_by_xpath('.//div[contains(text(), "Out of stock")]')
            stock_status = 'Out of stock'
        except:
            stock_status = 'In stock'

        item = {
            'link': link.get_attribute('href'),
            'price': price,
            'brand': brand,
            'name': name,
            'clearance': clearance,
            'stock status': stock_status,
        }
        prod_info.append(item)
    return True


if __name__ == '__main__':
    prod_info = []
    search_term = 'gloves'
    driver = webdriver.Chrome()
    url = 'https://www.farmandfleet.com/s/?keyword={}&pg={}'

    for i in range(1,8):
        driver.get(url.format(search_term.replace(' ', '%20'),i))
        sleep(2)
        scrape()

    driver.quit()
    df = pd.DataFrame(prod_info)
    df.to_excel('Blains_Products_{}.xlsx'.format(search_term), index=False)
