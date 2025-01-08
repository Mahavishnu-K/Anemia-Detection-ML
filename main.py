import yaml
from pathlib import Path
from src.matlab_integration import process_image_in_matlab
from src.feature_extraction import extract_features  
from src.classification import classify_image 

def main():
    # Load config file
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Get the paths from config and convert to Path objects
    raw_data_path = Path(config['paths']['raw_data'])
    processed_data_path = Path(config['paths']['processed_data'])

    # Example: Process an image using MATLAB
    image_path = raw_data_path / "sample_image.png"  # Using pathlib to join paths
    processed_image = process_image_in_matlab(image_path)

    # Example: Extract features (MATLAB or Python)
    features = extract_features(processed_image)

    # Example: Classify the image (using Python-based model)
    prediction = classify_image(features)

    print(f"Prediction: {prediction}")

if __name__ == "__main__":
    main()
