class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = dict()
        
        # Создаем те самые "корзины". 
        # Размер = len(nums) + 1, потому что число может встретиться максимум len(nums) раз.
        # freq[i] будет хранить список чисел, которые встретились ровно i раз.
        freq = [[] for _ in range(len(nums) + 1)]

        # 2. Считаем частоту каждого числа
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        # 3. МАГИЯ КОРЗИН: перекладываем числа в массив freq
        # метод .items() отдает пары (ключ, значение), то есть (число, частота)
        for num, count in count_map.items():
            freq[count].append(num)

        # 4. Собираем ответ, идя по корзинам с конца (от самой высокой частоты к низкой)
        res = []
        # range(старт, стоп, шаг). Идем от последнего индекса до 0 с шагом -1
        for i in range(len(freq) - 1, 0, -1):
            # В корзине freq[i] может быть несколько чисел, вытаскиваем их
            for num in freq[i]:
                res.append(num)
                # Как только собрали ровно k элементов — мы победили, выходим!
                if len(res) == k:
                    return res
        
