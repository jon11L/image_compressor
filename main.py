from PIL import Image
import os

def compress_images(input_dir, output_dir, quality=30):
    '''takes images and compress them into a new diretory, with a parameter to adjust the compression size.'''
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            filepath = os.path.join(input_dir, filename)
            image = Image.open(filepath)

            # Compress and save the image
            output_path = os.path.join(output_dir, filename)
            image.save(output_path, "JPEG", quality=quality)

            print(f"Compressed and saved: {output_path}")

if __name__ == "__main__":
    input_directory = "images_raw"
    output_directory = "compressed_images"
    quality = 30  # Adjust quality as needed, lower means more compression

    compress_images(input_directory, output_directory, quality)
