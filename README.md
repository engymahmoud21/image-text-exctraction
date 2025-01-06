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
1. Modify the Image Path and Output File Path
At the beginning of the program, you will find the following lines where the image path and the output file path are defined:

image_path = "C:/Users/Enjy/Downloads/New folder/i.png"  # Replace with your image path
output_json_path = "C:/Users/Enjy/Downloads/New folder/output.json"  # Replace with your desired JSON output path
2. Run the Program
After ensuring the image and JSON file paths are correct, run the program. The program will:

Read the image from the specified path.
Extract text using Tesseract OCR.
Save the extracted text into a JSON file.
3. Output JSON File Format
After running the program successfully, the extracted text will be saved in a JSON file in the following format:

{
    "extracted_text": "This will be the extracted text from the image"
}

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



