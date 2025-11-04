"""
Watermarking Desktop GUI Application

Author: Hemant Vijay
Last Updated: 4-Nov-2025
Course: 100 Days of Code - The Complete Python Pro Bootcamp by Angela Yu
Course URL: https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

This project is part of an assignment for Angela Yu's course on Udemy.

Description:
This is a desktop application that allows users to upload images and add watermarks to them.
The application uses Python's tkinter library for the graphical user interface (GUI).
Users can select an image file, choose a watermark position, customize the watermark text,
and save the watermarked image to their computer.
"""

# Import the tkinter library - this is Python's standard GUI (Graphical User Interface) package
# It helps us create windows, buttons, and other visual elements
import tkinter as tk
from tkinter import filedialog, messagebox, font

# Import PIL (Python Imaging Library) - this library helps us work with images
# We use it to open, modify, and save image files
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Import os - this helps us work with file paths and operating system operations
import os


class WatermarkApp:
    """
    This is the main class for our Watermark Application.
    A class is like a blueprint that contains all the code and data for our application.

    When we create an instance of this class, it sets up the entire application window
    with all the buttons, text fields, and functionality needed to watermark images.
    """

    def __init__(self, root):
        """
        This is the initialization method - it runs automatically when we create the application.
        It sets up the main window and all the visual elements (buttons, labels, etc.)

        Parameters:
        root: This is the main window that tkinter creates for us
        """
        # Store the main window so we can use it throughout the class
        self.root = root

        # Set the title that appears at the top of the window
        self.root.title("Image Watermarking Tool")

        # Set the size of the window (width x height in pixels)
        self.root.geometry("800x700")

        # Set the background color of the window
        self.root.config(bg="#f0f0f0")

        # These variables will store our image data
        # We initialize them as None (empty) until the user uploads an image
        self.original_image = None  # The original uploaded image
        self.watermarked_image = None  # The image after we add the watermark
        self.image_path = None  # The file path where the original image is stored

        # Create all the visual elements (buttons, labels, etc.)
        self.create_widgets()

    def create_widgets(self):
        """
        This method creates all the visual elements (widgets) for our application.
        Widgets include buttons, labels, text entry fields, etc.
        """

        # Create a title label at the top of the window
        # A label is just text that displays information to the user
        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        title_label = tk.Label(
            self.root,
            text="Image Watermark Application",
            font=title_font,
            bg="#f0f0f0",
            fg="#333333"
        )
        # Place the title at the top with some padding
        title_label.pack(pady=20)

        # Create a frame (container) for the upload button
        # Frames help us organize widgets in groups
        upload_frame = tk.Frame(self.root, bg="#f0f0f0")
        upload_frame.pack(pady=10)

        # Create the "Upload Image" button
        # When clicked, it will call the upload_image method
        self.upload_btn = tk.Button(
            upload_frame,
            text="Upload Image",
            command=self.upload_image,
            bg="#4CAF50",
            fg="white",
            font=("Helvetica", 12),
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.upload_btn.pack()

        # Create a label to display the name of the uploaded file
        self.file_label = tk.Label(
            self.root,
            text="No image selected",
            bg="#f0f0f0",
            fg="#666666",
            font=("Helvetica", 10)
        )
        self.file_label.pack(pady=5)

        # Create a frame to display the image preview
        self.image_frame = tk.Frame(self.root, bg="#ffffff", width=500, height=300)
        self.image_frame.pack(pady=20)
        self.image_frame.pack_propagate(False)  # Keep the frame size fixed

        # Create a label inside the frame to show the actual image
        self.image_label = tk.Label(self.image_frame, bg="#ffffff")
        self.image_label.pack(expand=True)

        # Create a frame for watermark options
        options_frame = tk.Frame(self.root, bg="#f0f0f0")
        options_frame.pack(pady=10)

        # Create a label asking for watermark text
        tk.Label(
            options_frame,
            text="Watermark Text:",
            bg="#f0f0f0",
            font=("Helvetica", 11)
        ).grid(row=0, column=0, padx=10, sticky="w")

        # Create a text entry field where users can type their watermark text
        self.watermark_entry = tk.Entry(
            options_frame,
            font=("Helvetica", 11),
            width=30
        )
        self.watermark_entry.grid(row=0, column=1, padx=10)
        # Set default watermark text
        self.watermark_entry.insert(0, "© Hemant Vijay")

        # Create a label asking for watermark position
        tk.Label(
            options_frame,
            text="Position:",
            bg="#f0f0f0",
            font=("Helvetica", 11)
        ).grid(row=1, column=0, padx=10, sticky="w", pady=10)

        # Create a dropdown menu for selecting watermark position
        self.position_var = tk.StringVar(value="Bottom Right")
        position_options = ["Top Left", "Top Right", "Bottom Left", "Bottom Right", "Center"]
        position_menu = tk.OptionMenu(
            options_frame,
            self.position_var,
            *position_options
        )
        position_menu.config(font=("Helvetica", 11), bg="#ffffff")
        position_menu.grid(row=1, column=1, padx=10, sticky="w")

        # Create a frame for action buttons (Add Watermark and Save)
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        # Create "Add Watermark" button
        self.watermark_btn = tk.Button(
            button_frame,
            text="Add Watermark",
            command=self.add_watermark,
            bg="#2196F3",
            fg="white",
            font=("Helvetica", 12),
            padx=20,
            pady=10,
            cursor="hand2",
            state="disabled"  # Disabled until an image is uploaded
        )
        self.watermark_btn.grid(row=0, column=0, padx=10)

        # Create "Save Image" button
        self.save_btn = tk.Button(
            button_frame,
            text="Save Watermarked Image",
            command=self.save_image,
            bg="#FF9800",
            fg="white",
            font=("Helvetica", 12),
            padx=20,
            pady=10,
            cursor="hand2",
            state="disabled"  # Disabled until watermark is added
        )
        self.save_btn.grid(row=0, column=1, padx=10)

    def upload_image(self):
        """
        This method is called when the user clicks the "Upload Image" button.
        It opens a file dialog box where users can select an image file from their computer.
        """

        # Open a file selection dialog
        # This shows a window where users can browse their computer for image files
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif"),
                ("All Files", "*.*")
            ]
        )

        # Check if the user actually selected a file (they might have clicked Cancel)
        if file_path:
            try:
                # Store the path to the image file
                self.image_path = file_path

                # Open the image using PIL (Python Imaging Library)
                self.original_image = Image.open(file_path)

                # Display the image in the preview area
                self.display_image(self.original_image)

                # Update the file label to show the name of the selected file
                filename = os.path.basename(file_path)
                self.file_label.config(text=f"Selected: {filename}")

                # Enable the "Add Watermark" button now that we have an image
                self.watermark_btn.config(state="normal")

                # Disable the save button until watermark is added
                self.save_btn.config(state="disabled")

                # Clear any previously watermarked image
                self.watermarked_image = None

            except Exception as e:
                # If something goes wrong (file corrupted, wrong format, etc.)
                # Show an error message to the user
                messagebox.showerror(
                    "Error",
                    f"Failed to open image: {str(e)}"
                )

    def display_image(self, image):
        """
        This method displays an image in the preview area.
        It resizes the image to fit nicely in the window while maintaining its proportions.

        Parameters:
        image: The PIL Image object to display
        """

        # Get the size of our preview frame
        frame_width = 500
        frame_height = 300

        # Create a copy of the image so we don't modify the original
        display_img = image.copy()

        # Calculate how much we need to resize the image to fit in the frame
        # while keeping the same width-to-height ratio (aspect ratio)
        img_width, img_height = display_img.size

        # Calculate the scaling ratios for width and height
        width_ratio = frame_width / img_width
        height_ratio = frame_height / img_height

        # Use the smaller ratio to ensure the image fits completely
        scale_ratio = min(width_ratio, height_ratio)

        # Calculate new dimensions
        new_width = int(img_width * scale_ratio)
        new_height = int(img_height * scale_ratio)

        # Resize the image using high-quality resampling
        display_img = display_img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Convert the PIL image to a format tkinter can display
        photo = ImageTk.PhotoImage(display_img)

        # Update the image label with the new image
        self.image_label.config(image=photo)
        # Keep a reference to prevent garbage collection (technical requirement)
        self.image_label.image = photo

    def add_watermark(self):
        """
        This method adds a watermark to the uploaded image.
        It takes the text from the entry field and places it on the image
        at the position selected by the user.
        """

        # Check if we have an image to watermark
        if not self.original_image:
            messagebox.showwarning(
                "Warning",
                "Please upload an image first."
            )
            return

        # Get the watermark text from the entry field
        watermark_text = self.watermark_entry.get()

        # Check if the user entered any text
        if not watermark_text:
            messagebox.showwarning(
                "Warning",
                "Please enter watermark text."
            )
            return

        try:
            # Create a copy of the original image to add the watermark to
            # This preserves the original image
            self.watermarked_image = self.original_image.copy()

            # Create a drawing object that lets us draw on the image
            draw = ImageDraw.Draw(self.watermarked_image)

            # Get the image dimensions (width and height)
            img_width, img_height = self.watermarked_image.size

            # Calculate an appropriate font size based on the image size
            # Larger images get larger text
            font_size = int(img_height * 0.05)  # 5% of image height

            # Try to use a nice font, fall back to default if not available
            try:
                # Arial is a common font that should work on most systems
                watermark_font = ImageFont.truetype("arial.ttf", font_size)
            except:
                # If Arial is not found, use the default font
                watermark_font = ImageFont.load_default()

            # Calculate the size of the watermark text
            # This helps us position it correctly
            bbox = draw.textbbox((0, 0), watermark_text, font=watermark_font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # Add some padding around the text
            padding = 20

            # Calculate the position based on user selection
            position = self.position_var.get()

            if position == "Top Left":
                x = padding
                y = padding
            elif position == "Top Right":
                x = img_width - text_width - padding
                y = padding
            elif position == "Bottom Left":
                x = padding
                y = img_height - text_height - padding
            elif position == "Bottom Right":
                x = img_width - text_width - padding
                y = img_height - text_height - padding
            else:  # Center
                x = (img_width - text_width) // 2
                y = (img_height - text_height) // 2

            # Draw a semi-transparent background rectangle for better text visibility
            # This makes the text easier to read regardless of the image background
            background_padding = 10
            draw.rectangle(
                [
                    (x - background_padding, y - background_padding),
                    (x + text_width + background_padding, y + text_height + background_padding)
                ],
                fill=(0, 0, 0, 180)  # Semi-transparent black
            )

            # Draw the watermark text on the image
            # White text is visible on most backgrounds
            draw.text((x, y), watermark_text, font=watermark_font, fill=(255, 255, 255, 255))

            # Display the watermarked image in the preview
            self.display_image(self.watermarked_image)

            # Enable the save button now that we have a watermarked image
            self.save_btn.config(state="normal")

            # Show a success message
            messagebox.showinfo(
                "Success",
                "Watermark added successfully! You can now save the image."
            )

        except Exception as e:
            # If something goes wrong, show an error message
            messagebox.showerror(
                "Error",
                f"Failed to add watermark: {str(e)}"
            )

    def save_image(self):
        """
        This method saves the watermarked image to the user's computer.
        It opens a save dialog where users can choose where to save the file
        and what to name it.
        """

        # Check if we have a watermarked image to save
        if not self.watermarked_image:
            messagebox.showwarning(
                "Warning",
                "Please add a watermark first."
            )
            return

        # Get the original filename and suggest a new name
        if self.image_path:
            # Extract the original filename without the extension
            original_filename = os.path.splitext(os.path.basename(self.image_path))[0]
            original_extension = os.path.splitext(self.image_path)[1]
            # Suggest a filename with "_watermarked" added
            default_filename = f"{original_filename}_watermarked{original_extension}"
        else:
            default_filename = "watermarked_image.png"

        # Open a save dialog where the user can choose where to save the file
        save_path = filedialog.asksaveasfilename(
            title="Save Watermarked Image",
            defaultextension=".png",
            initialfile=default_filename,
            filetypes=[
                ("PNG Files", "*.png"),
                ("JPEG Files", "*.jpg *.jpeg"),
                ("All Files", "*.*")
            ]
        )

        # Check if the user selected a location (they might have clicked Cancel)
        if save_path:
            try:
                # Save the watermarked image to the selected location
                self.watermarked_image.save(save_path)

                # Show a success message
                messagebox.showinfo(
                    "Success",
                    f"Image saved successfully to:\n{save_path}"
                )

            except Exception as e:
                # If something goes wrong, show an error message
                messagebox.showerror(
                    "Error",
                    f"Failed to save image: {str(e)}"
                )


def main():
    """
    This is the main function that starts the application.
    It creates the main window and starts the event loop.
    """

    # Create the main window
    root = tk.Tk()

    # Create an instance of our WatermarkApp class
    # This sets up all the buttons, labels, and functionality
    app = WatermarkApp(root)

    # Start the event loop
    # This keeps the window open and responsive to user actions
    # The program will continue running until the user closes the window
    root.mainloop()


# This is a Python convention - it checks if this file is being run directly
# (as opposed to being imported as a module in another file)
if __name__ == "__main__":
    main()
