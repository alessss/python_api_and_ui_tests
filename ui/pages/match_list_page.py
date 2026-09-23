from selenium.webdriver.common.by import By

import config
from ui.pages.base_page import BasePage


class MatchListPage(BasePage):
    #Page Object for the match list (main page)

    MATCH_LIST_CONTAINER = (By.ID, "match-list")
    HEADER_BALANCE = (By.ID, "header-balance")

    def open(self):
        self.driver.get(config.BASE_URL + config.DEFAULT_USER_ID_PARAM)
        self.find_visible(*self.MATCH_LIST_CONTAINER)
        return self

    @staticmethod
    def _badge_locator(match_slug: str):
        return By.CSS_SELECTOR, f"#match-card-{match_slug} .badge"

    @staticmethod
    def _team_name_locator(match_slug: str):
        return By.CSS_SELECTOR, f"#match-card-{match_slug} .teamName"

    @staticmethod
    def _odds_button_locator(match_slug: str, outcome: str):
        # outcome must be one of: home, draw, away
        return By.ID, f"odds-{match_slug}-{outcome}"

    def get_team_names(self, match_slug: str) -> tuple[str, str]:
        elements = self.find_all_present(*self._team_name_locator(match_slug))
        names = [el.text for el in elements]
        return names[0], names[1]

    def get_odds_value(self, match_slug: str, outcome: str) -> float:
        button = self.find_visible(*self._odds_button_locator(match_slug, outcome))
        value_text = button.find_element(By.CSS_SELECTOR, ".oddsButtonValue").text
        return float(value_text)

    def select_outcome(self, match_slug: str, outcome: str):
        assert outcome in {"home", "draw", "away"}, f"Invalid outcome: {outcome}"
        self.click(*self._odds_button_locator(match_slug, outcome))
        return self

    def find_first_upcoming_match_slug(self) -> str:
        cards = self.find_all_present(By.CSS_SELECTOR, "#match-list .matchCard")
        for card in cards:
            card_id = card.get_attribute("id")  # e.g. "match-card-championship-leeds-norwich-2026-09-25"
            slug = card_id.removeprefix("match-card-")
            badge_text = card.find_element(By.CSS_SELECTOR, ".badge").text
            if badge_text == "UPCOMING":
                return slug
        raise AssertionError("No UPCOMING match found in the rendered match list")