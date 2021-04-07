import requests
data=requests.get("http://api.openweathermap.org/data/2.5/weather?q=Dublin,IE&appid=88a3085f305a4efc221df9c1f1c7430a")
print(data.text)
print(type(data))







