from bs4 import BeautifulSoup
import requests, json, os

class main():
    def scrapeManga(self, saveToFile:bool=False):
        id = self.split("/")

        with open("cookies.json", "r") as file:
            cookie = json.loads(file.read())

            cookies = {
                'cf_clearance': cookie["cookies"]["cf_clearance"],
                'csrftoken': cookie["cookies"]["csrftoken"]
            }

        headers = {
            'authority': 'nhentai.net',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0', 
            'referer': 'https://nhentai.net/',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        response = requests.get(self, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        tag = soup.find_all("span", {"class": "tags"})[2]

        tags = [i.find_all("span")[0].text for i in tag.find_all("a")]
        pages = [
            "https://nhentai.net/g" + i["href"]
            for i in soup.find_all("a", {"class": "gallerythumb"})
        ]
        jsonFormat = {
            "manga": {
                "id": id[4],
                "tags-info": {"count": len(tags), "tags": tags},
                "artist": soup.find_all("span", {"class": "tags"})[3]
                .find_all("span")[0]
                .text,
                "languages": soup.find_all("span", {"class": "tags"})[5]
                .find_all("span")[0]
                .text,
                "categories": soup.find_all("span", {"class": "tags"})[6]
                .find_all("span")[0]
                .text,
                "pages-info": {"count": len(pages), "pages-link": pages},
                "uploaded": soup.find_all("span", {"class": "tags"})[8].find_all(
                    "time"
                )[0]["datetime"],
            }
        }

        if not saveToFile:
            print("\n" + json.dumps(jsonFormat, indent=4) + "\n")
        else:
            with open(f"{id[4]}.json", "w") as file:
                file.write(json.dumps(jsonFormat, indent=4))

            print("\n" + "========================================" + "\n" + json.dumps(jsonFormat, indent=4) + "\n" + "========================================" + "\n")

if __name__ == "__main__":
    os.system("cls")
    while True:
        manga = input("Insert NHentai Link or ID: ")
        saveResult = input("Write to file (Y/N): ")

        try:
            if "https://nhentai.net/g/" in manga:
                if saveResult == "n":
                    main.scrapeManga(manga)
                else:
                    main.scrapeManga(manga, True)
            elif saveResult == "n":
                main.scrapeManga(f"https://nhentai.net/g/{manga}")
            else:
                main.scrapeManga(f"https://nhentai.net/g/{manga}", True)
        except Exception as err:
            print("\n" + "Error: " + str(err) + "\n")