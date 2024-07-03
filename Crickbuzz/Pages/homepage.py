from Configuration.Base import BaseClass
from testlib import commontestlib


class Cribuzz_home:
    def __init__(self, driver):
        self.driver = driver
        self.clibs = commontestlib.commonlib(driver)

    def homePageTitle(self):
        return self.clibs.get_title()

    def get_logo_type(self):
        cricbuzz_logo = self.driver.find_element_by_id("cb-logo-main-menu")
        clogo_type = cricbuzz_logo.get_attribute("itemprop")
        return clogo_type

    def get_player_Rank(self,player_name):
        self.clibs.nav_Rankings()
        self.clibs.select_mensRanking()
        player_rank_dict = self.clibs.get_Rank_detail()
        for player, rank in player_rank_dict.items():
            if player == player_name:
                player_rank = int(rank)
        return player_rank
    
    def get_player_Rank(self,player_name):
        self.clibs.nav_Rankings()
        self.clibs.select_mensRanking()
        player_rank_dict = self.clibs.get_Rank_detail()
        for player, rank in player_rank_dict.items():
            if player == player_name:
                player_rank = int(rank)
        return player_rank






