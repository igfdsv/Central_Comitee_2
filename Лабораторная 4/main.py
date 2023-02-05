class Spell:
    """Класс заклинаний для волшебства"""
    def __init__(self,
                 title: str,
                 description: str,
                 mana_cost: int,
                 min_magic_level: int):
        """
        Создание и подготовка заклинания

        :param title: Название заклинания
        :param description: Описание заклинания
        :param mana_cost: Энергия необходимая для произнесения заклинания
        :param min_magic_level: Минимальный уровень необходимый для произнесения заклинания

        Пример:
        >>> fire_sphere = Spell("Огненный шар", "Широкодоступная магия огня известная с незапамятных времён", 10, 3)
        >>> print(fire_sphere)
        Простейшее заклинание 'Огненный шар'
        Широкодоступная магия огня известная с незапамятных времён
        Стоимость: 10
        """
        self._title = title
        self._description = description
        self._mana_cost = mana_cost
        self._min_magic_level = min_magic_level

    @property
    def title(self):
        """Приватный т.к. этот аспект заклинания не может изменяться"""
        return self._title

    @property
    def description(self):
        """Приватный т.к. этот аспект заклинания не может изменяться"""
        return self._description

    @property
    def mana_cost(self):
        """Приватный т.к. этот аспект заклинания не может изменяться"""
        return self._mana_cost

    def calculate_cast_chance(self,
                              caster_mana: int,
                              caster_level: int) -> int:
        """
        Рассчитывает вероятность удачного сотворения заклинания в процентах

        :param caster_mana: Запас энергии колдуна
        :param caster_level: Магический уровень колдуна
        :return: вероятность удачного сотворения заклинания в процентах
        """
        if caster_level < self._min_magic_level \
           or caster_mana < self.mana_cost:
            return 0
        BASE_CHANCE = 20
        cast_chance = BASE_CHANCE + (caster_level - self._min_magic_level) * 10 + (caster_level - self.mana_cost) * 1
        if cast_chance > 100:
            return 100
        return cast_chance

    def calculate_duration(self, caster_level) -> float:
        """
        Рассчитывает время действия заклинания в секундах

        :param caster_level: Магический уровень колдуна
        :return: время действия заклинания в секундах
        """
        return (caster_level - self._min_magic_level) * 0.5

    def __str__(self):
        difficulty_str = ""
        if self._min_magic_level < 10:
            difficulty_str = "Простейшее"
        elif self._min_magic_level < 25:
            difficulty_str = "Обычное"
        elif self._min_magic_level < 50:
            difficulty_str = "Продвинутое"
        else:
            difficulty_str = "Великое"

        return f"{difficulty_str} заклинание {self.title!r}\n{self.description}\nСтоимость: {self.mana_cost}"

    def __repr__(self):
        return f"{self.__class__.__name__}(title={self.title!r}, description={self.description!r}, mana_cost={self.mana_cost}, min_magic_level={self._min_magic_level})"


class HealingSpell(Spell):
    """Класс заклинаний для лечения"""
    def __init__(self,
                 title: str,
                 description: str,
                 mana_cost: int,
                 min_magic_level: int,
                 heals: int):
        """
        Подготовка и инициализация заклинания лечения

        :param heals: Число очков здоровья которое восстанавливает заклинание
        остальные пар-ры см. в родительском классе

        Пример:
        >>> baseHealing = HealingSpell("Слабое лечение", "Магическое заживление ран и ссадин", 1, 3, 2)
        >>> print(baseHealing)
        Простейшее заклинание 'Слабое лечение'
        Магическое заживление ран и ссадин
        Стоимость: 1
        """
        super().__init__(title, description, mana_cost, min_magic_level)
        self.heals = heals


    # Наследуем метод для рассчёта вероятности сотворения заклинания


    def calculate_duration(self, caster_level) -> float:
        """
        Рассчитывает время действия заклинания в секундах.
        Мощные заклинания лечения имеют более короткое время действия.

        :param caster_level: Магический уровень колдуна
        :return: время действия заклинания в секундах

        Пример:
        "Малое лечение" длиться дольше чем "Сильное восстановление", исполненное столь же искуссным магом
        >>> minorHealing = HealingSpell("Малое лечение", "Походное заклинание клириков", 1, 3, 2)
        >>> minorHealing.calculate_duration(40)
        185.0
        >>> strongRegeneration = HealingSpell("Сильное восстановление", "Магия созданная на полях сражений для спасения в критических ситуациях", 10, 30, 20)
        >>> strongRegeneration.calculate_duration(40)
        5.0
        """
        return super().calculate_duration(caster_level) * (20.0 / self.heals)


    # Наследуем __str__
    

    def __repr__(self):
        return super().__repr__()[:-1] + f", heals={self.heals})"
