## NHentai Scraper 2022
- [Also check out NHentai Downloader](https://github.com/Charlzk05/NHentai-Downloader-2022)

NHentai Scraper that uses requests and cookies to bypass cloudflare

### Installation
1. Clone the repository ``git clone https://github.com/Charlzk05/NHentai-Scraper-2022.git``
2. Install requirements ``pip install -r requirements.txt``

### Usage
1. Go to your cloned repo folder
2. Get your **cf_clearance** and **csrftoken** cookie on [nhentai.net](https://nhentai.net/)

  ![image](https://user-images.githubusercontent.com/104715127/193413180-2271c533-4964-4969-bbbe-3afd71e9a623.png)
  ![image](https://user-images.githubusercontent.com/104715127/193413192-3ee30ce7-62f9-47ed-a49e-59c23fd17c39.png)

3. Replace **cf_clearance** and **csrftoken** on cookie.json with your cookies
4. Run the main.py with ``py main.py``
5. Result
```json
{
    "result": {
        "id": "369508",
        "tags-info": {
            "count": 2,
            "tags": [
                "dark skin",
                "corruption"
            ]
        },
        "artist": "ratatatat74 | mr.skull",
        "languages": "japanese",
        "categories": "doujinshi",
        "pages-info": {
            "count": 15,
            "pages-link": [
                "https://nhentai.net/g/g/369508/1/",
                "https://nhentai.net/g/g/369508/2/",
                "https://nhentai.net/g/g/369508/3/",
                "https://nhentai.net/g/g/369508/4/",
                "https://nhentai.net/g/g/369508/5/",
                "https://nhentai.net/g/g/369508/6/",
                "https://nhentai.net/g/g/369508/7/",
                "https://nhentai.net/g/g/369508/8/",
                "https://nhentai.net/g/g/369508/9/",
                "https://nhentai.net/g/g/369508/10/",
                "https://nhentai.net/g/g/369508/11/",
                "https://nhentai.net/g/g/369508/12/",
                "https://nhentai.net/g/g/369508/13/",
                "https://nhentai.net/g/g/369508/14/",
                "https://nhentai.net/g/g/369508/15/"
            ]
        },
        "uploaded": "2021-08-16T05:27:32.367878+00:00"
    }
}
```
