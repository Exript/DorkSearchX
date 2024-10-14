import os
from modules.google_dork import perform_google_dork
from modules.github_leak import search_github_leaks
from modules.darkweb_scan import scan_darkweb

def load_dork_list():
    dork_file = "dork_list.txt"
    
    if not os.path.exists(dork_file):
        print(f"Error: {dork_file} not found.")
        return []

    with open(dork_file, 'r') as file:
        dorks = [line.strip() for line in file.readlines() if line.strip()]
    
    return dorks

def run_dorkx():
    print("Welcome to DorkSearchX!")
    print("1. Run Google Dork")
    print("2. Run GitHub Leak Search")
    print("3. Scan Dark Web")
    
    choice = input("Select an option (1, 2, 3): ")

    if choice == "1":
        dorks = load_dork_list()
        if dorks:
            print("Running Google Dork...")
            for dork in dorks:
                perform_google_dork(dork)
    elif choice == "2":
        query = input("Enter search query for GitHub leaks: ")
        search_github_leaks(query)
    elif choice == "3":
        scan_darkweb()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    run_dorkx()
