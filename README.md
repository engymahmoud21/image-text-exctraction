# Extract Text from Image

## Overview
This Python script extracts text from an image file and saves it to a JSON file. It uses the `Pillow` library for image handling and `pytesseract` for Optical Character Recognition (OCR).

## Prerequisites
1. Install Python (version 3.6 or higher is recommended).
2. Install Tesseract-OCR:
   - For Windows, download and install Tesseract-OCR from [Tesseract's official repository](https://github.com/tesseract-ocr/tesseract). then edit the paths of the program "Tesseract"
   - For Linux, install Tesseract using your package manager (e.g., `sudo apt install tesseract-ocr`).
   - For macOS, use Homebrew: `brew install tesseract`.

## Installation
1. Clone or download this repository.
2. Install the required Python libraries using pip:
   ```bash
   pip install pillow pytesseract
   ```


## How to Use

### 1. Modify the Image Path and Output File Path
In the program, you'll find these lines to define the image and output file paths:

```python
image_path = "C:/Users/Enjy/Downloads/New folder/i.png"  # Your image path
output_json_path = "C:/Users/Enjy/Downloads/New folder/output.json"  # Your output JSON path
```

Replace them with your own paths.

### 2. Run the Program
After updating the paths, run the program. It will:

- Open the image from the specified path.
- Extract text from the image using Tesseract OCR.
- Save the extracted text to a JSON file.

### 3. Output JSON Format
The extracted text will be saved in a JSON file like this:

```json
{
    "extracted_text": "This is the text extracted from the image."
}
```

## how to use for the 2 Usage
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
If the image file is not found at the specified path, you will get an error message. Make sure the image path is correct..

## Notes
- The accuracy of the text extraction depends on the quality and clarity of the image.
- You can improve recognition by preprocessing the image (e.g., converting it to grayscale).

## License
This project is open-source and available under the MIT License.



