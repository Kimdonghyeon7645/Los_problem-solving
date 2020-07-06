import requests

url = 'https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php'
print(requests.get(url).text)