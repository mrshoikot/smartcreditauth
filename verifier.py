from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def verify(username, password):

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)



    driver.get("https://www.smartcredit.com/login")

    username_field = driver.find_element(by=By.NAME ,value="j_username")
    password_field = driver.find_element(by=By.NAME ,value="j_password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    driver.find_element(by=By.NAME, value="loginbttn").click()

    url = driver.current_url

    portions = url.split('/')


    try:
        if 'member' in portions and 'home' in portions:
            return 1


        # convert all query params to dict
        params = url.split('?')[1]
        params = params.split('&')
        params = [q.split('=') for q in params]
        params = {q[0]: q[1] for q in params}


        if 'error' in params and params['error'] == 'invalid-login':
            return 0
    except Exception as e:
        print(e)


    return -1