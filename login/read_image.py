# coding=utf-8

from PIL import Image
import pytesseract
# 打开图片
image = Image.open("F:/Python/study/images/img2.png")
# 识别图中英文文字
text = pytesseract.image_to_string(image)
print(text)