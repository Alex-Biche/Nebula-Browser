import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QTabWidget, QLineEdit, QPushButton, QToolBar, QAction
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl

class NebulaBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nebula Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Toolbar
        self.toolbar = QToolBar("Navigation")
        self.addToolBar(self.toolbar)

        # Add navigation buttons
        back_action = QAction("Back", self)
        back_action.triggered.connect(self.navigate_back)
        self.toolbar.addAction(back_action)

        forward_action = QAction("Forward", self)
        forward_action.triggered.connect(self.navigate_forward)
        self.toolbar.addAction(forward_action)

        reload_action = QAction("Reload", self)
        reload_action.triggered.connect(self.reload_page)
        self.toolbar.addAction(reload_action)

        home_action = QAction("Home", self)
        home_action.triggered.connect(self.navigate_home)
        self.toolbar.addAction(home_action)

        # Address bar
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)
        self.toolbar.addWidget(self.address_bar)

        # New Tab Button
        new_tab_action = QAction("New Tab", self)
        new_tab_action.triggered.connect(self.add_new_tab)
        self.toolbar.addAction(new_tab_action)

        # Tab widget
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_address_bar)
        self.layout.addWidget(self.tabs)

        # Open the first tab
        self.add_new_tab(QUrl("https://www.google.com"), "Home")

    def add_new_tab(self, qurl=None, label="New Tab"):
        if qurl is None:
            qurl = QUrl("https://www.google.com")
        
        browser = QWebEngineView()
        browser.setUrl(qurl)
        browser.urlChanged.connect(lambda url: self.update_tab_icon(browser, url))

        tab_index = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(tab_index)

        # Set favicon for the tab
        browser.iconChanged.connect(lambda: self.update_tab_icon(browser, browser.url()))
        self.update_tab_icon(browser, qurl)

    def update_tab_icon(self, browser, url):
        # Update tab favicon when available
        icon = browser.icon()
        if not icon.isNull():
            index = self.tabs.indexOf(browser)
            self.tabs.setTabIcon(index, icon)

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def navigate_back(self):
        current_browser = self.get_current_browser()
        if current_browser:
            current_browser.back()

    def navigate_forward(self):
        current_browser = self.get_current_browser()
        if current_browser:
            current_browser.forward()

    def reload_page(self):
        current_browser = self.get_current_browser()
        if current_browser:
            current_browser.reload()

    def navigate_home(self):
        current_browser = self.get_current_browser()
        if current_browser:
            current_browser.setUrl(QUrl("https://www.google.com"))

    def load_url(self):
        current_browser = self.get_current_browser()
        if current_browser:
            url = QUrl(self.address_bar.text())
            if url.scheme() == "":
                url.setScheme("http")
            current_browser.setUrl(url)

    def update_address_bar(self, index):
        current_browser = self.get_current_browser()
        if current_browser:
            url = current_browser.url()
            self.address_bar.setText(url.toString())

    def get_current_browser(self):
        return self.tabs.currentWidget()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = NebulaBrowser()
    browser.show()
    sys.exit(app.exec_())
