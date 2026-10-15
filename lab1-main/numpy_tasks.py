# numpy_tasks.py
import numpy as np
from grader_contracts.numpy_tasks import MatrixStatistics, TimeSeriesStatistics


def sum_prod(data):
    """Сумма произведений матриц на соответствующие векторы."""
    matrices = data.matrices
    vectors = data.vectors
    result = None
    for m, v in zip(matrices, vectors):
        prod = m @ v
        result = prod if result is None else result + prod
    return result


def binarize(data):
    """Бинаризация матрицы: > threshold -> 1, иначе -> 0."""
    matrix = data.matrix
    threshold = data.threshold
    return np.where(matrix > threshold, 1, 0)


def unique_rows(data):
    """Уникальные элементы каждой строки матрицы."""
    return [np.unique(row).tolist() for row in data.matrix]


def unique_columns(data):
    """Уникальные элементы каждого столбца матрицы."""
    matrix = data.matrix
    return [np.unique(matrix[:, i]).tolist() for i in range(matrix.shape[1])]


def matrix_statistics(data):
    """Случайная матрица нормального распределения + статистики."""
    np.random.seed(data.seed)
    matrix = np.random.normal(data.mean, data.std, size=(data.rows, data.columns))
    row_means = np.mean(matrix, axis=1)
    row_vars = np.var(matrix, axis=1)
    column_means = np.mean(matrix, axis=0)
    column_vars = np.var(matrix, axis=0)
    return MatrixStatistics(matrix, row_means, column_means, row_vars, column_vars)


def chess(data):
    """Шахматная матрица размера rows x columns из first и second."""
    m, n = data.rows, data.columns
    a, b = data.first, data.second
    matrix = np.zeros((m, n), dtype=type(a))
    for i in range(m):
        for j in range(n):
            matrix[i, j] = a if (i + j) % 2 == 0 else b
    return matrix


def draw_rectangle(data):
    """Рисует прямоугольник по центру изображения."""
    img = np.full(
        (data.image_height, data.image_width, 3),
        data.background_color,
        dtype=np.uint8,
    )
    x_start = (data.image_width - data.width) // 2
    y_start = (data.image_height - data.height) // 2
    img[y_start:y_start + data.height, x_start:x_start + data.width] = data.shape_color
    return img


def draw_ellipse(data):
    """Рисует эллипс по центру изображения."""
    img = np.full(
        (data.image_height, data.image_width, 3),
        data.background_color,
        dtype=np.uint8,
    )
    cx = data.image_width // 2
    cy = data.image_height // 2
    y, x = np.ogrid[:data.image_height, :data.image_width]
    mask = ((x - cx) / data.semi_axis_x) ** 2 + ((y - cy) / data.semi_axis_y) ** 2 <= 1
    img[mask] = data.shape_color
    return img


def analyze_time_series(data):
    """Анализ временного ряда."""
    series = np.asarray(data.values, dtype=float)
    window = data.window

    mean = float(np.mean(series))
    variance = float(np.var(series))
    std = float(np.std(series))

    local_maxima_indices = []
    local_minima_indices = []
    for i in range(1, len(series) - 1):
        if series[i] > series[i - 1] and series[i] > series[i + 1]:
            local_maxima_indices.append(i)
        if series[i] < series[i - 1] and series[i] < series[i + 1]:
            local_minima_indices.append(i)

    # Скользящее среднее по окну window
    if window <= len(series):
        moving_average = np.convolve(series, np.ones(window) / window, mode='same')
    else:
        moving_average = np.array([])

    return TimeSeriesStatistics(
        mean, variance, std,
        local_maxima_indices, local_minima_indices, moving_average,
    )


def one_hot(data):
    """One-hot encoding для вектора меток."""
    labels = np.asarray(data.labels)
    num_classes = data.class_count if data.class_count is not None else int(np.max(labels)) + 1
    result = np.zeros((len(labels), num_classes), dtype=int)
    for i, label in enumerate(labels):
        result[i, label] = 1
    return result