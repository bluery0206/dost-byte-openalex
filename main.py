from openalex import OpenAlexClient

def main():
    client = OpenAlexClient()

    # Ask the user what they want to search
    search_type = input("What do you want to search (work, author, institution)? ").strip().lower()
    query = input("Enter your search term: ").strip()

    if search_type == "work":
        # Search works
        works = client.list_works(search=query, per_page=5)
        for w in works["results"]:
            print(w["display_name"])

    elif search_type == "author":
        # Search authors
        authors = client.autocomplete("authors", query)
        print(authors)

    elif search_type == "institution":
        # Search institutions
        institutions = client.list_institutions(search=query, per_page=5)
        for inst in institutions["results"]:
            print(inst["display_name"])

    else:
        print("Unknown search type. Please choose 'work', 'author', or 'institution'.")

if __name__ == "__main__":
    main()
