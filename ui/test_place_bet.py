import pytest

from ui.pages.bet_slip_page import BetSlipPage
from ui.pages.match_list_page import MatchListPage


@pytest.mark.ui
def test_place_single_bet_e2e(driver, api_client):
    #Happy path, ignoring bug with incorrect potential payout on success page
    stake_to_place = "5.00"
    match_list = MatchListPage(driver).open()
    #workaround to overcome bug with displaying passed matches
    match_slug = match_list.find_first_upcoming_match_slug()
    home_team, away_team = match_list.get_team_names(match_slug)
    odds_before_bet = match_list.get_odds_value(match_slug, "home")
    balance_before = api_client.get_balance().json()["balance"]
    match_list.select_outcome(match_slug, "home")
    bet_slip = BetSlipPage(driver)
    # Sanity-check the slip reflects the selection before we act on it.
    selection_teams_text = bet_slip.get_selection_teams()
    assert home_team in selection_teams_text and away_team in selection_teams_text, (
        f"Bet slip selection '{selection_teams_text}' does not mention both "
        f"'{home_team}' and '{away_team}'"
    )
    bet_slip.set_stake(stake_to_place)
    assert bet_slip.get_total_stake_text() == f"€{stake_to_place}"
    bet_slip.click_place_bet()
    bet_slip.wait_for_success_modal()
    receipt = bet_slip.get_receipt_details()
    assert receipt["bet_id"], "Receipt did not show a Bet ID"
    assert receipt["stake"] == f"€{stake_to_place}"
    assert receipt["odds"] == f"{odds_before_bet:.2f}"
    assert home_team in receipt["match"] and away_team in receipt["match"]
    bet_slip.close_success_modal()
    balance_after = api_client.get_balance().json()["balance"]
    assert balance_after == pytest.approx(balance_before - float(stake_to_place), abs=0.01), (
        f"Expected balance to drop by {stake_to_place} "
        f"(before={balance_before}, after={balance_after})"
    )