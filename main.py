from openalex import OpenAlexClient

client = OpenAlexClient()

# Example: Get a specific work
work = client.get_work("W2741809807")
print(work["display_name"])

# Example: List works published in 2023
works = client.list_works(filter="publication_year:2023", per_page=5)
for w in works["results"]:
    print(w["display_name"])

# Example: Autocomplete author search
authors = client.autocomplete("authors", "Russel Rey F. Lupian")
print(authors)
