import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.Login.login import LoginWidget
from services.auth_service import AuthService

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the AuthService
        self.auth_service = AuthService()

        # Create the LoginWidget and pass the auth_service
        self.login_widget = LoginWidget()
        
        # Set the central widget to the login form
        self.setCentralWidget(self.login_widget)
        
        # Window setup
        self.setWindowTitle("CISC Virtual Hub - Login")
        self.setGeometry(100, 100, 900, 600)  # Adjust window size as needed
        
        # Connect login success signal to open the Dashboard (optional)
        self.login_widget.login_successful.connect(self.open_dashboard)

    def open_dashboard(self, username):
        """Handles the successful login event."""
        print(f"Login successful for {username}!")  # Replace with your actual dashboard opening logic
        # Here you can initialize and show the dashboard window if needed

        # For now, just show a simple message box or proceed to the next window
        # self.dashboard = Dashboard(username)
        # self.dashboard.show()
        self.close()  # Close the login window once logged in

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the main window and display the login form
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
