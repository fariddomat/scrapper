import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep
# import xlsxwriter module
import xlsxwriter
 
workbook = xlsxwriter.Workbook('scrape.xlsx')
worksheet = workbook.add_worksheet("My sheet")

cookies = {
    '_fbp': 'fb.1.1664636081548.2111463019',
    '_ga': 'GA1.2.1115068566.1664636087',
    'XSRF-TOKEN': 'eyJpdiI6IloybllzRkE5RlpVS1wvOGVCZXlzRFwvZz09IiwidmFsdWUiOiI1djdxck5UTG0wUXl1b3ZibWJYRVliUXhyTlwvaFRCNTE3OEhGS2FkcnVDdlE1aHpyNUtPNW0xb0U2WndjWGhGNUlVQnhyVVUwSW1jczFkd3ZtdnVtNVEwVnlLNEZxT2NiTWlGemFyaERHVDFFelZUWVpoZ215bWN1VEJ4djVDb00iLCJtYWMiOiJiZTY3ODUyNzM1YzQwYjM3ZWE1OWIwNjYxMGExZGM0YzE5Nzk4NTA1ZDFiYThkOTRlZTY3ZWE0ZjJlZDY0MDJmIn0%3D',
    'm5azn_session': 'eyJpdiI6IlErTHFRYjM5VWhkNVRsT1ZFUWpZRnc9PSIsInZhbHVlIjoiRzh1OTVuMU82RDZCYlwvSkZ0dlNzaHVEZkFVRWZKdzFET1V4TktxcUc3VlJySDZOYTFEdkw1MVwvZnpkVFhtdWxsZkg5WjRGNUxxc0tkSVVlTGtFVldKK3pWRURKdjZvT0htcThIUGZIa1wvT3NLMVwvWmRYdWhSV1JWdWYyck83aGNSIiwibWFjIjoiMzgzODQxNGFhNDAzY2Q4MTVlNTlmYTM5NzVhNDE1OWQ3ZjBlNzBmM2NiOWI1YjgyNjg2YTI2MjQxYjNjODEyZiJ9',
    '_gid': 'GA1.2.1983141179.1665063602',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Alt-Used': 'm5azn.com',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_fbp=fb.1.1664636081548.2111463019; _ga=GA1.2.1115068566.1664636087; XSRF-TOKEN=eyJpdiI6IloybllzRkE5RlpVS1wvOGVCZXlzRFwvZz09IiwidmFsdWUiOiI1djdxck5UTG0wUXl1b3ZibWJYRVliUXhyTlwvaFRCNTE3OEhGS2FkcnVDdlE1aHpyNUtPNW0xb0U2WndjWGhGNUlVQnhyVVUwSW1jczFkd3ZtdnVtNVEwVnlLNEZxT2NiTWlGemFyaERHVDFFelZUWVpoZ215bWN1VEJ4djVDb00iLCJtYWMiOiJiZTY3ODUyNzM1YzQwYjM3ZWE1OWIwNjYxMGExZGM0YzE5Nzk4NTA1ZDFiYThkOTRlZTY3ZWE0ZjJlZDY0MDJmIn0%3D; m5azn_session=eyJpdiI6IlErTHFRYjM5VWhkNVRsT1ZFUWpZRnc9PSIsInZhbHVlIjoiRzh1OTVuMU82RDZCYlwvSkZ0dlNzaHVEZkFVRWZKdzFET1V4TktxcUc3VlJySDZOYTFEdkw1MVwvZnpkVFhtdWxsZkg5WjRGNUxxc0tkSVVlTGtFVldKK3pWRURKdjZvT0htcThIUGZIa1wvT3NLMVwvWmRYdWhSV1JWdWYyck83aGNSIiwibWFjIjoiMzgzODQxNGFhNDAzY2Q4MTVlNTlmYTM5NzVhNDE1OWQ3ZjBlNzBmM2NiOWI1YjgyNjg2YTI2MjQxYjNjODEyZiJ9; _gid=GA1.2.1983141179.1665063602',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


# response = requests.get('https://m5azn.com/ar/orders/180749', cookies=cookies, headers=headers)
# soup = bs(response.content, 'html.parser')
def cfDecodeEmail(encodedString):
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email

URL = 'https://m5azn.com/ar/orders/'
  
# 180749
# Start from the first cell. Rows and
# columns are zero indexed.
row = 0
col = 0
for page in range(14,1000): 
    try:
        # pls note that the total number of
        # pages in the website is more than 5000 so i'm only taking the
        # first 10 as this is just an example
    
        req = requests.get(URL + str(page) + '/', cookies=cookies, headers=headers)
        soup = bs(req.text, 'html.parser')
    
        name = soup.find("td", id="name")
        address = soup.find("td", id="address")
        mobile = soup.find("td", id="mobile")
        total = soup.find("strong", id="total")
        # email = soup.select("[class='__cf_email__']")[-1].get("data-cfemail")
        
        email = cfDecodeEmail(soup.select("[class='__cf_email__']")[-1].get("data-cfemail"))
        i=str(page)
        print(i + " -" + name.text + "-" + email + "-" + address.text + "-" + mobile.text + "-" + total.text)
        
        
        
        worksheet.write(row, col, i)
        worksheet.write(row, col + 1, name.text)
        worksheet.write(row, col + 2, email)
        worksheet.write(row, col + 3, address.text)
        worksheet.write(row, col + 4, mobile.text)
        worksheet.write(row, col + 5, total.text)
        row += 1
    
    # sleep(randint(2,10))
    except:
        print("Not found")
        # do nothing
    
workbook.close()