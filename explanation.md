1- extract text from Images in python with pillow and pytesseract
2- pip install pytesseract pillow

1. pytesseract
Purpose: pytesseract is a Python wrapper for Google's Tesseract-OCR engine, used for Optical Character Recognition (OCR). It converts images of text into machine-readable text.
Role in the Script: Likely used to extract text from images. You might see functions like pytesseract.image_to_string for this purpose.
2. PIL (from Pillow)
Purpose: Pillow is a Python Imaging Library fork that provides tools for opening, manipulating, and saving image files.
Role in the Script: Handles image loading and processing. For example:
Opening an image: Image.open('file_path')
Preprocessing before passing the image to pytesseract.
3. json
Purpose: Provides tools for working with JSON (JavaScript Object Notation), a common data-interchange format.
Role in the Script: Likely used to structure or save the OCR output in JSON format for easier data handling or integration with other systems.
4. sys
Purpose: Offers access to system-specific parameters and functions.
Role in the Script: Often used to handle command-line arguments (sys.argv) or interact with the Python runtime environment.
