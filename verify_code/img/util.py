# -*- coding: UTF8 -*-

import random
import string
import io
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class ImageCodeUtil(object):

    font_path = f"{os.path.dirname(__file__)}/Arial.ttf"

    # 生成几位数的验证码
    number = 4

    # 生成验证码图片的高度和宽度
    size = (100, 30)

    # 背景颜色，默认为白色
    bgcolor = (255, 255, 255)

    # 字体颜色，默认为蓝色
    fontcolor = (0, 0, 255)

    # 干扰线颜色。默认为红色
    linecolor = (255, 222, 110)

    # 是否要加入干扰线
    draw_line = True

    # 加入干扰线条数的上下限
    line_number = (1, 5)

    # 用来随机生成一个字符串
    def __gene_text(self):
        source = list(string.ascii_letters)
        for index in range(0, 10):
            source.append(str(index))
        return ''.join(random.sample(source, self.number))  # number是生成验证码的位数

    # 用来绘制干扰线
    def __gene_line(self, draw, width, height):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=self.linecolor)

    # 生成验证码
    def gene_code(self) -> [str, str]:
        # if not dir_path.endswith("/"):
        #     dir_path += "/"
        width, height = self.size  # 宽和高
        image = Image.new('RGBA', (width, height), self.bgcolor)  # 创建图片
        font = ImageFont.truetype(self.font_path, 25)  # 验证码的字体
        draw = ImageDraw.Draw(image)  # 创建画笔
        text = self.__gene_text()  # 生成字符串
        font_width, font_height = font.getsize(text)
        # 填充字符串
        draw.text(((width - font_width) / self.number, (height - font_height) / self.number), text,
                  font=font, fill=self.fontcolor)
        if self.draw_line:
            self.__gene_line(draw, width, height)
        image = image.transform((width+20, height+10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)  # 创建扭曲
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
        # path = f'{dir_path}{uuid4().hex}.png'
        # image.save(path)  # 保存验证码图片
        buf = io.BytesIO()
        image.save(buf, "png")
        return text, buf.getvalue()
