import cv2
import numpy as np





def show_image(image):
    cv2.imshow('Изображение', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Функция для вывода информации об изображении
def print_image_info(image):
    show_image(image)
    print("Разрешение изображения:", image.shape[:2])
    print("Количество каналов:", image.shape[2])

    # Функция для изменения разрешения изображения


def resize_image(image, new_width, new_height):
    return cv2.resize(image, (new_width, new_height))


# Функция для поворота изображения
def rotate_image(image, angle):
    # Получение центра изображения
    center = (image.shape[1] // 2, image.shape[0] // 2)

    # Поворот изображения
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(
        image, rotation_matrix, (image.shape[1], image.shape[0]))

    return rotated_image

# Функция для отражения изображения по горизонтали
def flip_image_horizontal(image):
    return cv2.flip(image, 0)

# Функция для отражения изображения по вертикали
def flip_image_vertical(image):
    return cv2.flip(image, 1)


if __name__ == '__main__':
    # Загрузка изображения
    image = cv2.imread('data/images/pcb.jpg')

    new_width = 700  # Новая ширина
    new_height = 500  # Новая высота

    # Изменение размера изображения
    resized_image = cv2.resize(image, (new_width, new_height))
    # Функция отображения изображения

    # вывод изображения
    show_image(image=resized_image)

    # вывод информации об изображении
    print_image_info(image=resized_image)

    # изменение разрещения
    resized_image1 = cv2.resize(image, (new_width, new_height))

    # вывод изображения
    show_image(resized_image1)

    # Создание копии изображения
    copy_img = resize_image(image=image, new_height=500, new_width=700)

    # Поворот изображения на 45, 90 и 180 градусов
    rotated_image_45 = rotate_image(copy_img, 45)
    rotated_image_90 = rotate_image(copy_img, 90)
    rotated_image_180 = rotate_image(copy_img, 180)

    # Отображение повернутых изображений
    show_image(rotated_image_45)
    show_image(rotated_image_90)
    show_image(rotated_image_180)

    # Отражение изображения по горизонтали и вертикали
    flipped_image_horizontal = flip_image_horizontal(copy_img)
    flipped_image_vertical = flip_image_vertical(copy_img)

    # Отображение отраженных изображений
    show_image(flipped_image_horizontal)
    show_image(flipped_image_vertical)

    # Получение размеров изображения
    height, width = image.shape[:2]

    print("Высота изображения:", height)

    # Вырезание области 100x100 пикселей
    cropped_image = image[1800:1900, 1300:1400]

    # Отображение вырезанной области
    show_image(cropped_image)