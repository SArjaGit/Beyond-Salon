---
title: Beyond Salon
emoji: 👀
colorFrom: indigo
colorTo: gray
sdk: gradio
sdk_version: 5.9.1
app_file: app.py
pinned: false
---

# Beyond Salon

## Project Objective:

Beyond Salon is a web application that allows users to upload an image and select a hair color to see how the color suits them. The application uses Gradio for the user interface and Hugging Face Spaces for deployment.

## Project Goals
- The Goal is to either create or use existing models to figure out the hair masking in each image and then apply the hair transformation to the hair.
- Used existing models from segment_anything and diffusers
  
## Files
* [Gradio_UI.ipynb](https://github.com/SArjaGit/Project-3/blob/Read-me-Branch/Gradio_UI.ipynb) - User Interface for handling the input and applying the transformation
* [app.py](https://github.com/SArjaGit/Beyond-Salon/blob/main/app.py) - Hugging Face Spaces setup file (Gradio_UI.ipynb reconstituted to be used in Hugging Face Spaces)
* [/lib/hair.py](https://github.com/SArjaGit/Project-3/blob/main/lib/hair.py) - Main class that creates the hair mask and applies transformation
* [/lib](https://github.com/SArjaGit/Beyond-Salon/tree/main/lib) - Houses the python library files
* [/output](https://github.com/SArjaGit/Beyond-Salon/tree/main/output) - The folder where images are outputed
* [/uploaded_images](https://github.com/SArjaGit/Beyond-Salon/tree/main/uploaded_images) - The folder where uploaded images are stored

## Features

- Upload an image of yourself (we suggest a photograph closely-cropped to your head).
- Select a hair color from a dropdown menu.
- See the transformed image with the selected hair color.

## Notes

- On first run of the software, it will download the sam_vit_h_4b8939.pth file to be used with SegmentAnything.  It is a 2gb file and may take some time to download.

## Requirements

- Python 3.7+
- SegmentAnything
- Gradio
- Pillow
- OpenCV
- NumPy
- Webcolors
- Spaces

## Local Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SArjaGit/Beyond-Salon.git
    cd Beyond-Salon
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Local Usage

Run the Gradio_UI.ipynb file in VSCode or Jupyterlab

## Hugging Face (Remote Usage)

This code is deployed to a Hugging Face Space which can be accessed here: [https://huggingface.co/spaces/dailyinvention/beyondsalon](https://huggingface.co/spaces/dailyinvention/beyondsalon)
