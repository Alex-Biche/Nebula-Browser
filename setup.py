from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget

class SetupWindow(QMainWindow):
    def __init__(self, config, save_config_callback):
        super().__init__()
        self.config = config
        self.save_config = save_config_callback

        self.setWindowTitle("Nebula - First Time Setup")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Choose Your Theme:")
        self.light_button = QPushButton("Light Mode")
        self.dark_button = QPushButton("Dark Mode")

        self.light_button.clicked.connect(self.select_light_theme)
        self.dark_button.clicked.connect(self.select_dark_theme)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.light_button)
        layout.addWidget(self.dark_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_light_theme(self):
        self.config["theme"] = "light"
        self.config["first_launch"] = False
        self.save_config(self.config)
        self.close()

    def select_dark_theme(self):
        self.config["theme"] = "dark"
        self.config["first_launch"] = False
        self.save_config(self.config)
        self.close()
