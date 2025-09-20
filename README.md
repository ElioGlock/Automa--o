# Python Automation and Scraping Projects

This repository contains a collection of scripts demonstrating skills in GUI automation and web scraping using Python. Each project is designed to solve a specific automation task, from extracting data from websites to controlling desktop applications through image recognition and OCR.

## 🚀 Projects Included

Here is a summary of each project:

### 1\. IBGE State Data Scraper (`Extraindo_dados.py`)

  * **Description:** A web scraping script that extracts key statistical indicators for any Brazilian state (UF) from the official IBGE (Brazilian Institute of Geography and Statistics) website. The extracted data is then cleaned and organized into a Pandas DataFrame.
  * **Libraries & Concepts Demonstrated:**
      * `requests`: For making HTTP requests to the website.
      * `BeautifulSoup`: For parsing HTML content and extracting data.
      * `pandas`: For structuring the final data into a DataFrame.
      * Web Scraping, HTML Parsing, and Data Cleaning.

### 2\. Ulife Portal Login Automation (`ulife.py`)

  * **Description:** A GUI automation script that automates the login process for the "Ulife" student portal. It uses image recognition to find and interact with on-screen elements like buttons and input fields. The script can handle both scenarios where the user is already logged in (by logging out first) or is completely logged out.
  * **Libraries & Concepts Demonstrated:**
      * `pyautogui`: For controlling the mouse and keyboard, and for on-screen image recognition.
      * `os`, `sys`: For handling file paths correctly, especially when bundled into an executable.
      * GUI Automation and Exception Handling (`try...except`).

### 3\. Automated Video Watcher with OCR (`evolucao.py`)

  * **Description:** An advanced GUI automation script designed to automatically play a series of videos within a desktop application. It locates all "play" buttons on the screen, and for each video, it captures a screenshot of the time display, uses OCR to read the video's duration, and "watches" it before moving to the next.
  * **Libraries & Concepts Demonstrated:**
      * `pyautogui`: For screen control and image location.
      * `Pillow (PIL)`: For capturing and processing screen regions.
      * `pytesseract`: For performing Optical Character Recognition (OCR) to read text from images.
      * Advanced Process Automation and System Integration (Python + Tesseract).

## 🛠️ Setup and Installation

To run these scripts, you need Python 3 installed, along with the required libraries.

1.  **Install Python Libraries:**

    ```bash
    pip install requests beautifulsoup4 pandas pyautogui pillow pytesseract
    ```

2.  **Install Tesseract-OCR Engine:**
    The `evolucao.py` script requires the Tesseract-OCR engine to be installed on your system (it is not a Python package).

      * You can download it from the official [Tesseract GitHub repository](https://github.com/tesseract-ocr/tessdoc).
      * After installation, you must update the `TESSERACT_PATH` variable in the `evolucao.py` script to point to your `tesseract.exe` file location.

## ▶️ How to Use

### IBGE Scraper

1.  Open `Extraindo_dados.py`.
2.  Change the state abbreviation in the line `state = scrapping_uf("sp")` to your desired state (e.g., "rj", "mg").
3.  Run the script: `python Extraindo_dados.py`.

### Automation Scripts (`ulife.py` and `evolucao.py`)

1.  **Place Image Files:** Ensure that all the required `.png` image files are present in the correct subfolders (`images/` for `ulife.py` and `imtem/` for `evolucao.py`).
2.  **Modify Script Constants:** You will likely need to modify hardcoded values like screen coordinates (`VIDEO_DURATION_REGION`) and scroll amounts (`SCROLL_AMOUNT`) in `evolucao.py` to match your screen resolution and application layout.
3.  **Update Credentials (Important):** In `ulife.py`, the student ID is hardcoded (`pyautogui.write("202512408")`). You must change this to your own.
4.  Run the desired script:
    ```bash
    python ulife.py
    ```
    ```bash
    python evolucao.py
    ```

-----

**Disclaimer:** The GUI automation scripts are highly dependent on screen resolution, application window size, and the visual appearance of UI elements. If the target application's interface changes, or if you run it on a different computer, you will need to recapture the screen images and adjust coordinates for the scripts to work.
