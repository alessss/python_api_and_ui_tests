from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class BetSlipPage(BasePage):
    #bet slip
    SELECTION_TEAMS = (By.CSS_SELECTOR, ".betSelectionTeams")
    SELECTION_MARKET = (By.CSS_SELECTOR, ".betSelectionMarket")
    SELECTION_ODDS = (By.CSS_SELECTOR, ".betSelectionOdds")
    STAKE_INPUT = (By.ID, "bet-slip-stake-input")
    TOTAL_STAKE = (By.ID, "bet-slip-total-stake")
    POTENTIAL_PAYOUT = (By.ID, "bet-slip-potential-payout")
    PLACE_BET_BUTTON = (By.ID, "bet-slip-place-bet")

    #success receipt modal
    SUCCESS_MODAL_TITLE = (By.CSS_SELECTOR, ".modalTitle")
    SUCCESS_BET_ID = (By.ID, "modal-success-bet-id")
    SUCCESS_MATCH = (By.ID, "modal-success-match")
    SUCCESS_STAKE = (By.ID, "modal-success-stake")
    SUCCESS_ODDS = (By.ID, "modal-success-odds")
    SUCCESS_PAYOUT = (By.ID, "modal-success-payout")
    SUCCESS_PLACED_AT = (By.ID, "modal-success-placed-at")
    SUCCESS_CLOSE_BUTTON = (By.ID, "modal-success-close")
    SUCCESS_CLOSE_X = (By.ID, "modal-success-close-x")

    #bet slip actions
    def get_selection_teams(self) -> str:
        return self.get_text(*self.SELECTION_TEAMS)

    def set_stake(self, value: str):
        stake_field = self.find_visible(*self.STAKE_INPUT)
        stake_field.clear()
        stake_field.send_keys(str(value))
        return self

    def get_total_stake_text(self) -> str:
        return self.get_text(*self.TOTAL_STAKE)

    def click_place_bet(self):
        self.click(*self.PLACE_BET_BUTTON)
        return self

    #success modal actions
    def wait_for_success_modal(self):
        self.find_visible(*self.SUCCESS_BET_ID)
        return self

    def get_receipt_details(self) -> dict:
        return {
            "bet_id": self.get_text(*self.SUCCESS_BET_ID),
            "match": self.get_text(*self.SUCCESS_MATCH),
            "stake": self.get_text(*self.SUCCESS_STAKE),
            "odds": self.get_text(*self.SUCCESS_ODDS),
            "payout": self.get_text(*self.SUCCESS_PAYOUT),
            "placed_at": self.get_text(*self.SUCCESS_PLACED_AT),
        }

    def close_success_modal(self):
        self.click(*self.SUCCESS_CLOSE_BUTTON)
        return self