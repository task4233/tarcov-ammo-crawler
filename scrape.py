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
        self.guns = {}
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
            usable_ammos_for_gun = []
            try:
                if ammos != None:
                    ammos_a = ammos.find_all('a')
                    [usable_ammos_for_gun.append(am.get_text()) for am in ammos_a]
            except Exception as e:
                print(e)
                return None
            self.guns[ammo_name] = usable_ammos_for_gun
        print('====================guns==========================')
        for key in self.guns.keys():
            print(key)
            print(self.guns[key])
        return res.text
    
    def scrape_guns(self):
        guns_url = self.base_url + "武器一覧"

        # get text
        res = ""
        try:
            res = requests.get(guns_url)
        except Exception as e:
            return e

        soup = BeautifulSoup(res.text, "html.parser")
        tbodies = soup.find_all("tbody")
        for tbody in tbodies:
            print("=================tbody==================")
            tds = tbody.find_all("td")
            # print(tds)
            print(tds.find_all('td:nth-child(1)'))
        return None

if __name__ == "__main__":
    st = ScrapeTarcov("https://wikiwiki.jp/eft/")
    err = st.scrape_guns()
    if err != None:
        print(err)
    print("Run successfully")
    