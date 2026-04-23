import requests

BASE_URL = "https://api.openalex.org"

class OpenAlexClient:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def _get(self, endpoint, params=None):
        if params is None:
            params = {}
        if self.api_key:
            params["api_key"] = self.api_key
        url = f"{BASE_URL}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Works
    def get_work(self, work_id):
        """Retrieve a single work by ID (e.g., W2741809807 or doi:10.xxx)."""
        return self._get(f"works/{work_id}")

    def list_works(self, **filters):
        """List works with filters (e.g., publication_year=2023)."""
        return self._get("works", params=filters)

    # Authors
    def get_author(self, author_id):
        return self._get(f"authors/{author_id}")

    def list_authors(self, **filters):
        return self._get("authors", params=filters)

    # Institutions
    def get_institution(self, institution_id):
        return self._get(f"institutions/{institution_id}")

    def list_institutions(self, **filters):
        return self._get("institutions", params=filters)

    # Sources
    def get_source(self, source_id):
        return self._get(f"sources/{source_id}")

    def list_sources(self, **filters):
        return self._get("sources", params=filters)

    # Topics
    def list_topics(self, **filters):
        return self._get("topics", params=filters)

    # Autocomplete
    def autocomplete(self, entity_type, query):
        return self._get(f"autocomplete/{entity_type}", params={"q": query})
