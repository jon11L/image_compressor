from PIL import Image
import os
import time

def compress_images(input_dir, output_dir, quality=int):
    '''takes images and compress them into a new diretory, with a parameter to adjust the compression size.'''

    # Check if input dictionary is existing before proceeding.
    while True:
        try:
            # If input directory doesn't exist/not found, then error is raise and user prompted to enter it again.
            if not os.path.exists(input_dir):
                raise FileNotFoundError(f"directory '{input_dir}' could not be found or does not exist.")
            break           
        except FileNotFoundError as e:
            print(e)
            input_dir = input("Please enter a valid input directory path: ")

    # Create the output directory if it doesn't exist.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Directory exist, process the image files
    start_time = time.time()
    for filename in os.listdir(input_dir):

        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            filepath = os.path.join(input_dir, filename)
            image = Image.open(filepath)

            # Compress and save the image
            output_path = os.path.join(output_dir, filename)
            try:
                image.save(output_path, "JPEG", quality=quality)
                end_time = time.time()
                timing = end_time - start_time 
                print(f"")
                print(f"Compressed and saved to: {output_path}. In {round(timing, 4)}s") # In {timing} time
            except Exception as save_error:
                print(f"Failed to save {output_path}: {save_error}")


if __name__ == "__main__":
    input_directory = "path_to_your_input_directory"
    output_directory = "image_compressed" # If kept like this, that directory will be created where user currently is.
    quality = 30  # Adjust quality as needed, lower means more compression.

    compress_images(input_directory, output_directory, quality)
