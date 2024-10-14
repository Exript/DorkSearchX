import requests

def scan_darkweb():
    tor_proxy = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }

    search_query = input("Enter your search query for the dark web: ")
    darkweb_search_engine = "http://searchxdarkweb.onion/search?q="  # Dark web search engine URL

    try:
        url = darkweb_search_engine + search_query
        response = requests.get(url, proxies=tor_proxy)

        if response.status_code == 200:
            print("Dark web search successful!")
            print("Results:\n")
            print(response.text)  # You can also use BeautifulSoup to parse the HTML results
        else:
            print("Failed to retrieve results. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the dark web: {e}")

if __name__ == "__main__":
    scan_darkweb()
