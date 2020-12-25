import os
from PIL import Image
# 源目录
project_dir = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(project_dir, 'C:/Users/Administrator/Desktop/test')
# 输出目录
output = os.path.join(project_dir, 'C:/Users/Administrator/Desktop/test1')
def modify90():
    # 切换目录
    os.chdir(input)
    i = 0
    # 遍历目录下所有的文件
    for image_name in os.listdir(os.getcwd()):
        print(image_name)
        im = Image.open(os.path.join(input, image_name))
        img = im.transpose(Image.ROTATE_90)   #修改角度
       # img.save(os.path.join(output, str(i)+image_name))
        img.save(os.path.join(output, str(i) + '.jpg'))
        i = i+1
def modify180():
 # 切换目录
 os.chdir(input)
 i = 100
 # 遍历目录下所有的文件
 for image_name in os.listdir(os.getcwd()):
  print(image_name)
  im = Image.open(os.path.join(input, image_name))
  img = im.transpose(Image.ROTATE_180)  # 修改角度
  # img.save(os.path.join(output, str(i)+image_name))
  img.save(os.path.join(output, str(i) + '.jpg'))
  i = i + 1
def modify270():
 # 切换目录
 os.chdir(input)
 i = 200
 # 遍历目录下所有的文件
 for image_name in os.listdir(os.getcwd()):
  print(image_name)
  im = Image.open(os.path.join(input, image_name))
  img = im.transpose(Image.ROTATE_270)  # 修改角度
  # img.save(os.path.join(output, str(i)+image_name))
  img.save(os.path.join(output, str(i) + '.jpg'))
  i = i + 1
if __name__ == '__main__':
    modify90()
    modify180()
    modify270()