import csv
import sys
import os


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

    @staticmethod
    def from_list(attribute_list):
        if len(attribute_list) != 0:
            if attribute_list[0] == 'car':
                return Car.from_list(attribute_list)
            elif attribute_list[0] == 'truck':
                return Truck.from_list(attribute_list)
            elif attribute_list[0] == 'spec_machine':
                return SpecMachine.from_list(attribute_list)
        return None


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying,
                 passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count

    @classmethod
    def from_list(cls, attribute_list):
        if len(attribute_list) >= 6:
            passenger_seats_count = attribute_list[2]
            carrying = attribute_list[5]
            if not passenger_seats_count.isdigit() or not carrying.replace('.', '', 1).isdigit():
                return None

            passenger_seats_count = int(passenger_seats_count)
            carrying = float(carrying)
            if passenger_seats_count == 0 or carrying == 0:
                return None

            car_type = attribute_list[0]
            brand = attribute_list[1]
            photo_file_name = attribute_list[3]
            return Car(car_type, brand, photo_file_name, carrying,
                       passenger_seats_count)

    def __str__(self):
        attributes = [self.car_type, self.brand, self.photo_file_name, self.carrying, self.passenger_seats_count]
        return ', '.join(map(str, attributes))


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying,
                 body_width=0.0, body_height=0.0, body_length=0.0):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_width = body_width
        self.body_height = body_height
        self.body_length = body_length

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width

    @staticmethod
    def _pars_body_whl(body_whl):
        body_whl = list(filter(lambda x: x.replace('.', '', 1).isdigit(), body_whl.split('x')))
        if len(body_whl) == 3:
            return map(float, body_whl)
        else:
            return 0, 0, 0

    @classmethod
    def from_list(cls, attribute_list):
        if len(attribute_list) >= 5:
            carrying = attribute_list[5]
            if not carrying.replace('.', '', 1).isdigit():
                return None

            carrying = float(carrying)
            if carrying == 0:
                return None

            body_whl = attribute_list[4]
            body_width, body_height, body_length = Truck._pars_body_whl(body_whl)

            car_type = attribute_list[0]
            brand = attribute_list[1]
            photo_file_name = attribute_list[3]
            return Truck(car_type, brand, photo_file_name, carrying, body_width, body_height, body_length)

    def __str__(self):
        attributes = [self.car_type, self.brand, self.photo_file_name, self.carrying,
                      self.body_width, self.body_height, self.body_length]
        return ', '.join(map(str, attributes))


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra

    @classmethod
    def from_list(cls, attribute_list):
        if len(attribute_list) >= 7:
            carrying = attribute_list[5]
            if not carrying.replace('.', '', 1).isdigit():
                return None

            carrying = float(carrying)
            if carrying == 0:
                return None

            car_type = attribute_list[0]
            brand = attribute_list[1]
            photo_file_name = attribute_list[3]
            extra = attribute_list[6]
            return SpecMachine(car_type, brand, photo_file_name, carrying, extra)

    def __str__(self):
        attributes = [self.car_type, self.brand, self.photo_file_name, self.carrying, self.extra]
        return ', '.join(map(str, attributes))


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок

        for row in reader:
            car = CarBase.from_list(row)
            if car is not None:
                car_list.append(car)
    return car_list


if __name__ == '__main__':
    get_car_list(sys.argv[1])
