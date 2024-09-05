from PIL import Image
import os

def compress_images(input_dir, output_dir, quality=int):
    '''takes images and compress them into a new diretory, with a parameter to adjust the compression size.'''
    # Create the output directory if it doesn't exist.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # check if input dictionary is existing before proceeding to compress images
    while True:
        try:
            # if input directory doesn't exist/not found, then error is raise and user prompted to enter it again.
            if not os.path.exists(input_dir):
                raise FileNotFoundError(f"directory '{input_directory}' could not be found or does not exist.")
            # directory exist, process the image files
            for filename in os.listdir(input_dir):
                if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
                    filepath = os.path.join(input_dir, filename)
                    image = Image.open(filepath)

                    # Compress and save the image
                    output_path = os.path.join(output_dir, filename)
                    image.save(output_path, "JPEG", quality=quality)

                    print(f"Compressed and saved to: {output_path}")
            # exit the loop after processing
            break

        except FileNotFoundError as e:
            print(e)
            input_dir = input("Please enter a valid input directory path: ")












        # Loop through all files in the input directory.
        # for filename in os.listdir(input_dir):
        #     if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
        #         filepath = os.path.join(input_dir, filename)
        #         image = Image.open(filepath)

        #         # Compress and save the image
        #         output_path = os.path.join(output_dir, filename)
        #         image.save(output_path, "JPEG", quality=quality)

        #         print(f"Compressed and saved: {output_path}")


if __name__ == "__main__":
    input_directory = "path_to_your_input_directory"
    output_directory = "image_compressed"
    quality = 30  # Adjust quality as needed, lower means more compression.

    compress_images(input_directory, output_directory, quality)
