from time import sleep 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings 
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

warnings.simplefilter("ignore")
url = f'https://cdn.botpress.cloud/webchat/v1/index.html?options=%7B%22config%22%3A%7B%22composerPlaceholder%22%3A%22Listening...%22%2C%22botConversationDescription%22%3A%22AI%20Assistance%22%2C%22botId%22%3A%221f0ce907-6173-4d4e-9392-7fd25fc8252a%22%2C%22hostUrl%22%3A%22https%3A%2F%2Fcdn.botpress.cloud%2Fwebchat%2Fv1%22%2C%22messagingUrl%22%3A%22https%3A%2F%2Fmessaging.botpress.cloud%22%2C%22clientId%22%3A%221f0ce907-6173-4d4e-9392-7fd25fc8252a%22%2C%22webhookId%22%3A%229c6cdb70-4d84-4568-88d4-def243833393%22%2C%22lazySocket%22%3Atrue%2C%22themeName%22%3A%22prism%22%2C%22botName%22%3A%22Friday%22%2C%22avatarUrl%22%3A%22https%3A%2F%2Fcdn.vox-cdn.com%2Fthumbor%2F2E78dg_Cpbdh3nv6z0KKhOhYs6c%3D%2F0x0%3A1100x580%2F1200x800%2Ffilters%3Afocal(520x151%3A696x327)%2Fcdn.vox-cdn.com%2Fuploads%2Fchorus_image%2Fimage%2F71921482%2Fbkq6gtrpcnw43vsm5zm62q3z.0.png%22%2C%22stylesheet%22%3A%22https%3A%2F%2Fwebchat-styler-css.botpress.app%2Fprod%2F8d981395-7a94-479d-bee4-0c8a5d16faa6%2Fv83430%2Fstyle.css%22%2C%22frontendVersion%22%3A%22v1%22%2C%22useSessionStorage%22%3Atrue%2C%22enableConversationDeletion%22%3Atrue%2C%22theme%22%3A%22prism%22%2C%22themeColor%22%3A%22%232563eb%22%2C%22chatId%22%3A%22bp-web-widget%22%2C%22encryptionKey%22%3A%22VDolzuA2lS49FKLv4xWZJV39rqVxoq3v%22%7D%7D'
chrome_driver_path = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Enable headless mode (runs Chrome without GUI)
chrome_options.add_argument('--log-level=3')  # Set Chrome log level
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(3)


def click_on_chat_button():
    button = driver.find_element(By.XPATH, '/html/body/div/div/button').click()
    sleep(2)
    while True:
        try:
            loader = driver.find_element(
                By.CLASS_NAME, 'bpw-msg-list-loading')
            is_visible = loader.is_displayed()
            print('Initializing friday...')

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            print('Friday is Initializing.')
            break
        sleep(1)


def sendQuery(text):
    # Find and interact with the textarea element
    textarea = driver.find_element(By.ID, 'input-message')
    textarea.send_keys(text)
    sleep(1)

    send_btn = driver.find_element(By.ID, 'btn-send').click()
    sleep(1)


def isBubbleLoaderVisible():
    print('Friday Is Typing...')
    while True:
        try:
            bubble_loader = driver.find_element(
                By.CLASS_NAME, 'bpw-typing-group')
            is_visible = bubble_loader.is_displayed()

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            print('Friday Is Sending Mesage...')
            break
        sleep(1)


chatnumber = 2


def retriveData():
    print('Retriving Chat...')
    global chatnumber
    sleep(1)
    p = driver.find_element(
        By.XPATH, f'/html/body/div/div/div/div[2]/div[1]/div/div/div[{chatnumber}]/div/div[2]/div/div/div/div/div/p')
    print("\nFriday: " + p.text)
    chatnumber = chatnumber + 2
    return(p.text)


# click_on_chat_button()
# def ai_brain(): 
#     query = input('\nYou: ')
#     sendQuery(query)
#     isBubbleLoaderVisible()
#     retriveData()


# /html/body/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div/p
#/html/body/div/div/div/div[2]/div[1]/div/div/div[4]/div/div[2]/div/div/div/div/div/p
#/html/body/div/div/div/div[2]/div[1]/div/div/div[6]/div/div[2]/div/div/div/div/div/p