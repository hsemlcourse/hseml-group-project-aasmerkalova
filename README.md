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
│   ├── 02_preprocessing_split.ipynb    # Подготовка данных и сплит (train/val/test)
│   └── 03_baseline.ipynb       # Baseline-модель (Linear Regression)
│   └── 04_models.ipynb.        # Обучение 4+ моделей и ансамблей
│   └── 05_hyperopt.ipynb       # Подбор гиперпараметров
    └── 06_dimensionality_reduction.ipynb  # PCA и визуализация
├── presentation                # Презентация для защиты
├── report
│   ├── images                  # Изображения для отчёта
│   └── report.md               # Финальный отчёт
├── src
│   ├── preprocessing.py        # Предобработка данных
│   └── modeling.py             # Обучение и оценка моделей
├── tests
│   └── test.py                 # Тесты пайплайна
├── pyproject.toml              # Конфигурация ruff и других инструментов
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Запуск

Локальный запуск (без Docker)
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
Запуск через Docker
```bash
# Убедитесь, что Docker Desktop запущен на вашем компьютере. Затем выполните:
docker-compose up --build

#Остановка контейнера:
docker-compose down
```
## Данные
- `data/raw/` — исходные файлы (исходный csv файл скачан с Kaggle)
- `data/processed/` — предобработанные данные после EDA и feature engineering: cleaned_data.csv, а также файлы сплитов (X_train.csv, X_val.csv, X_test.csv, y_train.csv, y_val.csv, y_test.csv).

Сплит: train (60%), validation (20%), test (20%). Фиксированный seed = 42.


## Результаты

| Модель | [R²] | [MAE] | [RMSE] | Примечание |
|GradientBoosting|0.953276|0.966718|1.185269|
|RandomForest|0.952553|0.971392|1.194398|
|Ridge|0.950061 |0.996143 |1.225373|
|ElasticNet|0.950024|0.996074 |1.225818|
| Baseline | 0.9517 | 1.00 | 1.22 | |
| Лучшая модель GradientBoosting | 0.9549 | 0.97 | 1.18 |

## Выбор финальной модели

Финальная модель GradientBoosting с гиперпараметрами:

  - reg__learning_rate: 0.09545214831324028
  - reg__max_depth: 3
  - reg__min_samples_leaf: 1
  - reg__min_samples_split: 3
  - reg__n_estimators: 179
  - reg__subsample: 0.7644148053272926

Лучшее R² (CV): 0.9532

Эксперименты с уменьшением размерности (PCA)

После one-hot кодирования размерность признаков составила 33.
Применение PCA с сохранением 95% дисперсии снизило размерность до 23.

RandomForest + PCA (валидация): R² = 0.9365, MAE = 1.11, RMSE = 1.38
Оригинальный RandomForest (без PCA): R² = 0.9526
Качество модели на PCA-признаках оказалось ниже, поэтому от использования PCA отказались.
Визуализация первых двух главных компонент сохранена в presentation/pca_visualization.png.

## Отчёт

Финальный отчёт: [`report/report.md`](report/report.md)
