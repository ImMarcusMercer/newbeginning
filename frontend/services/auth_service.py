# Auth service for login, stll needs modification
import requests

class AuthService:
    def __init__(self):
        self.base_url = 'http://localhost:8000/users/login/api/'  

    def login(self, username, password):
        """Authenticate user by sending a POST request to the Django backend."""
        data = {'username': username, 'password': password}
        try:
            response = requests.post(self.base_url, data=data)
            response.raise_for_status()

            if response.status_code == 200:
                # Handle successful login, return result
                return LoginResult(ok=True, username=username)
            else:
                # Handle error from backend
                error = response.json().get("message", "Unknown error")
                return LoginResult(ok=False, error=error)

        except requests.exceptions.RequestException as e:
            # Handle error if the backend can't be reached
            return LoginResult(ok=False, error="Failed to connect to the server")

# Helper class to manage login results
class LoginResult:
    def __init__(self, ok, username=None, error=None):
        self.ok = ok
        self.username = username
        self.error = error
