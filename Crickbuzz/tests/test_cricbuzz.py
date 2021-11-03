import inspect
import logging
import os

from selenium.webdriver.common.by import By

from Configuration.Base import BaseClass
from Pages import homepage
from Utility import logger as cl, StatusReport as st
from Utility.util import utilities
from testlib import commontestlib
from testlib.navigation import nav
from selenium import webdriver

class TestCricbuzz(BaseClass):
    log = cl.customlogger(loglevel=logging.INFO)

    def test_cricbuzz(self):
        hpage = homepage.Cribuzz_home(self.driver)
        navigation = nav(self.driver)
        Ver = st.status()
        clibs = commontestlib.commonlib(self.driver)
        self.log.info("Launch Crickbuzz web Application")
        navigation.launch_App()
        title = hpage.homePageTitle()
        cricbuzz = "Cricbuzz"
        self.log.info("Titile is : %s ", title)
        self.log.info("Verify that lauched application title is \'Cricbuzz\'")
        self.log.info("#####Cricbuzz Title Verification#####")
        ver1 = False
        if cricbuzz in title:
            ver1 = True
        Ver.Verify_result(result=ver1, msg="Cricbuzz Title ")
        self.log.info("We have successfully launched cricbuzz")

        self.log.info("#####Cricbuzz logo Verification#####")
        clogo_type = hpage.get_logo_type()
        ver2 = False
        if clogo_type == "image":
            ver2 = True
        Ver.Verify_result(result=ver2, msg="Cricbuzz logo ")
        clibs.screenShot("Cricbuzz logo Verification")


    def test_WomenRanking(self):
        clibs = commontestlib.commonlib(self.driver)
        hpage = homepage.Cribuzz_home(self.driver)
        navigation = nav(self.driver)
        Ver = st.status()
        self.log.info("#####Verify that Women's Ranking page is displayed.######")
        clibs.nav_Rankings()
        clibs.select_womenRankings()
        page_heading = self.driver.find_element(By.CSS_SELECTOR, ".cb-nav-main h1.cb-nav-hdr")
        Ver.verify_text(expected_text="ICC Cricket Rankings - Women's Batting", actual_text=page_heading.text,
                        msg='Women Ranking page')

    def test_MenRanking(self):
        clibs = commontestlib.commonlib(self.driver)
        hpage = homepage.Cribuzz_home(self.driver)
        navigation = nav(self.driver)
        Ver = st.status()
        self.log.info("#####Verify that Mens Ranking page is displayed.######")
        clibs.nav_Rankings()
        clibs.select_mensRanking()

        page_heading = self.driver.find_element(By.CSS_SELECTOR, ".cb-nav-main h1.cb-nav-hdr")
        Ver.verify_text(expected_text="ICC Cricket Rankings - Men's Batting",actual_text=page_heading.text,msg='Mens Ranking page')

    def test_TopRanking_player(self):
        clibs = commontestlib.commonlib(self.driver)
        hpage = homepage.Cribuzz_home(self.driver)
        navigation = nav(self.driver)
        Ver = st.status()
        clibs.nav_Rankings()
        clibs.select_mensRanking()
        player_rank_dict = clibs.get_Rank_detail()
        for player,rank in player_rank_dict.items():
            if rank == "1":
                self.log.info("%s is the top ranking test player", player)
                top_ranking_player = player
                break
        Ver.verify_text(expected_text="Joe Root",actual_text=top_ranking_player, msg='Top Ranking Player')

    def test_playerranking(self):
        clibs = commontestlib.commonlib(self.driver)
        hpage = homepage.Cribuzz_home(self.driver)
        navigation = nav(self.driver)
        Ver = st.status()
        self.log.info("#####Verify that Rohit Sharma is in the top 5 best Test  player list#####")
        rank = hpage.get_player_Rank("Rohit Sharma")
        Ver.verify_Num_Condition(10,rank,"lt", "Rohit Sharma is in the top 5 best Test Day player list")
        utilities.get_testcaseName()






