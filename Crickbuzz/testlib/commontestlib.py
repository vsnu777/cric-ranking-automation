import logging
import os
import time
from traceback import print_stack

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from Configuration.Base import BaseClass
from Utility.readProperty import ReadConfig
from Utility import logger as cl
from Utility.util import utilities


class commonlib:
    log = cl.customlogger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        actions = ActionChains(driver)

    def get_title(self):
        title = self.driver.title
        return title

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../reports/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def nav_Rankings(self):
        actions = ActionChains(self.driver)
        ranking_lbl = self.driver.find_element_by_id("rankingDropDown")
        actions.move_to_element(ranking_lbl).perform()

    def get_ranking_menu_list(self):
        rankings = self.driver.find_elements_by_xpath("//div[@id='rankingDropDown']//a[@class='cb-subnav-item']")

        for ranking in rankings:
            self.log.info("Rankinglist: %s", ranking.text)
        return rankings

    def select_mensRanking(self):
        rankinglist = self.get_ranking_menu_list()
        for ranking in rankinglist:
            try:
                if ranking.text == "ICC Rankings - Men":
                    ranking.click()
                    self.log.info("selected men\'s ranking")
            except StaleElementReferenceException as exception:
                self.log.info("Stale Exception:%s has been ignored", exception)
            # wait = utilities.waitfor(driver=self.driver, timeout=15, pollfrequency=0.5)
            # wait.until(expected_conditions.text_to_be_present_in_element_value(rankingvalue,
            #                                                                    "ICC Rankings - Men"))

            # wait = utilities.waitfor(driver=self.driver, timeout=15, pollfrequency=0.5)
            # wait.until(expected_conditions.text_to_be_present_in_element_value(rankingvalue,
            # wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".cb-nav-main h1.cb-nav-hdr")))

    def select_womenRankings(self):
        rankings = self.get_ranking_menu_list()
        for ranking in rankings:
            if ranking.text == "ICC Rankings - Women":
                ranking.click()
                self.log.info("selected women\'s ranking")

    def get_RankPlayer_list(self):
        player_name_list = []
        player_list = self.driver.find_elements(By.XPATH, "//div[@class='cb-col cb-col-67 cb-rank-plyr']//a")
        for player in player_list:
            player_name_list.append(player.text)
        self.log.info(player_name_list)
        return player_name_list

    def get_PlayerCountry_detail(self):
        player_list = self.get_RankPlayer_list()
        player_country = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='cb-col cb-col-67 cb-rank-plyr']//a//following-sibling::div")
        playerCountry_dict = {}
        i = 0
        for player in player_list:
            country_name = player_country[i].text
            playerCountry_dict[player] = country_name
            i = i + 1
        self.log.info("Player dictionary is %s:", playerCountry_dict)
        return playerCountry_dict

    def get_Rank_detail(self):
        player_list = self.get_RankPlayer_list()
        player_Rank = self.driver.find_elements(By.XPATH,
                                                "//div//div[@class='cb-col cb-col-16 cb-rank-tbl cb-font-16']")
        playerRank_dict = {}
        i = 0
        for player in player_list:
            playerRank_dict[player] = player_Rank[i].text
            i = i + 1
        self.log.info("Player dictionary is %s:", playerRank_dict)
        return playerRank_dict

    def get_Rating_detail(self):
        player_list = self.get_RankPlayer_list()
        player_rating = self.driver.find_elements(By.CSS_SELECTOR,
                                                  ".cb-rank-tbl.pull-right")
        playerRating_dict = {}
        i = 0
        for player in player_list:
            playerRating_dict[player] = player_rating[i].text
            i = i + 1
        self.log.info("Player dictionary is %s:", playerRating_dict)
        return playerRating_dict
