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

import sys
import pyqrcode
from pyqrcode import QRCode


def print_usage():
    print("Usage: python create_qr_code.py <url>")


def generate_qrcode(url: str):
    qrc = pyqrcode.create(url)
    qrc.svg("qrcode.svg", scale=8)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        exit(0)

    generate_qrcode(sys.argv[1])
