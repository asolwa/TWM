import cv2 as cv
import numpy as np
from erode import main

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def show(name, img):
    # cv.imshow(name, cv.resize(img, (800, 600)))
    cv.namedWindow(name, cv.WINDOW_KEEPRATIO)
    cv.imshow(name, img)
    cv.resizeWindow(name, 1200, 1000)


def calculate_circularity(contour):
    perimeter = cv.arcLength(contour, True)
    area = cv.contourArea(contour)

    if perimeter == 0:  # Avoid division by zero
        return 0

    circularity = (4 * np.pi * area) / (perimeter ** 2)
    return circularity


def transform(mask):
    return mask
    # element = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (1, 1))
    # mask = cv.erode(mask, element)

    # element = cv.getStructuringElement(cv.MORPH_RECT, (11, 11), (1, 1))
    # return cv.dilate(mask, element, iterations=2)


def eccentricity(contour):
    ellipse = cv.fitEllipse(contour)
    (x, y), (major_axis, minor_axis), angle = ellipse

    # Compute eccentricity
    a = max(major_axis, minor_axis) / 2  # Semi-major axis
    b = min(major_axis, minor_axis) / 2  # Semi-minor axis
    return np.sqrt(1 - (b**2 / a**2))


def segments(contour):
    epsilon = 0.02*cv.arcLength(contour,True)
    approx = cv.approxPolyDP(contour,epsilon,True)
    # cv.polylines(img, [approx], isClosed=True, color=(0, 255, 0), thickness=3)
    return approx


def classify(name, mask):
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # cv.drawContours(img, contours, -1, (255, 255, 255), 2)  # White contours

    for i, contour in enumerate(contours):
        if cv.contourArea(contour) <= 100:  # Filter small noise
            continue

        # Get bounding box for contour
        x, y, w, h = cv.boundingRect(contour)

        # Draw contour
        segs = segments(contour)

        if len(segs) > 6:
            shape = "Circle"
            color = RED
        else:
            shape = "Square"
            color = GREEN
        # shape = f'{shape}{len(approx)}'
        cv.putText(img, shape, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
    show(name, img)


# Load image
img = cv.imread("test.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


# Create color detecting masks
yellow_low = (18, 76, 161)
yellow_high = (41, 255, 255)

red_low = (0, 98, 135)
red_high = (8, 255, 255)

green_low = (43, 80, 66)
green_high = (104, 220, 143)

cyan_low = (66, 0, 118)
cyan_high = (148, 65, 195)

pink_low = (161, 0, 166)
pink_high = (360, 195, 255)

blue_low = (97, 78, 38)
blue_high = (134, 255, 255)

yellow_mask = cv.inRange(hsv, yellow_low, yellow_high)
red_mask = cv.inRange(hsv, red_low, red_high)
green_mask = cv.inRange(hsv, green_low, green_high)
cyan_mask = cv.inRange(hsv, cyan_low, cyan_high)
pink_mask = cv.inRange(hsv, pink_low, pink_high)
blue_mask = cv.inRange(hsv, blue_low, blue_high)

yellow_mask = transform(yellow_mask)
red_mask = transform(red_mask)
green_mask = transform(green_mask)
cyan_mask = transform(cyan_mask)
pink_mask = transform(pink_mask)
blue_mask = transform(blue_mask)

# classify('yellow', yellow_mask)
classify('red', red_mask)


cv.waitKey()
