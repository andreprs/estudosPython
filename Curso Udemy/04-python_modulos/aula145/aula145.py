from pathlib import Path
from shutil import ExecError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# caminho do arquivo main (arquivo que está sendo executado)
ROOT_FOLDER  = Path(__file__).parent.parent
# caminho do driver de navegador (nesse caso, navegador chrome)
CHROME_DRIVER_PATH = ROOT_FOLDER / 'chromedriver.exe'


#inicialização do browser com selenium
def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    chrome_service = Service(executable_path=CHROME_DRIVER_PATH,)
    
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )
    
    return browser


if __name__ == '__main__':
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)
    
    # acessando o github 
    browser.get('https://www.github.com')
    
    try:
        # encontrando o botão 'Sing in' pelo nome
        btn_sign_in = browser.find_element(By.LINK_TEXT, 'Sign in')
        btn_sign_in.click()  # clicando no botão após encontrar

    except Exception as erro:
        print(f'Erro: {erro}')
    
    try:
        # encontrando os campos de email e senha e fazendo o input
        btn_login = browser.find_element(By.NAME, 'commit')  # encontando o botão de fazer login
        input_email = browser.find_element(By.ID, 'login_field')
        input_email.send_keys('andreprasel@gmail.com')  # substitua esse campo com o seu email de usuário
        
        input_password = browser.find_element(By.ID, 'password')
        input_password.send_keys('553@cinco')  # substitua esse campo com a sua senha de usuário
        
        sleep(3)
        btn_login.click()  # clicando no botão de fazer login
        
    except Exception as erro:
        print(f'Erro: {erro}')
    
    try:
        # clicando no botão de perfil para encontrar a opção de 'Sign Out'
        btn_menu = browser.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex')
        btn_menu.click()
        
        sleep(3)
        
        # encontrando a opção 'Sign Out' e clicando nela para deslogar da conta
        btn_sign_out = browser.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
        btn_sign_out.click()
        
    except Exception as erro:
        print(f'Erro: {erro}')

    sleep(10)
    browser.quit()
