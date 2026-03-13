import heapq
class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        curr = dummy
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        while heap:
            val, i = heapq.heappop(heap)
            curr.next = lists[i]
            curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                
        return dummy.next
