# import requests

# def test_model_deployment(text):
#     url = "http://web:5000/testpredict"
#     data = {'text': text}
#     try:
#         response = requests.post(url, json=data)
#         response.raise_for_status()  
#         return response.json()
#     except requests.exceptions.HTTPError as http_err:
#         print(f"HTTP error occurred: {http_err}")
#         print("Response content:", response.content.decode())
#     except requests.exceptions.RequestException as req_err:
#         print(f"Request error occurred: {req_err}")
#     except Exception as err:
#         print(f"Other error occurred: {err}")

# test_sentences = [
#     "For this purpose the Gothenburg Young Persons Empowerment Scale (GYPES) was developed.",
#     "I love machine learning and natural language processing.",
#     "EPI = Echo planar imaging."
# ]

# for sentence in test_sentences:
#     print(f"Input: {sentence}")
#     print("Output:", test_model_deployment(sentence))
#     print()




# import requests
# import time

# def test_single_request(text):
#     url = "http://127.0.0.1:5000/testpredict"
#     data = {'text': text}
#     start_time = time.time()
#     try:
#         response = requests.post(url, json=data)
#         end_time = time.time()
#         if response.status_code == 200:
#             return response.json(), end_time - start_time
#         else:
#             return response.text, end_time - start_time
#     except requests.exceptions.HTTPError as http_err:
#         print(f"HTTP error occurred: {http_err}")
#         return None, None
#     except requests.exceptions.RequestException as req_err:
#         print(f"Request error occurred: {req_err}")
#         return None, None
#     except Exception as err:
#         print(f"Other error occurred: {err}")
#         return None, None

# def batch_test(texts, num_requests=10):
#     results = []
#     for _ in range(num_requests):
#         for text in texts:
#             output, response_time = test_single_request(text)
#             results.append((text, output, response_time))
#     return results

# if __name__ == "__main__":
#     test_texts = [
#         "We performed a linear regression model of the effect of PCL on Dizziness Handicap Inventory (DHI).",
#         "The following physiological traits were measured: stomatal conductance (gs, mol H2O m-2 s-1), transpiration rate (E, mmol H2O m-2 s-1), net photosynthetic rate (PN, μmol m-2 s-1) and intercellular CO2 concentration (Ci, μmol m-2 s-1)."
#     ]

#     # Perform batch test
#     results = batch_test(test_texts, num_requests=50)
#     for i, (text, output, response_time) in enumerate(results):
#         print(f"Test {i + 1}")
#         print(f"Input: {text}")
#         if output:
#             print(f"Output: {output}")
#             print(f"Response Time: {response_time:.2f} seconds")
#         else:
#             print("Output: None")
#             print("Response Time: N/A")
#         print("-" * 80)



import requests
import time

def test_single_request(text):
    url = "http://web:5000/testpredict"  
    data = {'text': text}
    start_time = time.time()
    try:
        response = requests.post(url, json=data)
        end_time = time.time()
        if response.status_code == 200:
            return response.json(), end_time - start_time
        else:
            return response.text, end_time - start_time
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return None, None

def batch_test(texts, num_requests=10):
    results = []
    for _ in range(num_requests):
        for text in texts:
            output, response_time = test_single_request(text)
            results.append((text, output, response_time))
    return results

if __name__ == "__main__":
    test_texts = [
        "We performed a linear regression model of the effect of PCL on Dizziness Handicap Inventory (DHI).",
        "The following physiological traits were measured: stomatal conductance (gs, mol H2O m-2 s-1), transpiration rate (E, mmol H2O m-2 s-1), net photosynthetic rate (PN, μmol m-2 s-1) and intercellular CO2 concentration (Ci, μmol m-2 s-1)."
    ]

    results = batch_test(test_texts, num_requests=50)
    for text, output, response_time in results:
        print(f"Input: {text}")
        print(f"Output: {output}")
        print(f"Response Time: {response_time} seconds")
        print()
