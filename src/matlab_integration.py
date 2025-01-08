import matlab.engine
from pathlib import Path

def start_matlab_engine():
    """Starts the MATLAB engine for Python."""
    eng = matlab.engine.start_matlab()
    return eng

def call_matlab_function(function_name, *args):
    """Calls a MATLAB function from Python."""
    eng = start_matlab_engine()

    # Assuming the MATLAB function is in the current path
    result = getattr(eng, function_name)(*args, nargout=1)  # Call the function with arguments
    eng.quit()
    return result

def process_image_in_matlab(image_path):
    """Call a MATLAB function to process an image."""
    result = call_matlab_function('process_image', str(image_path))
    return result

if __name__ == "__main__":
    # Example of processing an image using pathlib
    image_path = Path("data/raw/sample_image.png")
    processed_image = process_image_in_matlab(image_path)
    print(f"Processed Image: {processed_image}")
