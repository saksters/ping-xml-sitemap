import requests
import csv

parsed_url = 'https://www.example.com/sitemap.xml'
parsed_url_response = requests.get(parsed_url)

bing_response = requests.get('http://www.bing.com/webmaster/ping.aspx?siteMap='+parsed_url)
google_response = requests.get('http://www.google.com/ping?sitemap='+parsed_url)
if bing_response.status_code == 200:
    print(parsed_url+": 200 - Bing Ping Successful")
else:
    print(parsed_url+": Error - Bing Ping Failed")

if google_response.status_code == 200:
    print(parsed_url+": 200 - Google Ping Successful")
else:
    print(parsed_url+": Error - Google Ping Failed")