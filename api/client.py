import requests

import config


class BetApiClient:

    def __init__(self, base_url: str = config.BASE_URL, user_id: str = config.DEFAULT_USER_ID):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"x-user-id": user_id})

    def get_matches(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/matches")

    def get_balance(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/balance")

    def reset_balance(self) -> requests.Response:
        return self.session.post(f"{self.base_url}/api/reset-balance")

    def place_bet(self, match_id: str, selection: str, stake) -> requests.Response:
        payload = {
            "matchId": match_id,
            "selection": selection,
            "stake": stake,
        }
        return self.session.post(f"{self.base_url}/api/place-bet", json=payload)
