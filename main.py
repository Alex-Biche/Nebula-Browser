import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "build"))

import browser.browser as browser
import nebula_engine  # Now it should work


if __name__ == "__main__":
    browser.run()
