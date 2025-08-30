# Auth service for login, stll needs modification
import requests

class AuthService:
    def __init__(self):
        self.base_url = 'http://localhost:8000/api/users/login/api/'

    def login(self, username, password):
        """Authenticate user by sending a POST request to the Django backend."""
        data = {'username': username, 'password': password}
        try:
            # Send data as JSON instead of form-encoded
            response = requests.post(self.base_url, json=data)

            # Check if the response was successful
            response.raise_for_status()

            if response.status_code == 200:
                # Handle successful login
                # Assuming the backend returns a JWT token in 'access_token'
                result = response.json()
                token = result.get("access_token")  # Get the JWT token from the response
                if token:
                    return LoginResult(ok=True, username=username, token=token)
                else:
                    return LoginResult(ok=False, error="No token received from server")

            else:
                # Handle error from backend
                error = response.json().get("message", "Unknown error")
                return LoginResult(ok=False, error=error)

        except requests.exceptions.RequestException as e:
            # Handle error if the backend can't be reached
            return LoginResult(ok=False, error=f"{e}")

# Helper class to manage login results
class LoginResult:
    def __init__(self, ok, username=None, token=None, error=None):
        self.ok = ok
        self.username = username
        self.token = token  # Store the token if login is successful
        self.error = error

