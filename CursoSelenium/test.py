from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import(
    frame_to_be_available_and_switch_to_it
)



navegador = Chrome()
wdw = WebDriverWait(navegador, 20)
url = 'https://selenium.dunossauro.live/aula_11_b.html'
navegador.get(url)

navegador.execute_script("window.open('https://selenium.dunossauro.live/aula_11_a.html')")
navegador.execute_script("window.open('https://selenium.dunossauro.live/aula_08_a.html')")
navegador.execute_script("window.open('https://duckduckgo.com/')")





while True:
    if not navegador.window_handles:
        break

navegador.quit()