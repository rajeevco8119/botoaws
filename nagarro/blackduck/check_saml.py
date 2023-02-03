import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

driver = webdriver.Chrome(desired_capabilities=caps)
url = "https://sca.assaabloy.net/"
driver.get(url)
for entry in driver.get_log('browser'):
    print(entry)

# time.sleep(10)
# driver.close()

# O/P format
# {'level': 'SEVERE', 'message': 'https://sca.assaabloy.net/api/current-user - Failed to load resource: the server responded with a status of 401 ()', 'source': 'network', 'timestamp': 1675423106876}
# {'level': 'SEVERE', 'message': 'https://sca.assaabloy.net/favicon.ico - Failed to load resource: the server responded with a status of 404 ()', 'source': 'network', 'timestamp': 1675423107483}
# {'level': 'SEVERE', 'message': 'https://login.microsoftonline.com/favicon.ico - Failed to load resource: the server responded with a status of 404 (Not Found)', 'source': 'network', 'timestamp': 1675423109140}
