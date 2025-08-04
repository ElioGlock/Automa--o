import pyautogui
import time
from PIL import Image, ImageGrab
import pytesseract
import sys


TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
APP_ICON_IMG = "imtem/app.png"
PLAY_BUTTON_IMG = "imtem/play.png"
VIDEO_PLAYER_IMG = "imtem/video.png"
BACK_BUTTON_IMG = "imtem/back.png"

VIDEO_DURATION_REGION = (1322, 843, 1363, 874)
DEFAULT_CONFIDENCE = 0.9
SHORT_WAIT = 2
MEDIUM_WAIT = 4
SCROLL_AMOUNT = -2100  # -900,-2100,3300
OCR_CONFIG = r"--psm 7 -c tessedit_char_whitelist=0123456789:"


def read_image():
    img = Image.open("imtem/captura_regiao.png")
    img_cinza = img.convert("L")
    configs = r"--psm 7 -c tessedit_char_whitelist=0123456789:"
    texto_extraido = pytesseract.image_to_string(img_cinza, config=configs)
    return texto_extraido


def take_print():
    box = (1322, 843, 1363, 874)  # ajust on notebook
    image_reg = ImageGrab.grab(bbox=box)
    image_reg.show()
    image_reg.save("imtem/captura_regiao.png")


def convert(texto_extraido):
    partes = texto_extraido
    segundos = int(str(partes[0] + partes[1])) * 60 + int(str(partes[3] + partes[4]))
    return segundos


def click_image(image_path: str, conf: float = DEFAULT_CONFIDENCE) -> bool:
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=conf)
        if location:
            pyautogui.click(location)
            return True
        return False
    except pyautogui.ImageNotFoundException:
        return False


# --- LÓGICA PRINCIPAL ---

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

if not click_image(APP_ICON_IMG):
    sys.exit("App não encontrado. Abortando.")
time.sleep(SHORT_WAIT)
pyautogui.moveTo(1000, 500)
pyautogui.scroll(SCROLL_AMOUNT)
time.sleep(SHORT_WAIT)

play_buttons = list(pyautogui.locateAllOnScreen(PLAY_BUTTON_IMG, confidence=0.9))
print(f"Botões de 'play' encontrados: {len(play_buttons)}")


for button_pos in play_buttons:
    
    pyautogui.click(pyautogui.center(button_pos))
    time.sleep(10)

    take_print()
    read = read_image()
    converted = convert(read)
    print(f"Duração extraída: {converted} segundos")
    
    click_image(VIDEO_PLAYER_IMG)
    
    if converted > 0:
        # Use time.sleep(video_duration) para esperar o tempo real
        time.sleep(7)  # Espera fixa de 5s para teste rápido

    click_image(BACK_BUTTON_IMG)

    time.sleep(SHORT_WAIT)
    pyautogui.scroll(SCROLL_AMOUNT)
    time.sleep(SHORT_WAIT)
