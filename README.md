# Extract Text from Image

## Overview
This Python script extracts text from an image file and saves it to a JSON file. It uses the `Pillow` library for image handling and `pytesseract` for Optical Character Recognition (OCR).

## Prerequisites
1. Install Python (version 3.6 or higher is recommended).
2. Install Tesseract-OCR:
   - For Windows, download and install Tesseract-OCR from [Tesseract's official repository](https://github.com/tesseract-ocr/tesseract).
   - For Linux, install Tesseract using your package manager (e.g., `sudo apt install tesseract-ocr`).
   - For macOS, use Homebrew: `brew install tesseract`.

## Installation
1. Clone or download this repository.
2. Install the required Python libraries using pip:
   ```bash
   pip install pillow pytesseract
   ```

## Usage
1. Save your image file in a known location.
2. Run the script with the following command:
   ```bash
   python script.py <image_path> <output_json_path>
   ```
   - `<image_path>`: Path to the image file you want to process.
   - `<output_json_path>`: Path to save the JSON file containing the extracted text.

### Example
```bash
python script.py sample_image.png output.json
```

This will extract the text from `sample_image.png` and save it to `output.json`.

## Output
The output JSON file will have the following structure:
```json
{
    "extracted_text": "Your extracted text here."
}
```

## Error Handling
- If the image file is not found, an error message will be displayed.
- Other errors will also be reported in the terminal.

## Notes
- The accuracy of the text extraction depends on the quality and clarity of the image.
- You can improve recognition by preprocessing the image (e.g., converting it to grayscale).

## License
This project is open-source and available under the MIT License.



