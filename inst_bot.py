from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from set_data import username, password, hashtags, massages
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import random
import re



class InstagramBot():
    """Instagram Bot на Python by PythonToday"""

    def __init__(self, username, password, hashtags, massages):

        self.username = username
        self.password = password
        self.brovser = webdriver.Chrome("../insta/chromedriver")
        self.hashtags = hashtags
        self.massages = massages

    # метод для закрытия браузера
    def close_browser(self):

        self.brovser.close()
        self.brovser.quit()

    # метод логина
    def login(self):

        brovser = self.brovser
        brovser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = brovser.find_element(By.CSS_SELECTOR, '[name="username"]')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = brovser.find_element(By.CSS_SELECTOR, '[name="password"]')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

    # метод ставит лайки по hashtag
    def like_photo_by_hashtag(self):
        for hashtag in self.hashtags[0:1]:
            brovser = self.brovser
            brovser.maximize_window()
            brovser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(5)
            # post_count = brovser.find_element(By.CSS_SELECTOR, '[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1chd833 x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]').text
            # numbers = re.findall(r'\d+\.?\d*', post_count)
            # print(numbers)
            # time.sleep(5)
            # d = int(''.join(numbers))

            # loops_count = int(d / 12)
            # for i in range(0, loops_count):
            for i in range(0, 2):
                brovser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 5))

            hrefs = brovser.find_elements(By.TAG_NAME, 'a')
            posts = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
            list_users = []

            for url in posts[10:15]:
                try:
                    brovser.get(url)
                    time.sleep(2)
                    usrer = brovser.find_element(By.CSS_SELECTOR, '[class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye xwhw2v2 xl56j7k x17ydfre x1f6kntn x2b8uid xlyipyv x87ps6o x14atkfc x1d5wrs8 x972fbf xcfux6l x1qhh985 xm0m39n xm3z3ea x1x8b98j x131883w x16mih1h xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xjbqb8w x1n5bzlp xqnirrm xj34u2y x568u83 x3nfvp2"]').get_attribute('href')
                    like_button = brovser.find_element(By.CLASS_NAME, '_aamw')
                    ActionChains(brovser).click(like_button).perform()
                    time.sleep(3)
                    # brovser.refresh()
                    # time.sleep(3)
                    coment_input = brovser.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Добавьте комментарий..."]').click()
                    
                    time.sleep(2)
                    coment_input = brovser.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Добавьте комментарий..."]')
                    coment_input.send_keys(self.massages)
                    time.sleep(2)
                    coment_input.send_keys(Keys.ENTER)
                    list_users.append(usrer)

                except Exception as er:
                    print(er)
                    print(list_users)

    # метод проверяет по xpath существует ли элемент на странице
    def xpath_exists(self, url):

        brovser = self.brovser
        try:
            brovser.find_element(url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    # метод ставит лайк на пост по прямой ссылке
    def put_exactly_like(self, userpost):

        brovser = self.brovser
        brovser.get(userpost)
        time.sleep(4)

        wrong_userpage = "/html/body/div[1]/section/main/div/h2"
        if self.xpath_exists(wrong_userpage):
            print("Такого поста не существует, проверьте URL")
            self.close_browser()
        else:
            print("Пост успешно найден, ставим лайк!")
            time.sleep(2)

            class_licke = 'xp7jhwk'
            like_button = brovser.find_element(By.CLASS_NAME, {class_licke})
            time.sleep(3)
            ActionChains(brovser).click(like_button).perform()
            time.sleep(2)

            print(f"Лайк на пост: {userpost} поставлен!")
            self.close_browser()

    # метод ставит лайки по ссылке на аккаунт пользователя
    def put_many_likes(self, userpage):

        brovser = self.brovser
        brovser.get(userpage)
        time.sleep(4)

        wrong_userpage = "/html/body/div[1]/section/main/div/h2"
        if self.xpath_exists(wrong_userpage):
            print("Такого пользователя не существует, проверьте URL")
            self.close_browser()
        else:
            print("Пользователь успешно найден, ставим лайки!")
            time.sleep(2)

            posts_count = int(brovser.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span").text)
            loops_count = int(posts_count / 12)
            print(loops_count)

            posts_urls = []
            for i in range(0, loops_count):
                hrefs = brovser.find_elements(By.TAG_NAME, 'a')
                hrefs = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

                for href in hrefs:
                    posts_urls.append(href)

                brovser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(2, 4))
                print(f"Итерация #{i}")

            file_name = userpage.split("/")[-2]

            with open(f'{file_name}.txt', 'a') as file:
                for post_url in posts_urls:
                    file.write(post_url + "\n")

            set_posts_urls = set(posts_urls)
            set_posts_urls = list(set_posts_urls)

            with open(f'{file_name}_set.txt', 'a') as file:
                for post_url in set_posts_urls:
                    file.write(post_url + '\n')

            with open(f'{file_name}_set.txt') as file:
                urls_list = file.readlines()

                for post_url in urls_list[0:6]:
                    try:
                        brovser.get(post_url)
                        time.sleep(2)

                        like_button = "/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button"
                        brovser.find_element(By.XPATH, {like_button}).click()
                        # time.sleep(random.randrange(80, 100))
                        time.sleep(2)

                        print(f"Лайк на пост: {post_url} успешно поставлен!")
                    except Exception as ex:
                        print(ex)
                        self.close_browser()

            self.close_browser()


my_bot = InstagramBot(username, password, hashtags, massages)
my_bot.login()
my_bot.like_photo_by_hashtag()
my_bot.close_browser()
