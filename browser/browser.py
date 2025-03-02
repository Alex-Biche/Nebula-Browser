# browser/browser.py
import tkinter as tk
from tkinter import scrolledtext
import nebula_engine

class NebulaBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Nebula Browser")
        self.root.geometry("800x600")
        
        # Create toolbar
        self.toolbar = tk.Frame(root, bg="lightgray")
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Create address bar
        self.address_var = tk.StringVar()
        self.address_var.set("https://example.com")
        self.address_bar = tk.Entry(self.toolbar, textvariable=self.address_var, width=80)
        self.address_bar.pack(side=tk.LEFT, padx=5, pady=5)
        self.address_bar.bind("<Return>", self.navigate)
        
        # Create navigation buttons
        self.go_button = tk.Button(self.toolbar, text="Go", command=self.navigate)
        self.go_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Create content area
        self.content_area = scrolledtext.ScrolledText(root)
        self.content_area.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    
    def navigate(self, event=None):
        url = self.address_var.get()
        self.content_area.delete(1.0, tk.END)
        self.content_area.insert(tk.END, f"Loading {url}...\n\n")
        
        try:
            # Fetch and parse the page
            html_content = nebula_engine.fetch_page(url)
            parsed_content = nebula_engine.parse_page(html_content)
            
            # Display the content
            self.content_area.delete(1.0, tk.END)
            self.content_area.insert(tk.END, parsed_content)
            
        except Exception as e:
            self.content_area.delete(1.0, tk.END)
            self.content_area.insert(tk.END, f"Error loading page: {str(e)}")

def run():
    root = tk.Tk()
    browser = NebulaBrowser(root)
    root.mainloop()

if __name__ == "__main__":
    run()