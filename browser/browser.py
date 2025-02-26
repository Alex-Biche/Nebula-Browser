import nebula_engine

print("Starting Nebula Browser...")

def run():
    print("Running the browser...")

    # Simulate a webpage fetch
    page_content = nebula_engine.fetchPage("https://example.com")
    print(page_content)

# Uncomment to actually run the browser when main.py is executed
if __name__ == "__main__":
    run()
