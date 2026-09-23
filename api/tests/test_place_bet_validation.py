import pytest


@pytest.mark.api
@pytest.mark.parametrize("stake", [1, 100, 0o001, 0xA])
def test_place_bet_stake_200(api_client, stake):
    matches = api_client.get_matches().json()
    assert matches, "No matches returned by GET /api/matches — cannot proceed with test"
    match = matches[0]
    balance_before = api_client.get_balance().json()["balance"]
    response = api_client.place_bet(
        match_id=match["id"],
        selection="HOME",
        stake=stake,
    )
    assert response.status_code == 200, (
        f"Expected 200 for valid stake, got {response.status_code}: {response.text}"
    )
    balance_after = api_client.get_balance().json()["balance"]
    assert balance_after == (balance_before - stake), (
        "Balance not changed despite bet placement being accepted — "
        f"before={balance_before}, after={balance_after}"
    )

#Bug not described in manual part present: "-1" for stake returns 200 status code, expected 422
#Failing test left intentionnaly, @pytest.mark.xfail decorator can be added if we are aware of this fact
@pytest.mark.api
@pytest.mark.parametrize("stake", [0.50, 0.99, 0, -1, "abc", 101, 0o001111, 0xABC])
def test_place_bet_stake_422(api_client, stake):
    matches = api_client.get_matches().json()
    assert matches, "No matches returned by GET /api/matches — cannot proceed with test"
    match = matches[0]
    balance_before = api_client.get_balance().json()["balance"]
    response = api_client.place_bet(
        match_id=match["id"],
        selection="HOME",
        stake=stake,
    )
    assert response.status_code == 422, (
        f"Expected 422 for invalid stake, got {response.status_code}: {response.text}"
    )
    balance_after = api_client.get_balance().json()["balance"]
    assert balance_after == balance_before, (
        "Balance changed despite bet placement being rejected — "
        f"before={balance_before}, after={balance_after}"
    )