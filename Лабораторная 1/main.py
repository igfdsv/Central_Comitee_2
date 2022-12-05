import doctest
import math


class Elevator:
    def __init__(self, floors: int, max_weight: float, speed: float):
        """
        Создание и подготовка объекта "лифт"

        :param floors: Число этажей
        :param max_weight: Грузоподъёмность, кг
        :param speed: Скорость, этажей в секунду

        :raise TypeError: Если число этажей не целое,
                          либо грузоподъёмность или скорость не являются числами
        :raise ValueError: Если число этажей меньше двух,
                          либо грузпоодъёмность или скорость не положительные

        Пример:
        >>> burj_khalifa_elevator = Elevator(163, 1000, 2)  # лифт Бурдж-Халифы

        >>> basic_lift = Elevator(9, 600, 0.333)  # лифт девятиэтажки
        """
        if not isinstance(floors, int):
            raise TypeError("Число этажей должно быть целым")
        if floors < 2:
            raise ValueError("Число этажей должно быть больше 1")
        self.floors = floors
        self.current_floor = 1

        if not isinstance(max_weight, (int, float)):
            raise TypeError("Грузоподъёмность должна быть числом")
        if max_weight <= 0:
            raise ValueError("Грузоподъёмность должна быть положительной")
        self.max_weight = max_weight
        self.weight = 0  # Вес груза/пассажиров

        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость лифта должна быть числом")
        if speed <= 0:
            raise ValueError("Скорость лифта должна быть положительной")
        self.speed = speed

    def load_cargo(self, floor: int, cargo_weight: float) -> bool:
        """
        Функция погрузки в лифт

        :param floor: Этаж с которого происходит погрузка
        :param cargo_weight: Вес загружаемого груза
        :return: False, если перевес, иначе - True

        :raise Exception: Если лифт находится на другом этаже

        >>> basic_lift = Elevator(9, 600, 0.333)
        >>> basic_lift.load_cargo(1, 1000)  # Пытаемся загрузить слона
        False

        >>> basic_lift = Elevator(9, 600, 0.333)
        >>> basic_lift.load_cargo(1, 100)  # Пытаемся загрузить человека
        True
        """
        if floor != self.current_floor:
            raise Exception("Лифт на другом этаже")

        self.weight += cargo_weight
        return self.weight < self.max_weight

    def move_to_floor(self, floor_number: int) -> float:
        """
        Функция отправки лифта на этаж

        :param floor_number: Номер этажа на который отправляется лифт
        :return: Время поездки (секунд)

        :raise TypeError: Если номер этажа не целое число
        :raise ValueError: Если номер этажа меньше 1 или больше максимального для данного лифта

        :raise Exception: Если лифт перегружен

        Примеры:
        >>> cargo_elevator = Elevator(3, 2000, 0.1)
        >>> cargo_elevator.move_to_floor(3)
        20.0

        >>> kitchen_elevator = Elevator(2, 15, 0.5)
        >>> kitchen_elevator.load_cargo(1, 30)  # Загружаем мешок с картошкой
        False
        >>> kitchen_elevator.move_to_floor(2)
        Traceback (most recent call last):
        ...
        Exception: Перегрузка!
        """
        if not isinstance(floor_number, int):
            raise TypeError("Номер этажа должен быть целым числом")
        if floor_number < 1:
            raise ValueError("Номер этажа должен быть положительным")
        if floor_number > self.floors:
            raise ValueError(f"Этот лифт едет только до {self.floors} этажа")

        if self.weight > self.max_weight:
            raise Exception("Перегрузка!")

        time = abs(self.current_floor - floor_number) / self.speed
        self.current_floor = floor_number  # Здесь должно быть присваивание c задержкой time секунд
                                           # число должно изменяться каждые 1/self.speed секунд...
        return time


class Pen:
    def __init__(self, thickness: int, color: str):
        """
        Создание и подготовка кисти для рисования на плоском холсте

        :param thickness: Толщина кисти в условных единицах
        :param color: Цвет кисти

        Примеры:
        >>> green_snake = Pen(20, "dark green")  # Кисть для рисования зелёной змейки

        >>> sunset_horizon = Pen(3, "orange")  # Кисть для рисования горизонта на закате
        """
        if not isinstance(thickness, int):
            raise TypeError("Толщина кисти должна быть целым числом")
        if thickness < 1:
            raise ValueError("Толщина кисти должна быть положительной")
        self.thickness = thickness

        self.color = color

    def draw_straight_line(self,
                          begin: tuple[float, float],
                          end: tuple[float, float]) -> None:
        """
        Функция позволяет нарисовать прямую данной кистью

        :param begin: Координаты (x, y) начала прямой
        :param end:  Координаты конца прямой

        Примеры:
        >>> sea_horizon = Pen(3, "light blue")
        >>> sea_horizon.draw_straight_line((0, -50), (0, 50))  # Рисует морской горизонт

        >>> neon_light = Pen(7, "neon blue")
        >>> neon_light.draw_straight_line((0, 0), (0, 100))
        >>> neon_light.draw_straight_line((0, 100), (20, 100))
        >>> neon_light.draw_straight_line((20, 100), (20, 0))  # Рисует силуэт небоскрёба в Токио
        """
        pass  # без реализации

    def draw_arc(self,
                 center: tuple[float, float],
                 radius: float,
                 start_angle: float,
                 end_angle: float) -> None:
        """
        Функция для рисования дуги окружности

        :param center: Координаты центра окружности на которой лежит дуга
        :param radius: Радиус окружности на которой лежит дуга
        :param start_angle: Угол начала дуги
        :param end_angle: Угол конца дуги

        :raise ValueError: Если радиус отрицательный выбрасывает ошибку
        :raise ValueError: Если любой из углов не входит в промежуток от -pi до pi

        Примеры:
        >>> thick_red = Pen(5, "red")
        >>> thick_red.draw_arc((0, 0), 1, -math.pi, math.pi)  # Рисует единичную окружность

        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")

        if start_angle > math.pi or start_angle < - math.pi or \
           end_angle > math.pi or end_angle < - math.pi:
            raise ValueError("Углы должны быть в пределах от -pi до pi")

        pass  # без реализации


class WaterMixer:
    def __init__(self,
                 hot_water_temperature: float,
                 hot_water_speed: float,
                 cold_water_temperature: float,
                 cold_water_speed: float):
        """
        Создание объекта типа смеситель

        :param hot_water_temperature: Температура горячей воды
        :param hot_water_speed: Скорость истечения горячей воды
        :param cold_water_temperature: Температура холодной воды
        :param cold_water_speed: Скорость истечения холодной воды

        Примеры:
        >>> mixer = WaterMixer(60, 1, 20, 1)
        """
        self.check_water_speed(hot_water_speed, "горячей")
        self.hot_water_speed = hot_water_speed
        self.check_water_speed(cold_water_speed, "холодной")
        self.cold_water_speed = cold_water_speed

        self.check_water_temperature(hot_water_temperature, "горячей")
        self.check_water_temperature(cold_water_temperature, "холодной")
        if hot_water_temperature < cold_water_temperature:
            raise ValueError("Температура горячей воды должна быть больше температуры холодной")
        self.cold_water_temperature = cold_water_temperature
        self.hot_water_temperature = hot_water_temperature

        self.hot_water_controller = 0
        self.cold_water_controller = 0

    def check_water_temperature(self, water_temperature, name: str) -> None:
        """
        Функция для валидации температуры воды

        :param water_temperature: Пользовательское значение температуры воды
        :param name: Название, горячая или холодная вода

        :raise TypeError: Если пользовательское значение не является числом выбрасывает ошибку
        :raise ValueError: Если температура воды меньше 0 или больше 100 градусов выбрасывает ошибку
        """
        if not isinstance(water_temperature, (int, float)):
            raise TypeError(f"Скорость {name} воды должна быть числом")
        if water_temperature < 0 or water_temperature > 100:
            raise ValueError("Жидкая вода должна иметь температуру от 0 до 100 градусов")

    def check_water_speed(self, water_speed, name: str) -> None:
        """
        Функция для валидации скорости истечения воды

        :param water_speed: Пользовательское значение скорости истечения воды
        :param name: Название, горячая или холодная вода

        :raise TypeError: Если пользовательское значение не является числом выбрасывает ошибку
        :raise ValueError: Если скорость истечения воды отрицательная выбрасывает ошибку
        """
        if not isinstance(water_speed, (int, float)):
            raise TypeError(f"Скорость {name} воды должна быть числом")
        if water_speed <= 0:
            raise ValueError(f"Скорость {name} воды должна быть положительной")

    def set_controller(self,
                       hot_water: float,
                       cold_water: float) -> None:
        """
        Функция для установки кранов смесителя

        :param hot_water: "открытость" крана горячей воды (0-100%)
        :param cold_water: "открытость" крана холодной воды (0-100%)

        :raise ValueError: Выбрасывает ошибку при попытке открыть кран больше чем на 100%

        Примеры:
        >>> mixer = WaterMixer(60, 1, 20, 1)
        >>> mixer.set_controller(50, 50)
        """
        if hot_water < 0 or hot_water > 100:
            raise ValueError("Нельзя открыть кран больше чем на 100% или меньше чем на 0%")
        if cold_water < 0 or cold_water > 100:
            raise ValueError("Нельзя открыть кран больше чем на 100% или меньше чем на 0%")
        self.cold_water_controller = cold_water / 100
        self.hot_water_controller = hot_water / 100

    def get_water_speed(self) -> float:
        """
        Функция для получения скорости истечения воды из смесителя

        :return: скорость истечения воды

        Примеры:
        >>> mixer = WaterMixer(60, 1, 20, 1)
        >>> mixer.set_controller(100, 100)
        >>> mixer.get_water_speed()
        2.0
        """
        return self.hot_water_speed * self.hot_water_controller + self.cold_water_speed * self.cold_water_controller

    def is_open(self) -> bool:
        """
        Функция для проверки состояния смесителя

        :return: состояние смесителя true - открыт, false - закрыт

        Примеры:
        >>> mixer = WaterMixer(60, 1, 20, 1)
        >>> mixer.set_controller(50, 50)
        >>> mixer.is_open()
        True
        """
        return bool(self.cold_water_controller or self.hot_water_controller)

    def get_water_temperature(self) -> float:
        """
        Функция для получения температуры вытекающей воды

        :return: температура истекающей воды

        :raise Exception: Выбрасывает ошибку если смеситель закрыт

        Примеры:
        >>> mixer = WaterMixer(60, 1, 20, 1)
        >>> mixer.set_controller(50, 50)
        >>> mixer.get_water_temperature()
        40.0

        >>> mixer = WaterMixer(20, 2, 0, 1)
        >>> mixer.set_controller(50, 50)
        >>> mixer.get_water_temperature()
        13.333333333333334
        """
        if not self.is_open():
            raise Exception("Смеситель закрыт")

        return (self.hot_water_controller * self.hot_water_temperature * self.hot_water_speed +
                self.cold_water_controller * self.cold_water_temperature * self.cold_water_speed) / \
               (self.cold_water_controller * self.cold_water_speed + self.hot_water_controller * self.hot_water_speed)


if __name__ == "__main__":
    doctest.testmod()
