import time

from selenium import webdriver


def voteforfynn():
    driver = webdriver.Chrome('path/to/chromedriver')
    driver.get('https://www.mtvema.com/de-de/wahl/bestgermanact/')
    time.sleep(5)

    class_names = driver.find_elements_by_class_name(
        'elements-accordion-components-item-styles_item_3UqYKLNwlTA3-XlJkgIjHA')
    myvotes = 0
    k = 0
    for i in class_names:
        #print(k, i)
        k += 1
        if(k == 4):
            fynn = i.find_element_by_class_name("etYaFo")
            driver.execute_script("arguments[0].scrollIntoView();", fynn)
            time.sleep(1)
            while(True):
                fynn.click()
                myvotes += 1
                if(myvotes % 10 == 0):
                    print(myvotes)
                time.sleep(6)
    driver.quit()


voteforfynn()
