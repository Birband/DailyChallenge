import pathlib
from PIL import Image
import numpy as np

INPUT_FOLDER = pathlib.Path("INPUT")
OUTPUT_FOLDER = pathlib.Path("OUTPUT")
CHUNK_SIZE = 8

def initialize_directories() -> None:
    INPUT_FOLDER.mkdir(exist_ok=True)
    OUTPUT_FOLDER.mkdir(exist_ok=True)


def load_image(image_name : str) -> Image:
    image_path = INPUT_FOLDER / image_name
    if not image_path.exists():
        raise FileNotFoundError(f"Image {image_name} not found")
    
    image = Image.open(image_path)
    return image
    
def prepare_image(image : Image) -> np.ndarray:
    image = image.convert("RGB")
    image_array = np.array(image)
    return image_array

def process_image(image_array : np.ndarray, filename: str = "output.jpg") -> np.ndarray:
    for i in range(0, image_array.shape[0], CHUNK_SIZE):
        for j in range(0, image_array.shape[1], CHUNK_SIZE):
            chunk = image_array[i:i+CHUNK_SIZE, j:j+CHUNK_SIZE]
            average_color = np.mean(chunk, axis=(0, 1))
            image_array[i:i+CHUNK_SIZE, j:j+CHUNK_SIZE] = average_color
                
    new_image = Image.fromarray(image_array)
    new_image.save(OUTPUT_FOLDER / filename)

def main():
    initialize_directories()

    file_name = "example.jpg"

    image = prepare_image(load_image(file_name))

    process_image(image, file_name)

    print("Done!")
    

if __name__ == "__main__":
    main()