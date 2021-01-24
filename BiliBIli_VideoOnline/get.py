import pymysql
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("D:\\Utils\\webDriver\\chromedriver_win32\\chromedriver.exe")
wait = WebDriverWait(browser, 10)


def get_data():
    try:
        browser.get("https://www.bilibili.com/video/BV1Eb411u7Fw?from=search&seid=9573459907114273103")

        # 直到刷新出元素
        result = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.bilibili-player-video-info-people-number'))
        )
        return result.text
    except TimeoutException:
        print("超时，重新请求...")
        return get_data()  # 重新请求


sql = "insert into bilibili (data,time,day,mouth,year) values({0},{1},{2},{3},{4})"


# 将数据存入数据库
def push(data):
    # 获得时间信息
    year = time.strftime("%Y", time.localtime())
    mouth = time.strftime("%m", time.localtime())
    day = time.strftime("%d", time.localtime())
    hour = time.strftime("%H", time.localtime())

    # 连接到Demo数据库
    db = pymysql.connect("192.168.1.103", 'root', '4682327', "Demo")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql.format(data, hour, day, mouth, year))
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()


def main():
    # print(get_data())
    push(get_data())


if __name__ == '__main__':
    main()
