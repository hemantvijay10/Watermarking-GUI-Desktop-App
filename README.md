# Image Watermarking Desktop Application

## Project Information

**Author:** Hemant Vijay
**Last Updated:** 4 November 2025
**Course:** 100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu
**Course Link:** https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

This project is an assignment from Angela Yu's Python course on Udemy.

## About This Project

This is a desktop application that allows users to add watermarks to their images. A watermark is text or a logo that you place on an image to mark it as yours or to add copyright information. This is commonly used by photographers, designers, and content creators to protect their work.

## What Does This Application Do

The application provides a simple and easy to use interface where you can:

1. Upload any image file from your computer (supports PNG, JPG, JPEG, BMP, and GIF formats)
2. Type custom watermark text (like your name, copyright notice, or company name)
3. Choose where the watermark should appear on the image (top left, top right, bottom left, bottom right, or center)
4. Preview the watermarked image before saving
5. Save the watermarked image to any location on your computer

## Technical Details

The application is built using Python and the following libraries:

**tkinter:** This is Python's standard library for creating graphical user interfaces. It provides all the buttons, windows, and text fields you see in the application.

**Pillow (PIL):** This is the Python Imaging Library that handles all image processing tasks including opening images, adding text to images, and saving modified images.

## How To Use This Application

### Installation Requirements

Before running the application, you need to have Python installed on your computer and install the required library:

```
pip install Pillow
```

### Running The Application

To start the application, open a terminal or command prompt in the project folder and run:

```
python watermark_app.py
```

### Using The Application

**Step 1: Upload An Image**

Click the "Upload Image" button at the top of the window. A file browser will open where you can select an image from your computer. Once selected, you will see a preview of your image in the center of the window.

**Step 2: Customize Your Watermark**

In the watermark text field, type the text you want to appear on your image. By default, it shows the author's name, but you can change it to anything you want.

Use the position dropdown menu to select where you want the watermark to appear on your image. You can choose from five positions: Top Left, Top Right, Bottom Left, Bottom Right, or Center.

**Step 3: Add The Watermark**

Click the "Add Watermark" button. The application will add your text to the image and show you a preview of the result. The watermark text will appear in white with a semi transparent black background to ensure it is visible on any image.

**Step 4: Save Your Watermarked Image**

If you are happy with how the watermark looks, click the "Save Watermarked Image" button. A file browser will open where you can choose where to save the file and what to name it. The application will suggest a filename with "_watermarked" added to the original filename.

## Features

**User Friendly Interface:** The application has a clean and simple design that is easy to understand and use, even for people without technical knowledge.

**Image Preview:** You can see both the original image and the watermarked version before saving, so you know exactly what the final result will look like.

**Flexible Positioning:** Choose exactly where you want your watermark to appear on the image with five preset positions.

**Custom Text:** Add any text you want as a watermark, whether it's your name, a copyright symbol, or a business name.

**Automatic Text Sizing:** The application automatically calculates the appropriate text size based on your image dimensions, ensuring the watermark looks good on images of any size.

**Readable Watermarks:** The watermark text is displayed in white with a semi transparent black background, making it readable on both light and dark images.

**Multiple File Format Support:** The application works with the most common image formats including PNG, JPEG, JPG, BMP, and GIF.

**Safe Processing:** The application never modifies your original image. It always creates a new copy with the watermark, keeping your original file safe.

## Project Structure

The project contains the following files:

**watermark_app.py:** This is the main Python file that contains all the code for the application. It includes the user interface design, image processing logic, and all the functions that make the application work.

**requirements.txt:** This file lists what the application does in simple terms. It serves as the project specification.

**LICENSE.dat:** This file contains the MIT License, which is a permissive free software license. It allows anyone to use, modify, and distribute this code freely. It also includes the educational project notice crediting Angela Yu's course.

**README.md:** This file (the one you are reading now) provides comprehensive documentation about the project, how to use it, and what it does.

## Understanding The Code

The application is built using object oriented programming, which means the code is organized into a class called WatermarkApp. This class contains all the functionality of the application.

### Main Components

**Initialization (__init__ method):** Sets up the main window and creates all the visual elements like buttons and text fields.

**Widget Creation (create_widgets method):** This creates all the user interface elements including the upload button, watermark text field, position selector, preview area, and action buttons.

**Image Upload (upload_image method):** Handles the process of selecting and loading an image file from the user's computer.

**Image Display (display_image method):** Takes an image and resizes it proportionally to fit nicely in the preview area without distorting it.

**Adding Watermark (add_watermark method):** This is where the main image processing happens. It takes the watermark text and position, calculates where to place it, and draws it on the image with appropriate styling.

**Saving Image (save_image method):** Handles saving the watermarked image to a location chosen by the user.

## Error Handling

The application includes error handling to deal with common issues:

If you try to upload a file that is not a valid image, you will see an error message.

If you try to add a watermark without uploading an image first, you will see a warning message.

If you try to add a watermark without entering any text, you will see a warning message.

If something goes wrong while saving the image, you will see an error message explaining what happened.

## License

This project is licensed under the MIT License, which is one of the most permissive and widely used open source licenses. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of this software.

The only requirement is that you include the original copyright notice and license text in any substantial portions of the software you distribute.

See the LICENSE.dat file for the complete license text.

## Educational Purpose

This project was created as part of a learning exercise in the "100 Days of Code" course by Angela Yu. The purpose of this assignment is to practice:

Creating graphical user interfaces with Python's tkinter library

Working with images using the Pillow (PIL) library

Implementing file dialogs for opening and saving files

Object oriented programming concepts in Python

Error handling and user input validation

Creating user friendly applications with good visual design

## Credits

**Course Instructor:** Angela Yu

**Course Platform:** Udemy

**Course Name:** 100 Days of Code: The Complete Python Pro Bootcamp

**Student/Developer:** Hemant Vijay

Special thanks to Angela Yu for creating an excellent course that teaches practical Python programming through hands on projects like this one.

## Future Enhancement Ideas

While this application is complete and functional for its intended purpose, here are some ideas for how it could be enhanced in the future:

Add support for image watermarks (logos) in addition to text watermarks

Allow users to customize the font style and color of the watermark text

Add the ability to adjust watermark transparency

Include batch processing to watermark multiple images at once

Add the ability to resize or crop images before watermarking

Include preset watermark templates for common use cases

Add undo and redo functionality

Support for dragging the watermark to a custom position with the mouse

## Troubleshooting

**The application window does not open:**

Make sure you have Python installed correctly on your system. Try running "python --version" in your terminal to verify.

**Error about tkinter not being available:**

Tkinter usually comes pre installed with Python, but on some Linux systems you may need to install it separately. On Ubuntu/Debian, run: sudo apt get install python3 tk

**Error about PIL or Pillow:**

Make sure you have installed Pillow using: pip install Pillow

**The watermark looks too small or too large:**

The application automatically sizes the watermark based on the image dimensions. If you need different sizing, you can modify the font_size calculation in the add_watermark method in the code.

**Fonts are not displaying correctly:**

The application tries to use Arial font but falls back to a default font if Arial is not available. This is normal and the watermark will still work correctly.

## Contact and Support

This is an educational project created for learning purposes. If you have questions about the code or encounter issues:

1. Review the extensive comments in the watermark_app.py file, which explain each section of code in detail
2. Refer to the official Python documentation for tkinter and Pillow
3. Check the Angela Yu course materials for additional context and explanations

## Conclusion

This image watermarking application demonstrates practical Python programming skills including GUI development, image processing, and file handling. It provides a useful tool for anyone who needs to add watermarks to their images while showcasing fundamental programming concepts in an accessible way.

Thank you for reviewing this project!
