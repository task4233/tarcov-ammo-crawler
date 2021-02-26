import requests
from bs4 import BeautifulSoup
import csv

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
        except Exception as e:
            print(e)
            return None

        soup = BeautifulSoup(res.text, "html.parser")
        # h3が弾の詳細が書かれている部分
        lists = soup.find_all("h3")
        for list in lists:
            try:
                ammos = list.find_next().find_next().find_next().find_next().select_one("table > tbody > tr > td:nth-child(2)")
                # 見出しに弾が入っていない物は除去
            except Exception as e:
                print(e)
                return None
            if ammos == None:
                continue
            ammo_name = list.next_element
            print(ammo_name)
            try:
                with open("out/" + ammo_name + ".csv", "w") as f:
                    if ammos != None:
                        ammos_a = ammos.find_all('a')
                        writer = csv.writer(f)
                        writer.writerows(ammos_a)
            except Exception as e:
                print(e)
                return None
        return res.text


if __name__ == "__main__":
    st = ScrapeTarcov("https://wikiwiki.jp/eft/")
    resp = st.scrape_ammo()
    # print(resp)
    