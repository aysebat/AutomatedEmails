import arxiv

class PaperFeed:

    def __init__(self, query, length):
        self.query = query
        self.length = length

    def get_paper(self):
        search = arxiv.Search(query=self.query,
                              max_results= self.length,
                              sort_by=arxiv.SortCriterion.SubmittedDate)

        for result in search.results():
            print(result.title)
            print(result.links[0])




paper = PaperFeed(query="neutrino", length=10)
print(paper.get_paper())