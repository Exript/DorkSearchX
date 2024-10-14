import os
from googlesearch import search

# Dork listesini dork_list.txt dosyasından oku
def load_dorks(file_path):
    dorks = []
    with open(file_path, 'r') as file:
        for line in file:
            # Her satırda arama komutu ve açıklama olduğu varsayılıyor
            parts = line.strip().split(',')
            if len(parts) > 1:
                dorks.append(parts[0])  # Sadece arama komutunu al
    return dorks

# Google'da dorkları arama ve sonuçları döndürme
def google_dork(domain, dorks):
    for dork in dorks:
        # Google aramasında "site:<domain>" ile sorgulama yap
        query = f"site:{domain} {dork}"
        print(f"\n[*] Searching for: {query}")
        try:
            # Googlesearch kütüphanesi ile arama yap
            results = search(query, num_results=10)
            for result in results:
                print(result)
                # Sonuçları dosyaya yaz
                with open("dork_results.txt", "a") as f:
                    f.write(result + "\n")
        except Exception as e:
            print(f"[!] Error while searching for {query}: {e}")

if __name__ == "__main__":
    # Kullanıcıdan domain adresini al
    domain = input("Enter the domain to search (e.g., example.com): ").strip()

    # Dork listesini yükle
    dorks = load_dorks('dork_list.txt')

    # Google'da dorking işlemini başlat
    google_dork(domain, dorks)
/usr/local/python/3.12.1/bin/python3 google_dork.py