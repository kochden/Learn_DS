import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Угадываем число через поиск середины диапазона
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    # Ваш код начинается здесь
    count = 0
    lower_range = 1
    upper_range = 100
    predict = int(round((lower_range + upper_range) / 2, 0))
    while number != predict:
        count += 1
        if predict == lower_range:
            predict = upper_range
        elif predict == upper_range:
            predict = lower_range
        else:
            if number > predict:
                lower_range = predict
            elif number < predict:
                upper_range = predict
            predict = int(round((lower_range + upper_range) / 2, 0))
    # Ваш код заканчивается здесь

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
if __name__ == '__main__':
    score_game(game_core_v3)