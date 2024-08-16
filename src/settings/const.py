class JsonConst:
    SUCCESS_JSON: dict = {"x": 10, "y": 2}
    SUCCESS_REMAINDER_JSON: dict = {"x": 15, "y": 2}
    SUCCESS_JSON_REMAINDER: dict = {"x": 15, "y": 2}
    FAILED_JSON_KEYS: dict = {"y": 24}
    FAILED_JSON_FORMAT: dict = {"x": "avbs", "y": 24}
    FAILED_JSON_LONG_INT: dict = {"x": 23123124124124124, "y": 123124213}
    FAILED_JSON_ZERO_DIVISION = {"x": 10, "y": 0}


class JsonErrorConst:
    BAD_KEYS: dict = {'statusCode': 2, 'statusMessage': 'Не указаны необходимые параметры'}
    BAD_KEYS_FORMAT: dict = {'statusCode': 3, 'statusMessage': 'Значения параметров должны быть целыми'}
    LONG_INT: dict = {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    BAD_JSON_FORMAT: dict = {'statusCode': 5, 'statusMessage': 'Не допустимый формат json'}
    CALCULATION_ERROR: dict = {'statusCode': 8, 'statusMessage': 'Ошибка вычисления'}


class Const:
    json_const = JsonConst
    json_error_const = JsonErrorConst



