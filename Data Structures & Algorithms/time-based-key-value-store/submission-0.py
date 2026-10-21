class TimeMap:

    def __init__(self):
        # Хранилище: key -> list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Так как timestamps возрастают, просто добавляем в конец
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        arr = self.store[key]
        left, right = 0, len(arr) - 1
        res = ""

        # Бинарный поиск наибольшего timestamp_prev <= timestamp
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]  # Подходящий кандидат
                left = mid + 1     # Ищем еще больший timestamp справа
            else:
                right = mid - 1    # timestamp слишком велик, идем влево

        return res