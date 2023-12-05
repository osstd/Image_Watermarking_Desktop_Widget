from tkinter import filedialog


def save_image(image):
    # Prompt user for save location
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

    # Save the image
    if save_path:
        image.save(save_path)
