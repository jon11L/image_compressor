# Image compressor

I have originally created this python script with the help of chatGPT to compress some photos/images i had to send. As they contained confidential data, i did not want to put them through these 3rd party websites.

## How the Program Works:

1. **Imports**: It imports the necessary libraries (`PIL` for image processing and `os` for file handling).


2. **`compress_images` function**:
   - It reads all files in the `input_dir`.
   - For each image with a `.jpg` or `.jpeg` extension, it opens the image using `PIL`.
   - It compresses the image by saving it in the `output_dir` with the specified `quality` (30 by default, where 100 is the best quality and 1 is the worst).
3. **Main section**: It defines the input and output directories and calls the `compress_images` function.


### How to Use:
1. Replace `"path_to_your_input_directory"` with the path to the directory containing the images you want to compress.
2. Replace `"path_to_your_output_directory"` with the path to the directory where you want to save the compressed images.
3. Adjust the `quality` parameter if needed (lower values result in higher compression and smaller files, but with lower image quality).

When you run the script, it will compress the images in the specified directory and save the compressed versions in the output directory.


#### info : Tested with jpg files of a size about 2.5mb and turned to 200-300kb successfully.
