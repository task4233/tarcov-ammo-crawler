import requests
# from bs4 import BeautifulSoup

class ScrapeTarcov():
    """
    ScrapeTarov scrape information from wiki
    https://wikiwiki.jp/eft/
    """

    def __init__(self, base_url):
        self.base_url = base_url
        pass

    def scrape_ammo(self):
        ammo_url = self.base_url + "弾薬"
        print(ammo_url)

        try:
            response = requests.get(ammo_url)
        except Exception as e:
            print(e)
            return None 
        return response.text


if __name__ == "__main__":
    st = ScrapeTarcov("https://wikiwiki.jp/eft/")
    resp = st.scrape_ammo()
    print(resp)
    