# import requests
#
# def get_btc():
#     url = 'https://yobit.net/api/2/btc_usd/ticker'
#     responce = requests.get(url).json()
#     print(responce)
#     price = responce['ticker']['last']
#     return str(price) + ' usd'
#
#
# print(get_btc())

from selenium import webdriver

def getFullTrack(trackNum):

    chromedriver = "/Users/maks/PycharmProjects/Bot_empty/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://track24.ru/")
    window_before = driver.window_handles[0]

    window_before_title = driver.title
    print("Сайт:",window_before_title)


    track = driver.find_element_by_xpath("//*[@id='inputTrackCode']")
    track.send_keys(trackNum)

    input_number_value = track.get_attribute('value')
    print ("Трэк-код: " + input_number_value + "\n")


    button = driver.find_element_by_xpath("//*[@id='trackingButton']")
    button.click()
    check = driver.find_elements_by_xpath("//*[@id='trackingInfoEvents']/div")
    status = []

    for i in check:
        status.append((i.text).split("\n"))

    textMes = '\u2705' + trackNum + "\nИстория передвижений:"

    for j in status:
        textMes += "\n"
        for i in range(12):
            textMes += '\u3030'
        textMes += "\n"
        textMes += '\n'.join(j)

    driver.quit()

    return textMes


def getTrack(trackNum):

    chromedriver = "/Users/maks/PycharmProjects/Bot_empty/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://track24.ru/")
    window_before = driver.window_handles[0]

    window_before_title = driver.title
    print("Сайт:",window_before_title)


    track = driver.find_element_by_xpath("//*[@id='inputTrackCode']")
    track.send_keys(trackNum)

    input_number_value = track.get_attribute('value')
    print ("Трэк-код = " + input_number_value + "\n")


    button = driver.find_element_by_xpath("//*[@id='trackingButton']")
    button.click()
    check = driver.find_elements_by_xpath("//*[@id='trackingInfoEvents']/div")
    status = []
    counter = 1

    for i in check:
        counter += 1

    coun = 1
    for i in check:
        coun += 1
        if coun == counter:
            status.append((i.text).split("\n"))

    textMes = '\u2705' + trackNum + "\nПоследнее изменение посылки:"

    for j in status:
        textMes += "\n"
        for i in range(12):
            textMes += '\u3030'
        textMes += "\n"
        textMes += '\n'.join(j)


    driver.quit()

    return textMes


def waitTrack(trackNum):
    textMes = '\U0001F4E6' + trackNum + "\n" + '\U0001F50D' + "Идет проверка статуса посылки.\n" + "Подождите...\n"

    return textMes
# print(getFullTrack("UR365127905CN"))
