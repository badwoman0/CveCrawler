from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
chrome_options = Options()
chrome_options.add_argument('--headless')


# print(cve_informations.text)
# print(type(cve_informations.text))


def getInfor(page: int) -> dict:
    """爬取第一层级的漏洞信息，无需点击进入详细信息界面"""
    cveInfoList = []


    url = "https://avd.aliyun.com/nvd/list?type=WEB%E5%BA%94%E7%94%A8&page={}".format(page)
    browser = webdriver.Chrome(executable_path="/Users/badwoman/OpenSource/chrome/chromedriver", chrome_options=chrome_options)
    browser.get(url)
    
    time.sleep(3)
    for line in range (1,31):
        cveInfoDict = {
        "cve_code": "",
        "cve_name": "",
        "cwe": "",
        "foundtime": "",
        "details_href": "",
        "aliyunscore": ""}
        cveInfoDict["cve_code"] = browser.find_element(By.CSS_SELECTOR, "body > main > div > div > div.my-3.px-3.pt-2.bg-white.rounded.shadow-sm.table-responsive > table > tbody > tr:nth-child({}) > td:nth-child(1)".format(line)).text
        cveInfoDict["cve_name"] = browser.find_element(By.CSS_SELECTOR, "body > main > div > div > div.my-3.px-3.pt-2.bg-white.rounded.shadow-sm.table-responsive > table > tbody > tr:nth-child({}) > td:nth-child(2)".format(line)).text
        cveInfoDict["cwe"] = browser.find_element(By.CSS_SELECTOR, "body > main > div > div > div.my-3.px-3.pt-2.bg-white.rounded.shadow-sm.table-responsive > table > tbody > tr:nth-child({}) > td:nth-child(3)".format(line)).text
        cveInfoDict["foundtime"] = browser.find_element(By.CSS_SELECTOR, "body > main > div > div > div.my-3.px-3.pt-2.bg-white.rounded.shadow-sm.table-responsive > table > tbody > tr:nth-child({}) > td:nth-child(4)".format(line)).text
        a = browser.find_element(By.CSS_SELECTOR,"body > main > div > div > div.my-3.px-3.pt-2.bg-white.rounded.shadow-sm.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(1) > a")
        cveInfoDict["details_href"] = a.get_attribute("href")
        cveInfoList.append(cveInfoDict)

    browser.quit()
    return cveInfoList



def getScore(href) -> float:
    """通过href链接爬取漏洞详细信息"""
    return 0


def main():
    maxPages = 100
    for page in range(0, maxPages):
        a = 1
    return 0


# chrome 版本为108.0.5359.124 chromedirver 108.0.5359.124


if __name__ == "__main__":
    for page in range(1,794):
        print("start crawl page {}".format(page))
        temp_list =getInfor(page)
        with open ("cveInfo.json","a+",encoding="utf-8") as f:
            json.dump(temp_list, f ,ensure_ascii=False)
