class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # сохраняем ссылку на следующий
            curr.next = prev       # разворачиваем указатель
            prev = curr            # сдвигаем prev вперед
            curr = next_node       # сдвигаем curr вперед
            
        return prev