from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QLineEdit, QPushButton, QListWidget, QListWidgetItem, QSplitter
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl

class NebulaBrowser(QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.setWindowTitle("Nebula")
        self.setGeometry(100, 100, 1024, 768)

        self.tabs = []
        self.tab_widgets = {}

        # Apply Theme
        self.apply_theme()

        # Sidebar for Tabs
        self.sidebar = QListWidget()
        self.sidebar.setMaximumWidth(200)
        self.sidebar.itemClicked.connect(self.switch_tab)

        # Top Bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Search or enter a URL...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.new_tab_button = QPushButton("+")
        self.new_tab_button.clicked.connect(self.new_tab)

        self.close_tab_button = QPushButton("x")
        self.close_tab_button.clicked.connect(self.close_tab)

        top_bar_layout = QHBoxLayout()
        top_bar_layout.addWidget(self.new_tab_button)
        top_bar_layout.addWidget(self.close_tab_button)
        top_bar_layout.addWidget(self.url_bar)

        # Main Browser Area
        self.browser = QWebEngineView()
        self.new_tab(start_url="nebula://home")

        # Splitter for Sidebar and Browser Area
        splitter = QSplitter()
        splitter.addWidget(self.sidebar)
        splitter.addWidget(self.browser)
        splitter.setSizes([200, 824])

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_bar_layout)
        main_layout.addWidget(splitter)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def apply_theme(self):
        theme = self.config["theme"]
        if theme == "light":
            self.setStyleSheet("""
                QMainWindow { background-color: white; color: black; }
                QLineEdit { background-color: #f0f0f0; border-radius: 10px; padding: 5px; }
                QPushButton { background-color: #ff7961; color: white; border: none; }
                QListWidget { background-color: #f0f0f0; }
            """)
        else:
            self.setStyleSheet("""
                QMainWindow { background-color: #1e1e1e; color: white; }
                QLineEdit { background-color: #2d2d2d; border-radius: 10px; padding: 5px; }
                QPushButton { background-color: #3f51b5; color: white; border: none; }
                QListWidget { background-color: #2d2d2d; }
            """)

    def add_new_tab(self, qurl=None, label="New Tab"):
    # If qurl is None or invalid, default to Google
        if not qurl or not isinstance(qurl, QUrl):
        qurl = QUrl("https://www.google.com")
    
        browser = QWebEngineView()
        browser.setUrl(qurl)
        browser.urlChanged.connect(lambda url: self.update_tab_icon(browser, url))

        tab_index = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(tab_index)

        # Set favicon for the tab
        browser.iconChanged.connect(lambda: self.update_tab_icon(browser, browser.url()))
        self.update_tab_icon(browser, qurl)



    def close_tab(self):
        current_tab_index = self.sidebar.currentRow()
        if current_tab_index >= 0:
            self.tabs.pop(current_tab_index)
            self.sidebar.takeItem(current_tab_index)
            if self.tabs:
                self.browser.setUrl(self.tabs[-1])
            else:
                self.browser.setHtml("<h1>No Tabs Open</h1>")

    def switch_tab(self, item):
        index = self.sidebar.row(item)
        self.browser.setUrl(self.tabs[index])

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http") and not url.startswith("nebula:"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))
        current_tab_index = self.sidebar.currentRow()
        if current_tab_index >= 0:
            self.tabs[current_tab_index] = QUrl(url)

        # Update tab icon
        current_item = self.sidebar.item(current_tab_index)
        current_item.setIcon(QIcon(self.browser.icon()))
