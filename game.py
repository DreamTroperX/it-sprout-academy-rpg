class Player:
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.class_choice = None
        self.coins = 0
        self.artifacts = []
        self.quests_completed = []

    def choose_class(self, player_class):
        self.class_choice = player_class

    def complete_quest(self, quest):
        # Логіка виконання квесту
        self.quests_completed.append(quest)

    def level_up(self):
        self.level += 1

    def earn_coins(self, amount):
        self.coins += amount

    def acquire_artifact(self, artifact):
        self.artifacts.append(artifact)


class Quest:
    def __init__(self, name, level_required, rewards):
        self.name = name
        self.level_required = level_required
        self.rewards = rewards

    def check_requirements(self, player):
        # Перевірка виконання вимог для квесту
        if player.level >= self.level_required:
            return True
        else:
            return False

    def complete_quest(self, player):
        # Логіка виконання квесту та нагороди гравця
        if self.check_requirements(player):
            player.complete_quest(self)
            player.level_up()
            player.earn_coins(self.rewards['coins'])
            for artifact in self.rewards['artifacts']:
                player.acquire_artifact(artifact)
            return True
        else:
            return False


# Приклад використання класів і квестів
player1 = Player("Ім'я гравця")
quest1 = Quest("Базовий квест", 0, {'coins': 100, 'artifacts': ['Сертифікат']})

player1.choose_class("Приключенец")
if quest1.complete_quest(player1):
    print(f"{player1.name} успішно виконав квест {quest1.name} і отримав нагороди!")
    print(f"Рівень: {player1.level}, Монети: {player1.coins}, Артефакти: {player1.artifacts}")
else:
    print(f"{player1.name} не може виконати квест {quest1.name} на даному рівні!")

# Додайте інші класи, квести, артефакти та логіку гри за потреби
