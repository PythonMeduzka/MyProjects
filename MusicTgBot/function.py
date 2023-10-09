from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def downloadingMusic(message, a):
    placeholder_value = "https://open.spotify.com/..../...."
    xp = By.XPATH
    max_wait_time = 60
    driver = webdriver.Edge()
    driver.get('https://spotifydown.com/ru')
    driver.find_element(xp, f"//input[@placeholder='{placeholder_value}']").send_keys(message)
    time.sleep(0.5)
    driver.find_element(xp, "//button[contains(text(), 'Скачать')]").click()
    driver.refresh()
    driver.find_element(xp, f"//input[@placeholder='{placeholder_value}']").send_keys(message)
    driver.find_element(xp, "//button[contains(text(), 'Скачать')]").click()
    time.sleep(0.5)
    driver.find_element(xp, "//button[contains(text(), 'Скачать')]").click()
    while max_wait_time > 0:
        try:
            time.sleep(0.5)
            link_element = driver.find_element(xp, "//a[contains(text(), 'Скачать')]")
            a = driver.find_element(xp, "//img[contains(@class, 'h-48 h-48 sm:w-64 sm:h-64 m-auto')]")
            driver.find_element(xp, "//a[contains(text(), 'Скачать')]").click()
            break
        except:
            max_wait_time -= 0.5
            time.sleep(0.5)
    message = link_element.get_attribute("download")
    a = a.get_attribute("src")
    time.sleep(3)
    driver.close()
    return message, a


def downloadPlaylist(playlist_link, playlist_photo):
    placeholder_value = "https://open.spotify.com/..../...."
    xp = By.XPATH
    max_wait_time = 900
    driver = webdriver.Edge()
    driver.get('https://spotifydown.com/ru')
    driver.find_element(xp, f"//input[@placeholder='{placeholder_value}']").send_keys(playlist_link)
    time.sleep(0.5)
    driver.find_element(xp, "//button[contains(text(), 'Скачать')]").click()
    driver.refresh()
    driver.find_element(xp, f"//input[@placeholder='{placeholder_value}']").send_keys(playlist_link)
    driver.find_element(xp, "//button[contains(text(), 'Скачать')]").click()
    time.sleep(1)
    link = playlist_link
    playlist_link = ""
    download_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Скачать')]")
    i = 0
    while i != len(download_buttons):
        print(f"i ===== {i}")
        print(download_buttons)
        download_buttons[i].click()
        print(f"i ===== {i}")
        while max_wait_time > 0:
            try:
                link_element = driver.find_element(xp, "//a[contains(text(), 'Скачать')]")
                a = driver.find_element(xp, "//img[contains(@class, 'h-48 h-48 sm:w-64 sm:h-64 m-auto')]")
                playlist_link = f'{playlist_link}, {link_element.get_attribute("download")}'
                playlist_photo = f'{playlist_photo}, {a.get_attribute("src")}'
                driver.find_element(xp, "//a[contains(text(), 'Скачать')]").click()
                while max_wait_time > 0:
                    try:
                        driver.find_element(xp, "//div[contains(text(), 'Close')]").click()
                        break
                    except:
                        max_wait_time -= 0.5
                        time.sleep(0.5)
                driver.get('https://spotifydown.com/ru')
                driver.get('https://spotifydown.com/ru')
                driver.find_element(xp, f"//input[@placeholder='{placeholder_value}']").send_keys(link)
                driver.find_element(xp, "//button[contains(text(), 'Скачать')]").click()
                time.sleep(8)
                while max_wait_time > 0:
                    try:
                        download_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Скачать')]")
                        break
                    except:
                        max_wait_time -= 0.5
                        time.sleep(0.5)
                time.sleep(1)
                i = i + 1
                break
            except:
                max_wait_time -= 0.5
                time.sleep(0.5)
    time.sleep(1)
    driver.close()
    return playlist_link, playlist_photo
