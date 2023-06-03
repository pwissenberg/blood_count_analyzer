"""This module extracts with OCR the information from teh scanned files in the scanned pdf."""
from pathlib import Path

# from pytesseract import image_to_string
import pytesseract
import tabula
from pdf2image import convert_from_path
from pdfminer.high_level import extract_text, extract_pages
import requests
import json
import cv2
from PIL import Image

pdf_path = Path(
    r"C:\Users\PW\programs\blood_count_analyzer\blood_analyzer\Bluttest-24-2-23.pdf"
)


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\PW\AppData\Local\Programs\Tesseract-OCR"
)

images = convert_from_path(pdf_path)

final_text = ""
for pg, img in enumerate(images):
    final_text += pytesseract.image_to_string(img)

print(final_text)
