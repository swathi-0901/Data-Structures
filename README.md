# Data Structures

## Sorting Technics:


- ### Count Sort:

Counting sort is a stable sorting technique, which is used to sort objects according to the keys that are small numbers. It counts the number of keys whose key values are same. This sorting technique is effective when the difference between different keys are not so big, otherwise, it can increase the space complexity.

Datastructure used here is an array.

Steps for Count Sort algorithm:

1. Find out the maximum element (let it be max) from the given array.
2. Initialize an array of length max+1 with all elements 0. This array is used for storing the count of the elements in the array.
3. Store the count of each element at their respective index in count array
4. Store cumulative sum of the elements of the count array.
5. Find the index of each element of the original array in count array. This gives the cumulative count. Place the element at the index calculated.
6. After placing each element at its correct position, decrease the its count by one.

- ### Heap Sort:

Heap Sort is one of the best sorting methods being in-place and with no quadratic worst-case running time. Heap sort involves building a Heap data structure from the given array and then utilizing the Heap to sort the array.

Heap Sort algorithm:

1. The tree satisfies Max-Heap property, then the largest item is stored at the root node.
2. Remove the root element and put at the end of the array (nth position) Put the last item of the tree (heap) at the vacant place.
3. Reduce the size of the heap by 1 and heapify the root element again so that we have highest element at root.
4. The process is repeated until all the items of the list is sorted.


- ### Selection Sort:

This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.

Selection Sort algorithm:

1. Set MIN to location 0
2. Search the minimum element in the list
3. Swap with value at location MIN
4. Increment MIN to point to next element
5. Repeat until list is sorted


## Searching Technics:


- ### Binary Search:


Binary search is a fast search algorithm with run-time complexity of Ο(log n). This search algorithm works on the principle of divide and conquer. For this algorithm to work properly, the data collection should be in the sorted form.

Datastructure used here is an array.

Steps for Count Sort algorithm:

1. Find the middle element in the sorted list.
2. Compare the search element with the middle element in the sorted list.
3.  If both are not matched, then check whether the search element is smaller or larger than the middle element.
4. If the search element is smaller than middle element, repeat steps for left sublist.
5. If the search element is larger than middle element, repeat steps for right sublist.
6. Repeat the same process until we find the search element in the list or until sublist contains only one element.

- ### Rabin-Karp:

Rabin-Karp is another pattern searching algorithm to find the pattern in a more efficient way. It also checks the pattern by moving window one by one, but without checking all characters for all cases, it finds the hash value. When the hash value is matched, then only it tries to check each character. This procedure makes the algorithm more efficient.

