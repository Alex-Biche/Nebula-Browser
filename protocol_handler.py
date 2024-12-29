class ProtocolHandler:
    def handle(self, browser, url):
        page = url[len("nebula://"):]
        if page == "home":
            browser.setHtml("<h1>Welcome to Nebula</h1><p>This is a Nebula-specific page.</p>")
        elif page.startswith("about"):
            browser.setHtml("<h1>About Nebula</h1><p>This browser is designed for innovation.</p>")
        else:
            browser.setHtml("<h1>404 - Page Not Found</h1>")
