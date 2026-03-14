import cv2
import numpy as np
import pytesseract

def clean_cell(cell):
    cell = cv2.cvtColor(cell, cv2.COLOR_BGR2GRAY)
    cell = cv2.adaptiveThreshold(
        cell,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2
    )

    h, w = cell.shape
    margin = int(min(h, w) * 0.15)
    cell = cell[margin:h-margin, margin:w-margin]

    kernel = np.ones((2,2), np.uint8)
    cell = cv2.morphologyEx(cell,cv2.MORPH_OPEN, kernel)

    return cell

def is_empty(cell):
    total_pixels = cell.shape[0] * cell.shape[1]
    white_pixels = cv2.countNonZero(cell)

    return white_pixels < total_pixels * 0.03

def count_holes(cell):

    contours, hierarchy = cv2.findContours(
        cell,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    holes = 0

    if hierarchy is not None:
        for h in hierarchy[0]:
            if h[3] != -1:
                holes += 1

    return holes

def recognize_digit(cell):
    cell = clean_cell(cell)

    if is_empty(cell):
        return 0

    cell = cv2.resize(cell, (128,128))

    config = "--psm 10 -c tessedit_char_whitelist=123456789"
    text = pytesseract.image_to_string(cell, config=config)
    text = text.strip()

    holes = count_holes(cell)
    if text.isdigit():
        digit = int(text)
        if digit == 3 and holes >= 2:
            digit = 8
        if digit == 8 and holes < 2:
            digit = 3
        return digit

    return 0

def read_sudoku(image_path):
    board = [[0 for _ in range(9)] for _ in range(9)]
    img = cv2.imread(image_path)

    if img is None:
        return board

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)

    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2
    )

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    biggest = None
    max_area = 0

    for c in contours:
        area = cv2.contourArea(c)
        if area > max_area:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            if len(approx) == 4:
                biggest = approx
                max_area = area

    if biggest is None:
        return board

    pts = biggest.reshape(4, 2).astype("float32")

    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)

    rect = np.zeros((4, 2), dtype="float32")
    rect[0] = pts[np.argmin(s)] 
    rect[2] = pts[np.argmax(s)] 
    rect[1] = pts[np.argmin(diff)] 
    rect[3] = pts[np.argmax(diff)]  

    size = 450

    dst = np.array([
        [0,0],
        [size,0],
        [size,size],
        [0,size]
    ], dtype = "float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(img, M, (size, size))

    step = size // 9

    for y in range(9):
        for x in range(9):
            cell = warp[
                y * step:(y + 1) * step,
                x * step:(x + 1) * step
            ]

            digit = recognize_digit(cell)

            board[y][x] = digit

    return board