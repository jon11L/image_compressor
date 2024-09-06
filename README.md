# *Image compressor*

## How the Program Works:

1. **Imports**: imports the necessary libraries (`PIL` for image processing and `os` for file handling).


2. **`compress_images` function**:
   - It reads all files in the `input_dir`.
   - For each image with a `.jpg` or `.jpeg` extension, it opens the image using `PIL`.
   - It compresses the image by saving it in the `output_dir` with the specified `quality` (30 by default, where 100 is the best quality and 1 is the worst).
3. **Main section**: It defines the input and output directories and calls the `compress_images` function.


## How to Use:



1. For `input_dir` Replace `"path_to_your_input_directory"` with the path to the directory containing the images you want to compress. 

2. for the `output_dir` Replace `"compressed_image"` with the path to the directory where you want to save the compressed images. or this will be 'compressed_image' will be created in the current directory

3. Adjust the `quality` parameter if needed (lower values result in higher compression and smaller files, but with lower image quality).


### extra info:
 Tested with jpg files of a size about 2.5mb and turned to 200-300kb successfully.

For the paths input:
- Full Path: e.g., "C:/Users/YourUsername/Images" or "/home/yourusername/images"
- Relative Path: e.g., "images" (for a directory within the current working directory)


