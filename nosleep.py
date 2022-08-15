import re
import urllib.request
import warnings
from importlib import reload
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def main(query): 
	try:		
		grab = urllib.request.urlopen('https://domains.tntcode.com/ip/'+ query +'/', timeout=1000).read()
		html = grab.decode('ISO-8859-1')  # encoding may vary!
		res = re.findall('"/domain/(.*?)"', html)
		data = res
		return data

	except Exception as e:
		print("error")
