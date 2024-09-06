from PIL import Image, ImageOps
import os
import time

def compress_images(input_dir: str, output_dir: str, quality:int = 30):
    '''Compresses images from the input directory and saves them to the output directory. 
    - input_dir (the directory where the program will look for the images to be compressed.)
    - output_dir (Where the compressed images will be stored, if this directory does not exist it will then be created.)
    - quality (allow to adjust the compression level // value: 1 - 95 , the lower the more compression, also more possible quality loss.)
    '''
    # Check if input dictionary is existing before proceeding, if not prompt the user to input.
    while not os.path.exists(input_dir):
        print(f"directory '{input_dir}' could not be found or does not exist.")
        input_dir = input("Please enter a valid input directory path: ")

    # some details feature, how many files were compressed and the total time it took.
    start_time = time.time()
    compressed_count = 0

    for filename in os.listdir(input_dir):

        if filename.lower().endswith((".jpg",".jpeg", ".png")):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            # Compress and save the image
            try:
                with Image.open(input_path) as img:
                    img = ImageOps.exif_transpose(img)

                    os.makedirs(output_dir, exist_ok=True)
                    img.save(output_path, "JPEG", quality=quality, optimize=True)
                    compressed_count += 1
                    print(f"Compressed: {output_path}") 
            except Exception as e:
                print(f"Failed to compressed and or save the file: {output_path}: \n {e}")

    end_time = time.time()
    if compressed_count > 0:
        print(f"Compression done!  In {round(end_time - start_time, 3)}s.  \nSaved to: {output_dir}.")
        print(f"{compressed_count} images compressed.")
    else:
        print("no images were compressed.")


if __name__ == "__main__":
    input_directory = "path_to_your_input_directory"
    output_directory = "image_compressed" # If kept like this, that directory will be created where user currently is.
    quality = 30

    compress_images(input_directory, output_directory, quality)
