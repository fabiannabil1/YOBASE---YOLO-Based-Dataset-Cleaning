# YOLO Cleaner: Smart Image Filtering with YOLO

YOLO Cleaner is a Python utility that leverages the power of the YOLO (You Only Look Once) model to automatically scan through image folders and remove images that do not contain a person. With options for multithreading and adjustable detection parameters, this tool streamlines the process of curating datasets or cleaning up image collections.

---

## Features

- **Automatic Person Detection:** Uses the YOLO model to detect the presence of people in images.
- **Automatic Cleanup:** Deletes images where no person is detected.
- **Adjustable Confidence Threshold:** Easily set the detection confidence via command-line arguments.
- **Multithreading Support:** Optionally process multiple folders concurrently. You can choose to set the number of threads manually or let it default to the number of folders.
- **Flexible Folder Input:** Provide one or more image folder paths to process.

---

## Requirements

- Python 3.6 or higher
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) package  
- Other standard libraries: `os`, `argparse`, `concurrent.futures`

You can install the required YOLO package using pip:

```bash
pip install ultralytics
```

---

## Installation

1. **Clone the repository or download the script.**

2. **Ensure all dependencies are installed:**

   ```bash
   pip install ultralytics
   ```

3. **Place your YOLO model file (e.g., `best.pt`) in an accessible directory or provide its path when running the script.**

---

## Usage

Run the script from your terminal with the required arguments:

```bash
python script.py --model_path best.pt --conf 0.4 --image_folders "folder1" "folder2" "folder3"
```

### Command-Line Arguments

- `--model_path`:  
  Path to the YOLO model (default is `best.pt`).

- `--conf`:  
  Confidence threshold for detection (default is `0.4`).

- `--image_folders`:  
  List of folders containing images (required). Separate multiple folders with a space.

- `--multithread`:  
  Enable multithreading to process folders concurrently.

- `--num_threads`:  
  Specify the number of threads to use. If not provided, it defaults to the number of input folders.

### Example with Multithreading

To enable multithreading and process folders concurrently (e.g., using 2 threads):

```bash
python script.py --model_path best.pt --conf 0.4 --multithread --num_threads 2 --image_folders "folder1" "folder2" "folder3"
```

---

## How It Works

1. **Model Loading:**  
   The script loads a YOLO model from the specified path.

2. **Image Processing:**  
   For each image in the provided folders, the script runs the YOLO model with the specified confidence threshold to detect persons.

3. **Image Filtering:**  
   If no person is detected in an image, the script deletes that image from the folder.

4. **Optional Multithreading:**  
   When multithreading is enabled, the script processes multiple folders concurrently, improving performance on larger datasets.

---

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests. Please adhere to standard coding practices and include comments where necessary.

---

## License


---

## Contact

For any inquiries or suggestions, please reach out via the repository’s issue tracker or contact the maintainer directly.