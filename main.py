from image_processor import ImageProcessor
from image_saver import save_image
from tkinter import Tk, Button, Entry, Label, filedialog, messagebox
from PIL import ImageTk


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking App")

        self.image_processor = None
        self.image_path = ""
        self.watermark_text = Entry(root, font=("Arial", 12), highlightthickness=0, width=25,
                                    borderwidth=0)  # Increase input text size

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Set window size and background color
        self.root.geometry("400x1000")
        self.root.configure(bg='lightcoral')

        # Load Image Button
        load_button = Button(self.root, text="Load Image", command=self.load_image, font=("Arial", 12, "bold"), bd=0)
        load_button.pack(pady=10)

        # Watermark Entry
        Label(self.root, text="Watermark Text:", font=("Arial", 18, "bold"), bg='lightcoral').pack()
        self.watermark_text.pack(pady=10)

        # Watermark Button
        watermark_button = Button(self.root, text="Watermark Image", command=self.watermark_image,
                                  font=("Arial", 10, "bold"), bd=0)
        watermark_button.pack(pady=10)

        # Save Image Button
        save_button = Button(self.root, text="Save Image", command=self.save_watermarked_image,
                             font=("Arial", 10, "bold"), bd=0)
        save_button.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png *.jpg *.jpeg")])

        if file_path:
            self.image_path = file_path
            self.image_processor = ImageProcessor(file_path)
            self.display_image()

    def display_image(self):
        if self.image_path and self.image_processor:
            image = self.image_processor.original_image
            image.thumbnail((300, 300))  # Resize for display
            photo = ImageTk.PhotoImage(image)

            # Update the displayed image
            img_label = Label(self.root, image=photo)
            img_label.image = photo
            img_label.pack()

    def watermark_image(self):
        if not self.image_path or not self.image_processor:
            messagebox.showerror("Error", "Please load an image first.")
            return

        text = self.watermark_text.get()
        watermarked_image = self.image_processor.watermark(text)
        # self.display_image()

        # Store the watermarked image for saving
        self.watermarked_image = watermarked_image

    def save_watermarked_image(self):
        if hasattr(self, 'watermarked_image'):
            messagebox.showinfo("Format", "Image will be saved in '.png' format")
            save_image(self.watermarked_image)
        else:
            messagebox.showerror("Error", "No watermarked image to save.")


if __name__ == "__main__":
    root = Tk()
    app = WatermarkApp(root)
    root.mainloop()
