import requests
from bs4 import BeautifulSoup

README_FILE = "README.md"
START_MARKER = "<!-- NFT_STATS_START -->"
END_MARKER = "<!-- NFT_STATS_END -->"

URL = "https://crystara.trade/marketplace/pixelpulse"

# --- Sayfayı çek ---
try:
    resp = requests.get(URL)
    resp.raise_for_status()
    html = resp.text
except Exception as e:
    print(f"⚠️ Sayfa çekilemedi: {e}")
    html = ""

# --- BeautifulSoup ile parse ---
soup = BeautifulSoup(html, "html.parser")

# Örnek: floor price, toplam satış, sahip sayısı
# (Sayfanın HTML yapısına göre selector’ları değiştirebilirsin)
try:
    floor_price = soup.select_one(".floor-price").text.strip()
except:
    floor_price = "N/A"

try:
    total_sales = soup.select_one(".total-sales").text.strip()
except:
    total_sales = "N/A"

try:
    owners = soup.select_one(".owners-count").text.strip()
except:
    owners = "N/A"

try:
    last_sale = soup.select_one(".last-sale-date").text.strip()
except:
    last_sale = "N/A"

# --- README için içerik ---
stats_md = f"""
Floor Price: {floor_price}
Total Sales: {total_sales}
Owners: {owners}
Last Sale: {last_sale}
"""

# --- README güncelle ---
with open(README_FILE, "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find(START_MARKER) + len(START_MARKER)
end_idx = content.find(END_MARKER)

new_content = content[:start_idx] + "\n" + stats_md + "\n" + content[end_idx:]

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ README NFT stats güncellendi!")
