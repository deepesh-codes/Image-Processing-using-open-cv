import cv2

# Load the image from file
image = cv2.imread('Pic.webp')

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not load image. Check the file path.")
else:
    # Display the original image
    cv2.imshow('Original Image', image)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray_image)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imshow('Blurred Image', blurred_image)

    # Use the Canny edge detector
    edges = cv2.Canny(gray_image, 100, 200)
    cv2.imshow('Edges', edges)

    # Resize the image to 100x100 pixels
    resized_image = cv2.resize(image, (100, 100))
    cv2.imshow('Resized Image', resized_image)

    # Draw a rectangle (startX, startY, endX, endY)
    cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 3)

    # Draw a circle (centerX, centerY, radius)
    cv2.circle(image, (150, 150), 50, (255, 0, 0), 3)

    # Display the image with shapes
    cv2.imshow('Image with Shapes', image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
