from github import Github

def search_github_leaks():
    g = Github("your_github_token_here")  # Replace with your GitHub API token
    query = "filename:credentials.json OR filename:password"
    
    result = g.search_code(query)
    
    for repo in result:
        print(f"Repository: {repo.repository.full_name}")
        print(f"File URL: {repo.html_url}\n")
    
    print("GitHub leak search completed.\n")
