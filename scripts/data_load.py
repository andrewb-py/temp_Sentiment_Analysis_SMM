import os
import pandas as pd

project_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(project_dir, '..', 'data')

# Проверка, существует ли уже папка с данными во избежание повторной загрузки
if not os.path.exists(data_dir):

    train = pd.read_csv("hf://datasets/MonoHime/ru_sentiment_dataset@a66a66ee3a858c2b59e056b3fb7dfaf501fc5425/train.csv")
    test = pd.read_csv("hf://datasets/MonoHime/ru_sentiment_dataset@a66a66ee3a858c2b59e056b3fb7dfaf501fc5425/valid.csv")

    os.makedirs(data_dir)

    train.to_csv(os.path.join(data_dir, "train.csv"), index=False)
    test.to_csv(os.path.join(data_dir, "test.csv"), index=False)
