import requests

def test_model_deployment(text):
    url = "http://web:5000/testpredict"
    data = {'text': text}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print("Response content:", response.content.decode())
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Test the deployment
test_sentences = [
    "For this purpose the Gothenburg Young Persons Empowerment Scale (GYPES) was developed.",
    "I love machine learning and natural language processing.",
    "EPI = Echo planar imaging."
]

for sentence in test_sentences:
    print(f"Input: {sentence}")
    print("Output:", test_model_deployment(sentence))
    print()
