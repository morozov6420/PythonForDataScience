from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# https://www.youtube.com/watch?v=SEukWq_e3Hs&feature=youtu.be

im1 = Image.open('day3_24.06/lecture/1.png').convert("L")
pix = np.array(im1)

# Функция для изменения изображения


def transform(pix, mat):
    tmp = []
    for x in range(pix.shape[0]):
        for y in range(pix.shape[1]):
            tmp.append(np.array(mat @ [x, y, 0]).astype('int'))

    tmp = np.delete(tmp, 2, 1)
    x_min = tmp[:, 0].min()
    x_max = tmp[:, 0].max()
    y_min = tmp[:, 1].min()
    y_max = tmp[:, 1].max()

    new_tmp = np.vstack((tmp[:, 0] - x_min, tmp[:, 1] - y_min)).T
    new_pix = np.zeros(shape=(abs(x_min) + abs(x_max) +
                              1, abs(y_min) + abs(y_max) + 1))
    i = 0
    for x in range(pix.shape[0]):
        for y in range(pix.shape[1]):
            new_pix[new_tmp[i, 0], new_tmp[i, 1]] = pix[x, y]
            i += 1
    return new_pix


# Матрица поворота
# fi = np.radian(30)
# mat = np.array([
#     [np.cos(fi),  np.sin(fi), 0],
#     [-np.sin(fi), np.cos(fi), 0],
#     [0,           0         , 1]
# ])

# Матрица переноса
# x_ = x + l
# y_ = y + m
# mat = np.array([
#     [1, 0, 0],
#     [0, 1, 0],
#     [l, m, 1]
# ])

# Масштабирования
# x_ = x * a
# y_ = y * b
# mat = np.array([
#     [a, 0, 0],
#     [0, b, 0],
#     [0, 0, 1]
# ])

# Отражение
# x_ = x
# y_ = y * -1
# mat = np.array([
#     [-1,  0, 0],
#     [0, -1, 0],
#     [0,  0, 1]
# ])

# Повернём изображение

fi = np.radians(10)
mat = np.array([
    [np.cos(fi), -np.sin(fi), 0],
    [np.sin(fi), np.cos(fi),  0],
    [0,          0,           1]
])

plt.imshow(transform(pix=pix, mat=mat))
plt.show()


# fi = np.radians(10)
# mat = np.array([
#     [np.cos(fi), -np.sin(fi), 0],
#     [np.sin(fi), np.cos(fi),  0],
#     [0,          0,           1]
# ])
# tmp = []
# for x in range(pix.shape[0]):
#     for y in range(pix.shape[1]):
#         tmp.append(np.array(mat @ [x, y, 0]).astype('int'))

# tmp = np.delete(tmp, 2, 1)
# x_min = tmp[:, 0].min()
# x_max = tmp[:, 0].max()
# y_min = tmp[:, 1].min()
# y_max = tmp[:, 1].max()
# print(x_min, x_max, y_min, y_max)

# new_tmp = np.vstack((tmp[:, 0] - x_min, tmp[:, 1] - y_min)).T
# new_pix = np.zeros(shape=(abs(x_min) + abs(x_max) +
#                           1, abs(y_min) + abs(y_max) + 1))
# i = 0
# for x in range(pix.shape[0]):
#     for y in range(pix.shape[1]):
#         new_pix[new_tmp[i, 0], new_tmp[i, 1]] = pix[x, y]
#         i += 1


# plt.imshow(new_pix)
# plt.show()
