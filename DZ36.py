import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


URL = "https://folodya.ru/"


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")


items = soup.find_all("div", class_="sofa-card")


data = []

for item in items:
    name = item.find("div", class_="sofa-name").text.strip()
    price_text = item.find("div", class_="sofa-price").text.strip()
    price = int(price_text.replace(" ", "").replace("₽", ""))
    data.append({"Название": name, "Цена": price})


df = pd.DataFrame(data)


df.to_csv("divan_prices.csv", index=False)


average_price = df["Цена"].mean()
print(f"Средняя цена на диваны: {average_price:,.0f} ₽")


plt.hist(df["Цена"], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel("Цена (₽)")
plt.ylabel("Количество диванов")
plt.title("Распределение цен на диваны")
plt.grid(True)
plt.show()
