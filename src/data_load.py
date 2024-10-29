import os
import pandas as pd


def raw_data_load():
    """
    Если не существует файлов с датасетами в папке data, то они скачиваются,
    иначе просто читаются оттуда
    :return: тренировочный и тестовый датасеты
    """

    data_dir = "../data"

    raw_train_path = os.path.join(data_dir, "raw_train.csv")
    raw_test_path = os.path.join(data_dir, "raw_test.csv")

    # Проверка, существуют ли уже файлы с данными во избежание повторной загрузки
    if not (os.path.exists(raw_train_path) and os.path.exists(raw_test_path)):
        train = pd.read_csv(
            "hf://datasets/MonoHime/ru_sentiment_dataset@a66a66ee3a858c2b59e056b3fb7dfaf501fc5425/train.csv")
        test = pd.read_csv(
            "hf://datasets/MonoHime/ru_sentiment_dataset@a66a66ee3a858c2b59e056b3fb7dfaf501fc5425/valid.csv")

        # На случай, если сама папка data уже существует
        try:
            os.makedirs(data_dir)
        except FileExistsError:
            pass

        train.to_csv(raw_train_path, index=False)
        test.to_csv(raw_test_path, index=False)

    train = pd.read_csv(raw_train_path)
    test = pd.read_csv(raw_test_path)

    return train, test