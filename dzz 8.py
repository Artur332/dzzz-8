import colorama

atrs = dir(colorama)

important_attrs = (
    'init'       # ініціалізація Colorama
    'deinit'     # деініціалізація Colorama
    'Fore'       # колір тексту
    'Back'       # колір фону
    'Style'      # cтиль тексту
    'strip'      # видалення кольорових кодів з тексту
)
