## Problem 2: Skip Iterator(https://leetcode.com/discuss/interview-question/341818/Google-or-Onsite-or-Skip-Iterator)
from collections.abc import Iterator
from collections import Counter
class SkipIterator:
    def __init__(self, iterator: Iterator[int]) -> None:
        self.iterator = iterator
        self.skipCount: Counter[int] = Counter()
        self.nextElement: None|int = None
        self.advance()
    
    def advance(self) -> None:
        self.nextElement = None
        while True:
            val = next(self.iterator, None)
            if val is None:
                break
            
            if self.skipCount[val] > 0:
                self.skipCount[val] -= 1
            else:
                self.nextElement = val
                break

    def hasNext(self) -> bool:
        return self.nextElement is not None

    def next(self) -> int|None:
        if not self.hasNext():
            raise StopIteration('No more elements')

        result = self.nextElement
        self.advance()
        return result
        
    
    def skip(self, val: int) -> None:
        if self.nextElement == val:
            self.advance()
        else:
            self.skipCount[val] += 1


it = SkipIterator(iter([1,2,3,4,5]))
it.skip(1)
it.skip(5)
print(it.hasNext())
print(it.next())
print(it.next())
print(it.hasNext())
print(it.next())
print(it.hasNext())