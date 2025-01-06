import pytesseract
from PIL import Image
import json
import os

def extract_text_from_image(image_path, output_json_path):
    """
    Extracts text from an image and saves it to a JSON file.

    Parameters:
    - image_path: str, path to the input image.
    - output_json_path: str, path to save the extracted text as a JSON file.
    """
    # Check if the input image exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file '{image_path}' does not exist.")

    # Open the image using PIL
    image = Image.open(image_path)

    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(image)

    # Create a dictionary to store the extracted text
    data = {
        "extracted_text": extracted_text
    }

    # Write the dictionary to a JSON file
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(f"Extracted text has been saved to '{output_json_path}'.")

# Example usage
if __name__ == "__main__":
    image_path = "C:/Users/Enjy/Downloads/New folder/text-editor-with-fonts.png"  # Replace with your image path
    output_json_path = "C:/Users/Enjy/Downloads/New folder/output.json"  # Replace with your desired JSON output path

    try:
        extract_text_from_image(image_path, output_json_path)
    except Exception as e:
        print(f"An error occurred: {e}")
