# 将 /tmp/template.md 复制到 _posts/ 目录下,将里面的内容中[picture]部分内容替换为 （/assets/images/）
# 文件夹下的随机一张的图片（通过遍历文件夹下获取图片文件，然后随机选一个文件名（排除掉文件夹）），并重命名为当前日期+文件名

import os
import time
import random
import shutil
import argparse


# 获取当前时间
def getNowTime():
    return time.strftime("%Y-%m-%d", time.localtime())


# 获取图片文件夹下的所有图片文件
def getImages():
    images = []
    for root, dirs, files in os.walk("./assets/images"):
        for file in files:
            if file != ".DS_Store":
                images.append(file)
    return images


# 随机获取一个图片文件名
def getRandomImage(images):
    return random.choice(images)


# 复制模板文件到_posts目录下
def copyTemplate():
    shutil.copyfile("./tmp/template.md", "./_posts/" + getNowTime() + ".md")


# 替换模板文件中的[picture]为随机获取的图片文件名
def replacePicture():
    images = getImages()
    randomImage = getRandomImage(images)
    with open("./_posts/" + getNowTime() + ".md", "r+", encoding="utf8") as f:
        content = f.read()
        content = content.replace("[picture]", randomImage)
        content = content.replace("title:", "title: " + tileName)

        f.seek(0)
        f.write(content)


tileName = ""


# 重命名文件
def renameFile():
    os.rename(
        "./_posts/" + getNowTime() + ".md",
        "./_posts/" + getNowTime() + "-" + tileName + ".md",
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="文章标题")
    args = parser.parse_args()
    tileName = args.title
    copyTemplate()
    replacePicture()
    renameFile()

    print("文章“ " + tileName + " ”创建成功")
