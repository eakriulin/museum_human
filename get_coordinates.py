import cv2

image = cv2.imread('/Users/eakriulin/Downloads/museum_human_v2/train/images/museum_heads_train_mp4-0000_jpg.rf.03ec3e6efe6bb92191db6455a330ca27.jpg')
coordinates = []

# Define the function to capture mouse events
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.append((x, y))
        print(f"Coordinate captured: ({x}, {y})")
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)  # Draw a small circle at the clicked point
        cv2.imshow("Image", image)

# Display the image and set up the mouse callback
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", get_coordinates)

# Keep the window open
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print all coordinates after window is closed
print("All captured coordinates:", coordinates)