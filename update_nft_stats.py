from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome ayarları (WSL uyumlu headless)
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--disable-software-rasterizer")

# Chromium driver kurulumu
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(chrome_type="chromium").install()),
    options=options
)

# PixelPulse sayfası
url = "https://crystara.trade/marketplace/pixelpulse"
driver.get(url)

# JS yüklenmesi için bekle
time.sleep(7)  # gerekirse artırabilirsin

# Verileri çek (Crystara sayfasının gerçek class/id'lerini buraya yaz)
def safe_find(selector):
    try:
        return driver.find_element(By.CSS_SELECTOR, selector).text.strip()
    except:
        return "N/A"

# ⚠ Buradaki CSS selector'ları sayfayı inspect ederek güncelle
floor_price = safe_find(".marketplace-floor-price")
total_sales = safe_find(".marketplace-total-sales")
owners = safe_find(".marketplace-owners")
last_sale = safe_find(".marketplace-last-sale")

driver.quit()

# README güncelleme
with open("README.md", "r") as f:
    content = f.read()

start_marker = "<!-- NFT_STATS_START -->"
end_marker = "<!-- NFT_STATS_END -->"

new_stats = f"""
Floor Price: {floor_price}
Total Sales: {total_sales}
Owners: {owners}
Last Sale: {last_sale}
"""

if start_marker in content and end_marker in content:
    before = content.split(start_marker)[0]
    after = content.split(end_marker)[1]
    content = before + start_marker + "\n" + new_stats + "\n" + end_marker + after

with open("README.md", "w") as f:
    f.write(content)

print("✅ README NFT stats güncellendi!")
