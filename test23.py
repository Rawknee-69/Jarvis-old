import pygame
import cv2
import numpy as np
import pyautogui

# Initialize video capture
cap = cv2.VideoCapture(0)

# Set a flag for volume control
increase_volume = False
decrease_volume = False

# Initialize pygame
pygame.init()

# Set the window size
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

while True:
    ret, frame = cap.read()

    # Convert the frame to grayscale for better processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to the frame to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use the Canny edge detection to find edges in the frame
    edges = cv2.Canny(gray, 50, 150)

    # Find contours in the frame
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Approximate the contour
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check if the contour has 2 fingers up or down
        if len(approx) == 2:
            # Logic to increase volume
            if increase_volume:
                pyautogui.press('volumeup')
                increase_volume = False
            # Logic to decrease volume
            elif decrease_volume:
                pyautogui.press('volumedown')
                decrease_volume = False

    # Resize the frame to fit the window
    frame = cv2.resize(frame, window_size)

    # Convert to RGB for pygame display
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = np.flipud(frame)

    # Create a Pygame surface
    frame = pygame.surfarray.make_surface(frame)

    # Update the display
    screen.blit(frame, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            cap.release()
            cv2.destroyAllWindows()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                increase_volume = True
            elif event.key == pygame.K_d:
                decrease_volume = True

    pygame.event.pump()
