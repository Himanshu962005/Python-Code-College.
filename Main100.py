# E57.MultiProcessing in Python.
import concurrent.futures;
import requests;
import os;
def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    with open(f"files/file{name}.jpg", "wb") as file:
        file.write(response.content)
    print(f"Finished Downloading {name}")
if __name__ == "__main__":
    os.makedirs("files", exist_ok=True)
    url = "https://picsum.photos/2000/3000"
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(60)]
        l2 = [i for i in range(60)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)