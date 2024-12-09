import requests
import json

def search_google(query, api_key, cx):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": api_key, "cx": cx, "q": query, "num": 10}  # Adjust num as needed

    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_best_answer(search_results):
    # Implement your own logic to analyze the search results and extract the best answer
    # For example, you could pick the first relevant snippet from the search results
    best_answer = search_results["items"][0]["snippet"]
    return best_answer

def main():
    query = input("Your search query here: ")
    google_api_key = "AIzaSyA3F6DGnAWlM9oAc7bvD1FOKQ3fp_EunNc"
    custom_search_engine_id = "323d63fa938554f39"

    search_results = search_google(query, google_api_key, custom_search_engine_id)
    best_answer = get_best_answer(search_results)

    result_data = {
        "query": query,
        "best_answer": best_answer,
        "search_results": search_results
    }

    with open("search_results.json", "w") as json_file:
        json.dump(result_data, json_file, indent=4)

if __name__ == "__main__":
    main()
