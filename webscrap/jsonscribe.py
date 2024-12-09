import json

def load_search_results(json_file_path):
    with open(json_file_path, "r") as json_file:
        search_data = json.load(json_file)
    return search_data

def format_search_results(search_data):
    query = search_data["query"]
    best_answer = search_data["best_answer"]
    search_results = search_data["search_results"]["items"]

    formatted_results = f"Query: {query}\n\nBest Answer: {best_answer}\n\nSearch Results:\n"
    for idx, result in enumerate(search_results, start=1):
        title = result.get("title", "")
        snippet = result.get("snippet", "")
        link = result.get("link", "")

        formatted_results += f"{idx}. {title}\n   {snippet}\n   Link: {link}\n\n"

    return formatted_results

def main():
    json_file_path = "search_results.json"

    search_data = load_search_results(json_file_path)
    formatted_results = format_search_results(search_data)

    print(formatted_results)

if __name__ == "__main__":
    main()
