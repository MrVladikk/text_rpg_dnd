import random


races = ["Человек", "Эльф", "Дварф", "Халфлинг"]
classes = ["Воин", "Следопыт", "Маг", "Плут"]

locations = {"Деревня": "Тихая деревня, где можно отдохнуть и подготовиться к приключениям.",
    "Лес": "Темный и опасный лес, полный диких зверей и чудовищ.",
    "Пещера": "Мрачная пещера, где скрываются опасные монстры и сокровища.",
    "Замок": "Старый заброшенный замок, где обитают призраки и нежить."}

monsters = {"Гоблин": {"hp": 10, "attack": 2, "defense": 1},
    "Орк": {"hp": 15, "attack": 3, "defense": 2},
    "Тролль": {"hp": 20, "attack": 4, "defense": 3},
    "Скелет": {"hp": 12, "attack": 2, "defense": 1}}

class Character:
    def __init__(self,name,race,char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.hp = random.randint(15,25)
        self.strength = random.randint(8,15)
        self.dexterity = random.randint(8,15)
        self.intelligence = random.randint(8,15)
        self.gold = 10
        self.location = "Деревня"
        
    def stats(self):
        return f"{self.name} - {self.race} {self.char_class}\n" \
               f"HP: {self.hp}, Сила: {self.strength}, Ловкость: {self.dexterity}, Интеллект: {self.intelligence}, Золото: {self.gold}"
    
def battle(player,enemy_name,enemy_stats):
    print(f"Вы столкнулись с {enemy_name}!")
    enemy_hp = enemy_stats["hp"]
    
    while player.hp > 0 and enemy_hp > 0:
        player_damage = max(1, player.strength - enemy_stats["defense"] + random.randint(1, 6))
        enemy_hp -= player_damage
        print(f"Вы атаковали {enemy_name} и нанесли {player_damage} урона. У него осталось {enemy_hp} HP.")
        
        if enemy_hp <= 0:
            print(f"Вы победили {enemy_name}!\n")
            player.gold += random.randint(1,15)
            return True
        
        enemy_damage = max(1, enemy_stats["attack"] - random.randint(0, player.dexterity // 3))
        player.hp -= enemy_damage
        print(f"{enemy_name} атаковал вас и нанес {enemy_damage} урона. У вас осталось {player.hp} HP.\n")
        
        if player.hp <= 0:
            print("Вы проиграли битву. Игра окончена.")
            return False
        
def game():
    print("Добро пожаловать в текстовую RPG!\n")
    
    name = input("Введите имя вашего персонажа: ")
    print("Выберите расу:")
    for i, race in enumerate(races, 1):
        print(f"{i}. {race}")
    while True:
        try:
            race = races[int(input("Введите номер расы: ")) - 1]
            break
        except (ValueError, IndexError):
            print("Неверный ввод. Попробуйте снова.")

    print("Выберите класс:")
    for i, char_class in enumerate(classes, 1):
        print(f"{i}. {char_class}")
    while True:
        try:
            char_class = classes[int(input("Введите номер класса: ")) - 1]
            break
        except (ValueError, IndexError):
            print("Неверный ввод. Попробуйте снова.")
    
    player = Character(name, race, char_class)
    print("\nВаш персонаж создан!")
    print(player.stats())
    
    while player.hp > 0:
        print(f"\nТекущая локация: {player.location}")
        print(locations[player.location])
        print("Что вы хотите сделать?\n1. Перейти в следующую локацию\n2. Осмотреться\n3. Проверить статус персонажа\n4. Выйти из игры")
        action = input("Введите номер действия: ")

        if action == "1":
            if player.location == "Деревня":
                player.location = "Лес"
            elif player.location == "Лес":
                player.location = "Пещера"
            elif player.location == "Пещера":
                player.location = "Замок"
            else:
                print("Вы уже в последней локации.")

        elif action == "2":
            enemy_name, enemy_stats = random.choice(list(monsters.items()))
            if not battle(player, enemy_name, enemy_stats):
                break

        elif action == "3":
            print("\nСтатус персонажа:")
            print(player.stats())

        elif action == "4":
            print("Вы вышли из игры. До свидания!")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")

    print("\nКонец игры.")

if __name__ == "__main__":
    game()