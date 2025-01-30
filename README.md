Nebula Browser

Nebula Browser is a fully open-source, modular web browser designed to provide flexibility and customization while integrating a decentralized Nebula Web system.

Features

Modular Design: Core browser, GUI, and networking components are separate, allowing for customization and swapping.

Custom GUI Support: Users can develop and use their own graphical interfaces.

Nebula Web Integration: Built-in NDNS (Nebula Domain Name Service) and NRS (Nebula Relay Service) for a unique browsing experience.

Package Manager & Build System: Install, update, and build components into a single executable.

Project Structure

/nebula_browser
 ├── /core_browser      # Main browser engine
 ├── /gui               # GUI system (separate from core)
 ├── /build_system      # Handles installation and packaging
 ├── /nebula_web        # Nebula networking (NDNS & NRS)
 ├── /config            # Stores user settings
 ├── /docs              # Documentation

Installation

Clone the repository:

git clone https://github.com/Alex-Biche/Nebula-Browser/

Navigate to the project directory:

cd nebula-browser

Install dependencies:

pip install -r requirements.txt

Run the browser:

python core_browser/main.py

License

Nebula Browser is licensed under the MIT License GPL V3.

Contributing

Contributions are welcome! Feel free to fork the repository, submit issues, and create pull requests.

Contact

For questions or collaboration, reach out via nebula@alexbiche.one
