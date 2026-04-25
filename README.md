[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kOqwghv0)
# ML Project — [Название проекта]

**Студент:** [Смеркалова Анастасия Артемовна / Student ID]

**Группа:** БИВ234


## Оглавление

1. [Описание задачи](#описание-задачи)
2. [Структура репозитория](#структура-репозитория)
3. [Запуски](#быстрый-старт)
4. [Данные](#данные)
5. [Результаты](#результаты)
7. [Отчёт](#отчёт)


## Описание задачи

<!-- Кратко опишите задачу: что предсказываем, какой датасет, метрика качества -->

**Задача:** Регрессия

**Датасет:** Starbucks Customer Ordering Patterns (Kaggle). Содержит информацию о заказах: время, локация, кастомизации и др.

**Целевая метрика:** R² – основная. Дополнительно: MAE и RMSE.


## Структура репозитория
Опишите структуру проекта, сохранив при этом верхнеуровневые папки. Можно добавить новые при необходимости.
```
.
├── data
│   ├── processed               # Очищенные и обработанные данные
│   └── raw                     # Исходные файлы
├── models                      # Сохранённые модели 
├── notebooks
│   ├── 01_eda.ipynb            # EDA, очистка, feature engineering
│   ├── 02_preprocessing_split.ipynb    # Подготовка данных и сплит
│   └── 03_baseline.ipynb       # Baseline-модель (Linear Regression)
│   └── 04_models.ipynb.        # Обучение 4+ моделей и ансамблей
│   └── 05_hyperopt.ipynb       # Подбор гиперпараметров
├── presentation                # Презентация для защиты
├── report
│   ├── images                  # Изображения для отчёта
│   └── report.md               # Финальный отчёт
├── src
│   ├── preprocessing.py        # Предобработка данных
│   └── modeling.py             # Обучение и оценка моделей
├── tests
│   └── test.py                 # Тесты пайплайна
├── requirements.txt
└── README.md
```

## Запуск

Этот блок замените способом запуска вашего сервиса.
```bash
# 1. Клонировать репозиторий
git clone <https://github.com/hsemlcourse/hseml-group-project-aasmerkalova.git>
cd <hseml-group-project-aasmerkalova>

# 2. Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

# 3. Установить зависимости
pip install -r requirements.txt
```

## Данные
- `data/raw/` — исходные файлы (исходный csv файл скачан с Kaggle)
- `data/processed/` — предобработанные данные после EDA и feature engineering: cleaned_data.csv, а также файлы сплитов (X_train.csv, X_val.csv, X_test.csv, y_train.csv, y_val.csv, y_test.csv).


## Результаты
Здесь коротко выпишите результаты.
| Модель | [R²] | [MAE] | Примечание |
|--------|-------------|-------------|------------|
| Baseline | 0.9517| 1.00 | |
| Лучшая модель | — | — | |


## Отчёт

Финальный отчёт: [`report/report.md`](report/report.md)
