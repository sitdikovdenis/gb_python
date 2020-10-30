"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""

"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу 
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других 
данных, можно использовать любую подходящую структуру, например словарь"""


"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


from abc import ABC, abstractmethod


class WarehouseIsEmpty(IndexError):
    def __init__(self, name):
        print(f"На складе недостаточно товара {name}")


class Warehouse:
    def __init__(self, square):
        self.square = square
        # equipments - аналог БД, каждый ключ словаря = имя таблицы в значении еще один словарь со столбцами
        Warehouse.equipments = dict()

    @staticmethod
    def equipment_count_validation(count):
        if not str(count).isdigit:
            raise Exception("Для выдачи товара введите целое число")

    # прием техники
    @classmethod
    def technique_reception(cls, equipment, equipment_count):
        cls.equipment_count_validation(equipment_count)
        equipment_name = equipment.__class__.__name__
        table = cls.equipments.get(equipment_name)
        table = table if table is not None else dict()
        t_equipment_count = table.get('equipment_count_on_warehouse')
        t_equipment_count = t_equipment_count if t_equipment_count is not None else 0
        t_equipment_count += equipment_count
        table.update({'equipment_count_on_warehouse': t_equipment_count})
        cls.equipments.update({equipment_name: table})

    # выдача техники
    @classmethod
    def issue_of_equipment(cls, equipment, equipment_count, sub_div):
        cls.equipment_count_validation(equipment_count)
        equipment_name = equipment.__class__.__name__
        table = cls.equipments.get(equipment_name)
        if table is None:
            raise WarehouseIsEmpty(equipment_name)
        t_equipment_count = table.get('equipment_count_on_warehouse')
        if t_equipment_count is None or t_equipment_count == 0:
            raise WarehouseIsEmpty(equipment_name)
        if t_equipment_count is None or t_equipment_count == 0 or t_equipment_count < equipment_count:
            raise WarehouseIsEmpty(equipment_name)

        t_equipment_count -= equipment_count
        # todo в будущем БД надо сделать посерьезнее и вынести location отдельным полем
        table.update({f'equipment_count_on_{sub_div}': equipment_count})
        table.update({'equipment_count_on_warehouse': t_equipment_count})
        Warehouse.equipments.update({equipment_name: table})

    def print_equipments(self):
        print(Warehouse.equipments)


class OfficeEquipment(ABC):
    @staticmethod
    def get_count(location, equipment_name):
        table = Warehouse.equipments.get(equipment_name)
        if table is None:
            return 0
        equipment_count = table.get(f'equipment_count_on_{location}')
        if equipment_count is None:
            return 0
        return equipment_count

    @abstractmethod
    def get_equipment_info(self):
        pass


class Printer(OfficeEquipment):
    def get_equipment_info(self):
        print("Это принтер")


class Scaner(OfficeEquipment):
    def get_equipment_info(self):
        print("Это сканер")


scaner = Scaner()
wh = Warehouse(123)

wh.technique_reception(scaner, 4)
wh.technique_reception(scaner, 3)

printer = Printer()

wh.technique_reception(printer, 4)
wh.technique_reception(printer, 1)
wh.print_equipments()

wh.issue_of_equipment(printer, 4, "it")
wh.print_equipments()

printer_count_on_it = OfficeEquipment.get_count("it", "Printer")
print(printer_count_on_it)
