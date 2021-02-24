import requests
from bs4 import BeautifulSoup

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

        # get text
        res = ""
        try:
            res = requests.get(ammo_url)
        except Exception: # as e
            # print(e)
            return None

        soup = BeautifulSoup(res.text, "html.parser")
        lists = soup.find_all("h2")
        cnt = 0
        for list in lists:
            # 見出しに弾が入っていない物は除去
            if not "弾" in list.contents[0]:
                continue
            cnt += 1
            if cnt == 1:
                print(list)
            with open("out/" + str(cnt)+".txt", "w") as f:
                f.write(str(list.contents))
        return res.text


if __name__ == "__main__":
    st = ScrapeTarcov("https://wikiwiki.jp/eft/")
    resp = st.scrape_ammo()
    print(resp)
    