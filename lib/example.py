from gevent import monkey
monkey.patch_all()
import requests
import gevent
from lxml import etree
 
 
def downloader(img_name, img_url):
    req = requests.get(img_url)
    img_content = req.content
    with open(img_name, "wb") as f:
        f.write(img_content)
 
 
def main():
    r = requests.get('http://www.nsgirl.com/portal.php')
    if r.status_code == 200:
        img_src_xpath = '//div[@id="frameXWswSe"]//div[@class="portal_block_summary"]//li//img/@src'
        s_html = etree.HTML(text=r.text)
        all_img_src = s_html.xpath(img_src_xpath)
 
        count = 0
        for img_src in all_img_src:
            count += 1
            # print(img_src)
            # http://www.nsgirl.com/forum.php?mod=image&aid=342&size=218x285&key=cd6828baf05c305c
            url = 'http://www.nsgirl.com/' + img_src
            gevent.joinall(
                [gevent.spawn(downloader, f"{count}.jpg", url), ]
            )
 
 
if __name__ == '__main__':
    main()