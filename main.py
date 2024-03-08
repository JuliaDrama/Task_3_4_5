import cv2
import numpy as np





def show_image(image):
    """
    Отображает изображение в окне с заголовком "Изображение".

    Parameters
    ----------
    image : numpy.ndarray
        Изображение для отображения. Должен быть массивом NumPy, представляющим изображение.

    Returns
    -------
    None

    Notes
    -----
    Эта функция отображает изображение в окне с заголовком "Изображение". Функция будет ожидать 
    неопределенно долго на случай нажатия клавиши, и закроет окно, когда будет нажата любая клавиша.
    """

    cv2.imshow('Изображение', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Функция для вывода информации об изображении
def print_image_info(image):
    """
    Отображает информацию об изображении, включая его разрешение и количество каналов.

    Parameters
    ----------
    image : numpy.ndarray
        Изображение, информацию о котором необходимо отобразить.

    Returns
    -------
    None
    """
    show_image(image)
    print("Разрешение изображения:", image.shape[:2])
    print("Количество каналов:", image.shape[2])

    # Функция для изменения разрешения изображения


def resize_image(image, new_width, new_height):
    """
    Изменяет размер изображения до указанной ширины и высоты.

    Parameters
    ----------
    image : numpy.ndarray
        Изображение для изменения размера.
    new_width : int
        Новая ширина изображения.
    new_height : int
        Новая высота изображения.

    Returns
    -------
    numpy.ndarray
        Изображение с новыми размерами.
    """
    return cv2.resize(image, (new_width, new_height))


# Функция для поворота изображения
def rotate_image(image, angle):
    """
    Поворачивает изображение на указанный угол.

    Parameters
    ----------
    image : numpy.ndarray
        Изображение для поворота.
    angle : float
        Угол поворота в градусах.

    Returns
    -------
    numpy.ndarray
        Повернутое изображение.
    """
    # Получение центра изображения
    center = (image.shape[1] // 2, image.shape[0] // 2)

    # Поворот изображения
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(
        image, rotation_matrix, (image.shape[1], image.shape[0]))

    return rotated_image

# Функция для отражения изображения по горизонтали
def flip_image_horizontal(image):
    """
    Отражает изображение по горизонтали.

    Parameters
    ----------
    image : numpy.ndarray
        Изображение для отражения.

    Returns
    -------
    numpy.ndarray
        Отраженное изображение по горизонтали.
    """
    return cv2.flip(image, 0)

# Функция для отражения изображения по вертикали
def flip_image_vertical(image):
    """
    Отражает изображение по вертикали.

    Parameters
    ----------
    image : numpy.ndarray
        Изображение для отражения.

    Returns
    -------
    numpy.ndarray
        Отраженное изображение по вертикали.
    """
    return cv2.flip(image, 1)

# Функция для изменения цвета группы пикселей произвольной формы и цвета
def change_pixel_color(image, x, y, height, width, color):
    """
    Изменяет цвет группы пикселей изображения.

    Parameters
    ----------
    image : numpy.ndarray
        Изображение, на котором будут изменены цвета.
    x : int
        Координата x верхнего левого угла области, для которой изменяется цвет.
    y : int
        Координата y верхнего левого угла области, для которой изменяется цвет.
    height : int
        Высота области, для которой изменяется цвет.
    width : int
        Ширина области, для которой изменяется цвет.
    color : tuple
        Цвет в формате BGR (Blue, Green, Red), представленный в виде кортежа.

    Returns
    -------
    None
    """
    # Проверить, что координаты находятся в пределах изображения
    if x < 0 or x >= image.shape[1] or y < 0 or y >= image.shape[0]:
        return None
    

    # Изменить цвет пикселя
    image[y:y+height, x:x+width] = color

# Функция для отрисовки прямоугольника вокруг группы пикселей произвольной формы, цвета и толщины
def draw_rectangle(image, x, y, height, width, color, thickness):
    """
    Рисует прямоугольник на изображении.

    Parameters
    ----------
    image : numpy.ndarray
        Изображение, на котором будет нарисован прямоугольник.
    x : int
        Координата x верхнего левого угла прямоугольника.
    y : int
        Координата y верхнего левого угла прямоугольника.
    height : int
        Высота прямоугольника.
    width : int
        Ширина прямоугольника.
    color : tuple
        Цвет прямоугольника в формате BGR (Blue, Green, Red), представленный в виде кортежа.
    thickness : int
        Толщина линии прямоугольника.

    Returns
    -------
    None
    """
    # Проверить, что координаты находятся в пределах изображения
    if x < 0 or x >= image.shape[1] or y < 0 or y >= image.shape[0]:
        return

    # Отрисовка прямоугольника
    cv2.rectangle(image, (x, y), (x+width, y+height), color, thickness)


# Функция для добавления текста на изображение
def print_text(image, text, x, y, font=cv2.FONT_HERSHEY_SIMPLEX, text_size=0.5, text_color=(0, 0, 0)):
    """
    Добавляет текст на изображение.

    Parameters
    ----------
    image : numpy.ndarray
        Изображение, на котором будет добавлен текст.
    text : str
        Текст, который нужно добавить.
    x : int
        Координата x верхнего левого угла области, в которой будет нарисован текст.
    y : int
        Координата y верхнего левого угла области, в которой будет нарисован текст.
    font : int, optional
        Шрифт для текста (по умолчанию cv2.FONT_HERSHEY_SIMPLEX).
    text_size : float, optional
        Размер текста (по умолчанию 0.5).
    text_color : tuple, optional
        Цвет текста в формате BGR (Blue, Green, Red), представленный в виде кортежа (по умолчанию (0, 0, 0)).

    Returns
    -------
    None
    """
    # Проверить, что координаты находятся в пределах изображения
    if x < 0 or x >= image.shape[1] or y < 0 or y >= image.shape[0]:
        return

    # Отрисовка текста
    cv2.putText(image, text, (y, x), font, text_size, text_color, 1)


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

    # Получение значения центрального пикселя
    center_pixel = cropped_image[50, 50]
    print(center_pixel)

    # Изменение значения центрального пикселя
    cropped_image[50, 50] = [0, 0, 255]

    # Отображение измененного изображения
    show_image(cropped_image)

    # Координаты левого верхнего угла группы пикселей
    x = 20
    y = 30

    # Размер
    height = 10
    width = 15

    # Цвет, на который будем менять пиксели
    color = (0, 255, 0)  # Зеленый
    # Изменение цвета
    change_pixel_color(cropped_image, x, y, height, width, color)

    # Отобразить измененное изображение
    show_image(cropped_image)

    # Отрисовать прямоугольник вокруг измененной области

    thickness = 2  # Толщина линии прямоугольника

    # Цвет, которым будем нарисован прямоугольник
    color = (255, 0, 0)  # Синий
    
    #Отрисовка прямоугольника
    draw_rectangle(cropped_image, x, y, height, width, color, thickness)
    #Вывод изображения
    show_image(cropped_image)

    # Отрисовать текст над прямоугольником
    height_text = 15 # Расстояние над прямоугольником
    # Цвет текста
    color = (255, 255, 255) # Белый
    # Отрисовка текста
    print_text(cropped_image, "rec", x, y - height_text, text_color = color)
    #Вывод изображения
    show_image(cropped_image)