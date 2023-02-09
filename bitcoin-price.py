import json
import requests
from win10toast import ToastNotifier
import time

t = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=gbp").text
t = json.loads(t)
price = str(t["bitcoin"]["gbp"])

toast = ToastNotifier()
toast.show_toast("Bitcoin price", price, duration = 5)
time.sleep(20)
