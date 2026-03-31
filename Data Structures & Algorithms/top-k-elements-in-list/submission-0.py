class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for elem in nums:
            count[elem] = 1+ count.get(elem,0)
        bucket_sort_arr = [[] for i in range (len(nums) + 1)  ]
        
        for c,n in count.items():
            bucket_sort_arr[n].append(c)
        #print(bucket_sort_arr)
        res = []
        for index in range(len(bucket_sort_arr)-1, 0 ,-1 ):
            
            for p in bucket_sort_arr[index]:
                res.append(p)
                if len(res) == k:
                    return res