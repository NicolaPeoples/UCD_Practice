020000
print(data.text)
data=requests.get("http://api.open-notify.org/astros.json")
print(data.status_code)
print(type(data.text))
data=data.json()
print(data["number"])
print(data)
for p in data["people"]:
 print (p["name"])

