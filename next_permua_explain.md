- The question's demand is to give an answer with O(log(n)) time complexity which leads me to the thought of using Binary Search
- However, conducting Binary Search on the entire array is wrong. It is just possible on the ascending part of the array
- My idea is to find the index where the last element of the initial array which is also the biggest number in the array after rotating which is implement in the 
```break_point()``` method as follow:
- Create a mid point of the current array if the value of middle point is smaller than the last one that means the right part is ascending and there is no break_point here, then recursively call the break_point() method with the left part 
- In the opposite case, the middle point value has higher value than the last one of the current array, that means we have moved to the rotated part, and the biggest element is on the right of this middle point or maybe itself. Now we call break_point() method for the right part 
- The method stop when the last is just right after the first element of the current array, if the first element is still smaller then the first one, we conclude that the array has no rotation and unless this, it means we reach the pivot point. 
NOTE: The function just effective if and only if it is the case of the question, where we have two part of an ascending array rotated
- After finding the point, we just conduct Binary Search on the side the value may belongs to  
 