#  MIT License
#
#  Copyright (c) 2022 Misagh Asgari
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

# This program collects images sorted in directories into xlsx and csv files.
# The directory structure should be as follows:
#     Root:
#        - Class 1
#            - image 1
#            - image 2
#            - ...
#            - image n
#        - Class 2
#        - ...
#        - Class n
#
#  Dependencies: PIL, numpy, xlsxwriter, pandas, openpyxl

import os
import sys
from PIL import Image
from numpy import array
import xlsxwriter
import pandas as pd

# Change this to determine final image size. Take into account the limitations of xlsx files in number of cols, rows.
# TODO: Expose this to argv
IMAGE_SIZE = (64, 64)


def main(path):
    images = []

    for data_class in os.listdir(path):
        for image in os.listdir(path + "\\" + data_class):
            # Loads image, resizes it to IMAGE_SIZE, coverts it to grayscale, flattens the array
            img = array(Image.open(path + "\\" + data_class + "\\" + image).resize(IMAGE_SIZE).convert('L')).flatten()
            images.append((data_class, img))

    xlsx_workbook = xlsxwriter.Workbook("file.xlsx")
    xlsx_worksheet = xlsx_workbook.add_worksheet("main")

    row, col = 0, 0
    for x in range(len(images)):
        xlsx_worksheet.write(row, col, images[x][0])
        col += 1

        for pixel in images[x][1]:
            xlsx_worksheet.write(row, col, pixel)
            col += 1

        row += 1
        col = 0

    xlsx_workbook.close()

    in_file = pd.read_excel("file.xlsx")
    in_file.to_csv("file.csv",
                   index=False,
                   header=True)


main(sys.argv[1])
