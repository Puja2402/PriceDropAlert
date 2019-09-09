import requests
from bs4 import BeautifulSoup
import smtplib

URL="https://www.amazon.in/Test-Exclusive-611/dp/B07HGMLBW1/ref=hsx_crw_1389401031_tl_4?pf_rd_p=3e57ae7f-1906-4860-9c24-5582dcc9cbb3&pf_rd_s=merchandised-search-20&pf_rd_t=101&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=ENGRSPKCV4BM3791N06B&pf_rd_r=ENGRSPKCV4BM3791N06B&pf_rd_p=3e57ae7f-1906-4860-9c24-5582dcc9cbb3"
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="productTitle").get_text()
    print(title.strip())
    price=soup.find(id="priceblock_ourprice").get_text()
    conv=float(price[2:4]+price[5:8])
    print(conv)
    if(conv<31000):
        send_mail()

#wslhwhhpwnrjyhtq
def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('baerdo2427@gmail.com','wslhwhhpwnrjyhtq')
    subject='Price fell down!'
    body='Check the amazon link https://www.amazon.in/Test-Exclusive-611/dp/B07HGMLBW1/ref=hsx_crw_1389401031_tl_4?pf_rd_p=3e57ae7f-1906-4860-9c24-5582dcc9cbb3&pf_rd_s=merchandised-search-20&pf_rd_t=101&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=ENGRSPKCV4BM3791N06B&pf_rd_r=ENGRSPKCV4BM3791N06B&pf_rd_p=3e57ae7f-1906-4860-9c24-5582dcc9cbb3'
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail('baerdo2427@gmail.com','ursadodesign@gmail.com',msg)
    print("SENT!")
    server.quit()
check_price()
