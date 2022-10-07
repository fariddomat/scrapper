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
    'XSRF-TOKEN': 'eyJpdiI6ImhzXC9EOTMzc0hXcTJiOTdmd0tkXC9iQT09IiwidmFsdWUiOiJPbEE1Zk51a2dQellcL0VVcW40RStYOTNpemQ1amZ2V2xvSGZ6RG5paEdleE1KbVhJRFpVTnNzWktEcVRwTElOMHFhQk1xVGFvMFBGaEg1RlJUQkhnUHUwTDlrbFBnOHFmN3hsQVRTais2RlY3UUNVTWpXMHNwYVNhU0htQ2hmYzUiLCJtYWMiOiI5MmFkNTg0MWY2OTEzMTQ2ODZiYmIwYjNmMmExMmI0ZTU0YTU2MTRjZDBjY2I5NDhjMzI0MjA1Y2Q5MGRhNzAxIn0%3D',
    'm5azn_session': 'eyJpdiI6IjRnd1hvajBZTjdNT3cxYTdLTE5GcUE9PSIsInZhbHVlIjoiK2l3eEFxYlMyRDI1TUVHN3NJRElRbUFydk9UTG41eE13QTl1VWl3dDlpXC9qSG93TUdOTjd1UURLUUQrWldDOHcxYUdJV2RLZ09Na3hRQ1VSbzV6cXhrMmprRElHZ2dycWtTYlo3YjNLcWFGc3hCRnhMbkdUME5LZ0hKc1cwT1prIiwibWFjIjoiYWVhNTk0N2MzNTEzN2MzNGI5OTIwNTRlYzBlYjFkMmI4NWE2ZmZjMmZkZWY4ZWYwMjhhZmU1YzUxOTk1MGUwOSJ9',
    '_gid': 'GA1.2.1283812712.1665150316',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Alt-Used': 'm5azn.com',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_fbp=fb.1.1664636081548.2111463019; _ga=GA1.2.1115068566.1664636087; XSRF-TOKEN=eyJpdiI6ImhzXC9EOTMzc0hXcTJiOTdmd0tkXC9iQT09IiwidmFsdWUiOiJPbEE1Zk51a2dQellcL0VVcW40RStYOTNpemQ1amZ2V2xvSGZ6RG5paEdleE1KbVhJRFpVTnNzWktEcVRwTElOMHFhQk1xVGFvMFBGaEg1RlJUQkhnUHUwTDlrbFBnOHFmN3hsQVRTais2RlY3UUNVTWpXMHNwYVNhU0htQ2hmYzUiLCJtYWMiOiI5MmFkNTg0MWY2OTEzMTQ2ODZiYmIwYjNmMmExMmI0ZTU0YTU2MTRjZDBjY2I5NDhjMzI0MjA1Y2Q5MGRhNzAxIn0%3D; m5azn_session=eyJpdiI6IjRnd1hvajBZTjdNT3cxYTdLTE5GcUE9PSIsInZhbHVlIjoiK2l3eEFxYlMyRDI1TUVHN3NJRElRbUFydk9UTG41eE13QTl1VWl3dDlpXC9qSG93TUdOTjd1UURLUUQrWldDOHcxYUdJV2RLZ09Na3hRQ1VSbzV6cXhrMmprRElHZ2dycWtTYlo3YjNLcWFGc3hCRnhMbkdUME5LZ0hKc1cwT1prIiwibWFjIjoiYWVhNTk0N2MzNTEzN2MzNGI5OTIwNTRlYzBlYjFkMmI4NWE2ZmZjMmZkZWY4ZWYwMjhhZmU1YzUxOTk1MGUwOSJ9; _gid=GA1.2.1283812712.1665150316',
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
for page in range(14,180749): 
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
