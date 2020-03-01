import matplotlib.pyplot as plt
from PIL import Image

# 打开指定图片
image = plt.imread('female.jpg')
im = Image.open('female.jpg')
width, height = im.size
print('图片宽为', width, '图片高为', height, '图片格式为', im.format, '图片描述为', im.format_description)
# 指定图片中的红波段
im_r = image[:, :, 0]
# 图片显示红波段
plt.imshow(im_r)
# 窗口中展示图片
plt.show()
# 加载灰度图，可以添加cmap参数解决
plt.imshow(im_r, cmap='Greys_r')
# 窗口中展示灰度图
plt.show()
