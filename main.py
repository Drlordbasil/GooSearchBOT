import requests
from bs4 import BeautifulSoup


class GoogleSearch:
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

    def search(self, query):
        try:
            url = f"https://www.google.com/search?q={query}"
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                results = self.extract_results(soup)
                return results

        except requests.RequestException as e:
            print(f"An error occurred while fetching search results: {e}")

        return []

    def extract_results(self, soup):
        results = []
        search_results = soup.select("div.g")

        for result in search_results:
            title_element = result.select_one("h3")
            link_element = result.select_one("a")
            snippet_element = result.select_one("div.IsZvec")

            if title_element and link_element and snippet_element:
                title = title_element.get_text()
                link = link_element["href"]
                snippet = snippet_element.get_text()

                results.append({"title": title, "link": link, "snippet": snippet})

        return results


def execute_program():
    query = "Top Python libraries for data analysis"

    search_engine = GoogleSearch()
    search_results = search_engine.search(query)

    if search_results:
        print("Search Results:")
        for result in search_results:
            print(f"Title: {result['title']}")
            print(f"Link: {result['link']}")
            print(f"Snippet: {result['snippet']} (trimmed)")
            print("---")
    else:
        print(
            f"No search results found for the query: {query}. Please try again with a different query."
        )


if __name__ == "__main__":
    execute_program()
