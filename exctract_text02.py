import pytesseract
from PIL import Image
import json
import sys

def extract_text_from_image(image_path, output_json_path):
    try:
        # Open the image file
        image = Image.open(image_path)

        # Use pytesseract to perform OCR on the image
        extracted_text = pytesseract.image_to_string(image)

        # Create a dictionary to store the extracted text
        output_data = {
            "extracted_text": extracted_text
        }

        # Write the dictionary to a JSON file
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(output_data, json_file, indent=4, ensure_ascii=False)

        print(f"Text successfully extracted and saved to {output_json_path}")

    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the user provided the necessary arguments
    if len(sys.argv) != 3:
        print("Usage: python extract_text_from_image.py <image_path> <output_json_path>")
    else:
        image_path = sys.argv[1]
        output_json_path = sys.argv[2]
        extract_text_from_image(image_path, output_json_path)