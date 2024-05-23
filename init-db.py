import mysql.connector

# Підключення до бази даних
db = mysql.connector.connect(
    host="localhost",
    user="administration",
    password="329600",
    database="it-sprout"
)

# Створення курсора для виконання запитів
cursor = db.cursor()

# Створення таблиці для гравців
cursor.execute("CREATE TABLE IF NOT EXISTS players (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), level INT, class VARCHAR(255), coins INT)")

# Створення таблиці для квестів
cursor.execute("CREATE TABLE IF NOT EXISTS quests (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), level_required INT, coins_reward INT, artifacts_reward VARCHAR(255))")

# Створення таблиці для артефактів
cursor.execute("CREATE TABLE IF NOT EXISTS artifacts (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description TEXT)")

# Закриття курсора та збереження змін у базі даних
db.commit()
cursor.close()
db.close()

print("Таблиці успішно створені у базі даних it-sprout.")
