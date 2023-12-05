from PIL import Image, ImageDraw, ImageFont


class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.original_image = Image.open(image_path)

    def watermark(self, text):
        watermarked_image = self.original_image.copy()
        draw = ImageDraw.Draw(watermarked_image)

        # customize the font size
        font_size = 20

        # importing default font type from system
        font = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", size=font_size)

        # specify watermark location
        x = watermarked_image.width / 2 - watermarked_image.width / 4
        y = watermarked_image.height / 2

        draw.text((x, y), text, font=font, fill=(255, 0, 0, 128))

        return watermarked_image
