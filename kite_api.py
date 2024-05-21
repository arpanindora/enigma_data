from kiteconnect import KiteConnect
from kiteconnect.exceptions import KiteException
import json
from logger import AppLogger

class KiteAPI:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.kite = None
        self.log = AppLogger()
        self.api_key, self.api_secret = self._load_api_credentials()

    def _load_api_credentials(self):
        """
        Load API credentials from a configuration file.
        """
        try:
            with open(self.config_file, 'r') as file:
                data = json.load(file)
                return data['kiteconnect']['api_key'], data['kiteconnect']['api_secret']
        except Exception as e:
            self.log.error(f"Failed to load API credentials: {e}")
            raise

    def _start_session(self):
        """
        Start a session by authenticating with the API and setting the access token.
        """
        self.kite = KiteConnect(api_key=self.api_key)
        print(f"Visit this URL to get your request_token: {self.kite.login_url()}")

        request_token = input("Enter the request token here: ")
        try:
            data = self.kite.generate_session(request_token, api_secret=self.api_secret)
            self.kite.set_access_token(data["access_token"])
        except KiteException as e:
            self.log.error(f"Failed to start session: {e}")
            raise
        return self.kite

    def get_session_connected(self):
        """
        Check if the current session is connected, otherwise initiate a new session.
        """
        if self.kite is None:
            return self._start_session()

        try:
            self.kite.profile()  # This throws an exception if the session is not valid
            return self.kite
        except KiteException as e:
            if e.code == 'Token is invalid':
                self.log.warning("Session has expired or is invalid.")
                return self.start_session()
            else:
                self.log.error(f"An error occurred: {e.message}")
                raise(f"An error occurred: {e.message}")
            

