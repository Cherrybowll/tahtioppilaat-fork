class DOI:
    def __init__(self, doi_id, doi):
        self.id = doi_id
        self.doi = doi

    def __str__(self):
        return f"{self.doi}"
