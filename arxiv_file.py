import arxiv

class PaperFeed:

    def __init__(self, query, length):
        self.query = query
        self.length = length

    def get_paper(self):
        search = arxiv.Search(query=self.query,
                              max_results=self.length,
                              sort_by=arxiv.SortCriterion.SubmittedDate)
        paper_body = ''
        for result in search.results():
            paper_body = paper_body + \
                         f"Title: {result.title}" + "\n" + \
                         f"Published Date: {result.published}" + "\n" + \
                         f"URL: {result.links[0]} \n \n"


        return paper_body

if __name__=="__main__":
    paper = PaperFeed(query="neutrino", length=10)
    print(paper.get_paper())