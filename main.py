from bs4 import BeautifulSoup
import requests, json

class main():
    def scrapeManga(url:str, saveToFile:bool=False):
        id = url.split("/")

        with open("cookies.json", "r") as file:
            cookie = json.loads(file.read())

            cookies = {
                'cf_clearance': cookie["cookies"]["cf_clearance"],
                'csrftoken': cookie["cookies"]["csrftoken"]
            }

        headers = {
            'authority': 'nhentai.net',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117',
        }

        response = requests.get(url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        tag = soup.find_all("span", {"class": "tags"})[2]

        tags = []
        pages = []

        for i in tag.find_all("a"):
            tags.append(i.find_all("span")[0].text)

        for i in soup.find_all("a", {"class": "gallerythumb"}):
            pages.append("https://nhentai.net/g" + i["href"])

        jsonFormat = {
            "result": {
                "id": id[4],
                "tags-info": {
                    "count": int(len(tags)),
                    "tags": tags
                },
                "artist": soup.find_all("span", {"class": "tags"})[3].find_all("span")[0].text,
                "languages": soup.find_all("span", {"class": "tags"})[5].find_all("span")[0].text,
                "categories": soup.find_all("span", {"class": "tags"})[6].find_all("span")[0].text,
                "pages-info": {
                    "count": int(len(pages)),
                    "pages-link": pages
                },
                "uploaded": soup.find_all("span", {"class": "tags"})[8].find_all("time")[0]["datetime"]
            }
        }

        if saveToFile == False:
            print("\n" + json.dumps(jsonFormat, indent=4) + "\n")
        else:
            with open(f"{id[4]}.json", "w") as file:
                file.write(json.dumps(jsonFormat, indent=4))

            print("\n" + json.dumps(jsonFormat, indent=4) + "\n")

if __name__ == "__main__":
    while True:
        manga = input("Insert NHentai Link or ID: ")
        saveResult = input("Write to file (Y/N): ")

        try:
            if "https://nhentai.net/g/" in manga:
                if saveResult == "n":
                    main.scrapeManga(manga)
                else:
                    main.scrapeManga(manga, True)
            else:
                if saveResult == "n":
                    main.scrapeManga("https://nhentai.net/g/" + manga)
                else:
                    main.scrapeManga("https://nhentai.net/g/" + manga, True)
        except Exception as err:
            print("\n" + "Error: " + str(err) + "\n")