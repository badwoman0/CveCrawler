from bs4 import BeautifulSoup
import requests

#body > main > div > div > div.my-3.px-3.pt-2.bg-white.rounded.shadow-sm.table-responsive > table > tbody

url = "https://avd.aliyun.com/nvd/list?type=WEB%E5%BA%94%E7%94%A8&page=2"

def getInformation(url):
    rawDate = requests.get(url)  
    pageSoup = BeautifulSoup(rawDate.content, 'html.parser')
  
    cves = pageSoup.select("body > main > div > div > div.my-3.px-3.pt-2.bg-white.rounded.shadow-sm.table-responsive > table > tbody > tr:nth-child(1)")
    for i in range(1,4):
        
        informations = [(pt.get_text()).strip() for pt in cves]
    print(len(informations))
    return cves



def click(href):
    aliyunscore = 0
    return aliyunscore

def main():
    maxPage = 10 #可获取
    for page in range(1,maxPage):
        url = "https://avd.aliyun.com/nvd/list?type=WEB%E5%BA%94%E7%94%A8&page={}".format(page)
        

if __name__ == "__main__":
    res = getInformation(url)
