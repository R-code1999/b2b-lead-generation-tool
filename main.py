import requests
from bs4 import BeautifulSoup

query = input("Enter your target (e.g. gyms in Delhi): ")
search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(search_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

print(f"\nSearching for: {query}\n")

results = soup.find_all("h3")

for i, result in enumerate(results[:5], start=1):
    print(f"{i}. {result.text}")

print("\nBasic lead data extracted (demo level).")
