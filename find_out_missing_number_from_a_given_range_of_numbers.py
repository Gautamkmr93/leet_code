from typing import List

class Missing_Number_Solution:
    def __init__(self,list_nums) -> None:
        self.nums=list_nums
        pass

    def missingNumber(self, given_list: List[int]) -> int:
        n = len(given_list)
        number_occurance = [0, ] * (n + 1)
        for num in given_list:
            number_occurance[num] = 1

        for i, occur in enumerate(number_occurance):
            if occur == 0:
                return i

mylist=[1,0,3,5,2]
sol = Missing_Number_Solution(mylist)
print(sol.missingNumber(mylist))

