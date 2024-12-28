import spaces
from lib.hair import look_maker
import gradio as gr
from PIL import Image
import os
import torch

UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)
#image = "source_data/Roberta.jpg"

@spaces.GPU
# Define the function to transform hair color
def transform_hair(image, color):

    # Define the directory for uploaded images
    image_path = os.path.join(UPLOAD_DIR, "uploaded_image.jpg")

    # Save the uploaded image to a temporary file
    image.save(image_path)

    print(f"Image saved to: {image_path}")

    # Call the set_hair_color method with the image path and color
    output_path = look_maker.hair_transform(color, image_path)

    output_path = "output/colored_hair.png"

    print(f"Output path: {output_path}")

    if output_path and os.path.exists(output_path):
        # Load the transformed image to return it
        transformed_image = Image.open(output_path)
        # Clean up the temporary file

        return transformed_image
    else:
        raise ValueError("Failed to generate transformed image")

    return transformed_image


print(f"Is CUDA available: {torch.cuda.is_available()}")
# True
print(f"CUDA device: {torch.cuda.get_device_name(torch.cuda.current_device())}")
# Tesla T4

# Create a Gradio interface
iface = gr.Interface(
    fn=transform_hair,
    inputs=[
        #gr.Image("source_data/Roberta.jpg"),
        gr.Image(type="pil", label="Input Image"),
        gr.Dropdown(choices=['blue', 'red', 'green', 'yellow', 'purple', 'pink', 'orange', 'brown', 'black', 'white','gray', 'cyan', 'magenta'], label="Hair Color")
    ],
    outputs=gr.Image(type="pil", label="Transformed Image"),
    title="Beyond Salon",
    description="Upload an image and select a hair color to see how the color suits.",
    article="<p style='text-align: center;'>bring life to your hair!!</p>"
)


# Launch the interface
iface.launch(share=True)
