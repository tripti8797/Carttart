from django.db import models
from PIL import Image
import os

class ClientLogo(models.Model):
    SECTOR_CHOICES = [
        ('healthcare', 'Healthcare'),
        ('fintech', 'Fintech'),
        ('realestate', 'Real Estate'),
        ('ecommerce', 'E-commerce'),
        ('esports', 'Esports'),
        ('tourism', 'Tourism'),
        ('energy', 'Energy'),
    ]

    # name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    sector = models.CharField(max_length=50, choices=SECTOR_CHOICES, default='other')

    def __str__(self):
        return self.sector

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.logo:
            image_path = self.logo.path
            img = Image.open(image_path).convert('RGBA')  # Open the image and ensure RGBA for transparency

            # Convert to grayscale (L mode), then back to RGBA while keeping transparency
            grayscale_img = img.convert('L')  # Convert to grayscale mode 'L' for shades of gray
            grayscale_img = grayscale_img.convert('RGBA')  # Convert back to RGBA to retain alpha channel

            # Ensure no black color by setting a minimum gray value for transparency
            pixel_data = grayscale_img.load()
            width, height = grayscale_img.size
            for y in range(height):
                for x in range(width):
                    r, g, b, a = pixel_data[x, y]
                    # If it's too dark (close to black), make it white
                    if r == 0 and g == 0 and b == 0:
                        pixel_data[x, y] = (255, 255, 255, a)  # Set black pixels to white
                    elif r == 0 or g == 0 or b == 0:  # If any color is 0, adjust to light gray
                        pixel_data[x, y] = (200, 200, 200, a)  # Change dark values to light gray
                    else:
                        pixel_data[x, y] = (r, g, b, a)  # Keep other colors as is

            # Save the final image with transparent background and no black color
            grayscale_img.save(image_path, format='PNG')