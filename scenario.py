from abc import ABC, abstractmethod


class Antagonist(ABC):
    """
    Абстрактный класс антагонистов
    """
    @abstractmethod
    def attack(self):
        pass


class Cthulhu(Antagonist):
    def attack(self):
        return "Ктулху вылез из моря"


class Joker(Antagonist):
    def attack(self):
        return "Джокер захватил банк"


class Tanos(Antagonist):
    def attack(self):
        return "Танос собирается уничтожить пол вселенной"


class Superhero(ABC):
    """
    Абстрактный класс супергероев
    """
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class ChuckNorris(Superhero):
    def name(self):
        return 'Чак Норрис'

    def attack(self):
        return "Крутой взгляд\n\t\t\U0001F60E"


class Superman(Superhero):
    def name(self):
        return 'Супермэн'

    def attack(self):
        return f"Лазерный луч\n{'-' * 30}"


class IronMan(Superhero):
    def name(self):
        return 'Железный человек'

    def attack(self):
        return "Тони Старк Уничтожил злодея Like a boss\n\t\t\U0001F91F"


class MediaChannel(ABC):
    """
    Абстрактный класс СМИ
    """
    @abstractmethod
    def news(self, superhero, city_name):
        pass


class TV(MediaChannel):
    def news(self, superhero_name, city_name):
        return f"Смотрите на всех каналах: {superhero_name} спас город {city_name}!"


class Newspaper(MediaChannel):
    def news(self, superhero_name, city_name):
        return f"Сегодня в газетах: {superhero_name} спас город {city_name}!"


class EventController:
    """
    Контроллер событий
    """
    def __init__(
            self,
            superhero: Superhero,
            city_name: str,
            media_channel: MediaChannel,
            antagonist: Antagonist
    ):
        self.superhero = superhero
        self.city_name = city_name
        self.media_channel = media_channel
        self.antagonist = antagonist

    def run(self):
        print(self.antagonist.attack())
        print(self.superhero.attack())
        print(self.media_channel.news(self.superhero.name(), self.city_name))


# Города выведены в словарь для корректного отображения на русском языке
cities = {
    'Tyumen': 'Тюмень',
    'Omsk': 'Омск',
    'Moskow': 'Москва',
}

# Привязка антагониста к городу
city_to_antagonist = {
    "Tyumen": Tanos(),
    "Omsk": Joker(),
    "Moskow": Cthulhu(),
}

# Входные данные (можно менять)
superhero = IronMan()  # Супергерой
city = "Moskow"  # Город
media_channel = Newspaper()  # Канал СМИ

# Получаем антагониста для города
antagonist = city_to_antagonist[city]
# Создаем событие со всеми параметрами
event = EventController(superhero, cities[city], media_channel, antagonist)
# Запуск
event.run()
