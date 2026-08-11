
def test_get_api_request(playwright):
     request= playwright.request.new_context()
     response= request.get("https://jsonplaceholder.typicode.com/posts/1")
     assert response.status == 200
     json_data = response.json()
     print(json_data)
     assert json_data["id"] == 1
     response.dispose()
     print("API request test completed successfully.")