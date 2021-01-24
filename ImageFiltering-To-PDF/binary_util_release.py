import cv2
import os
import numpy as np

title = "一元函数微分学2"
project = "22"

# 创建并打开文件
f = open("F:\\Desktop\\Work\\Code\\script\\pythonProject\\res\\{0}\\{1}.md".format(project,title), "w", encoding='utf-8')
# 图片模板
template_img = "![{0}]({1})\n<br>\n"


f_src = "F:\\Desktop\\Work\\Code\\script\\pythonProject\\src\\{0}\\".format(project)
f_res = "F:\\Desktop\\Work\\Code\\script\\pythonProject\\res\\{0}\\{1}.{2}"


def get_all_file(path):
    count = 1
    dirs = os.listdir(path)
    # 遍历目录下的图片
    for child in dirs:
        ChildPath = os.path.join(path, child)
        print(ChildPath)
        # 读取照片
        img = cv2.imread(ChildPath)
        ResPath = f_res.format(project, count, "png")
        print(ResPath)
        # 二值化并写出
        threshold_Util(ResPath, img);
        # 写入到markdown文件
        f.write(template_img.format(count, "{0}.png".format(count)))
        count = count + 1


# 初始化md文件
def md_init():
    f.write("# {0}\n<br>".format(title))


# 全局阈值
def threshold_Util(target, image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # ret, binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    print("阈值：", ret)
    # cv2.imshow("binary", binary)
    cv2.imwrite(target, binary)
    print("写出完成")


if __name__ == "__main__":
    md_init()
    get_all_file(f_src)
    # 关闭文件
    f.close()
