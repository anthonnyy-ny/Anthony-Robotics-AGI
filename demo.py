


# For loop examples
print("\n=== For Loop Examples ===")

# 1. Basic for loop with range
print("1. Basic for loop with range:")
for i in range(5):
    print(f"Count: {i}")

# 2. For loop with list
print("\n2. For loop with list:")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}")

# 3. For loop with enumerate (get index and value)
print("\n3. For loop with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 4. For loop with dictionary
print("\n4. For loop with dictionary:")
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# 5. For loop with string
print("\n5. For loop with string:")
for char in "Python":
    print(f"Character: {char}")

# 6. For loop with step
print("\n6. For loop with step:")
for i in range(0, 10, 2):
    print(f"Even number: {i}")

# 7. Nested for loop
print("\n7. Nested for loop:")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each row

print("\n" + "="*50)
print("LEETCODE 88: MERGE SORTED ARRAY")
print("="*50)

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Merge nums2 into nums1 in-place.
        nums1 has enough space (length >= m + n) to hold additional elements from nums2.
        """
        # Start from the end of nums1 (position m + n - 1)
        last = m + n - 1
        i = m - 1  # Last element in nums1
        j = n - 1  # Last element in nums2
        
        # Compare elements from the end and place larger one at the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
        
        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1

# Test cases
print("\nTest Case 1:")
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(f"nums1: {nums1[:m]} + {[0]*(len(nums1)-m)}")
print(f"nums2: {nums2}")
print(f"m: {m}, n: {n}")

solution = Solution()
solution.merge(nums1, m, nums2, n)
print(f"Result: {nums1}")

print("\nTest Case 2:")
nums1 = [1]
m = 1
nums2 = []
n = 0
print(f"nums1: {nums1[:m]} + {[0]*(len(nums1)-m)}")
print(f"nums2: {nums2}")
print(f"m: {m}, n: {n}")

solution.merge(nums1, m, nums2, n)
print(f"Result: {nums1}")

print("\nTest Case 3:")
nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(f"nums1: {nums1[:m]} + {[0]*(len(nums1)-m)}")
print(f"nums2: {nums2}")
print(f"m: {m}, n: {n}")

solution.merge(nums1, m, nums2, n)
print(f"Result: {nums1}")

print("\nTest Case 4:")
nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
print(f"nums1: {nums1[:m]} + {[0]*(len(nums1)-m)}")
print(f"nums2: {nums2}")
print(f"m: {m}, n: {n}")

solution.merge(nums1, m, nums2, n)
print(f"Result: {nums1}")

# Alternative solution using built-in sort (not recommended for interview)
print("\n" + "-"*30)
print("Alternative Solution (using sort):")
print("-"*30)

def merge_alternative(nums1, m, nums2, n):
    """
    Alternative solution using built-in sort
    Note: This is not the most efficient for interviews
    """
    # Copy nums2 elements to nums1
    for i in range(n):
        nums1[m + i] = nums2[i]
    
    # Sort the entire array
    nums1.sort()

# Test the alternative solution
print("\nTest Case 1 (Alternative):")
nums1_alt = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(f"nums1: {nums1_alt[:m]} + {[0]*(len(nums1_alt)-m)}")
print(f"nums2: {nums2}")

merge_alternative(nums1_alt, m, nums2, n)
print(f"Result: {nums1_alt}")

print("\n" + "="*50)
print("EXPLANATION:")
print("="*50)
print("""
Key Points:
1. nums1 has enough space (length >= m + n)
2. We merge from the end to avoid overwriting elements
3. Time Complexity: O(m + n)
4. Space Complexity: O(1) - in-place modification

Algorithm:
1. Start from the end of nums1 (position m + n - 1)
2. Compare elements from both arrays from the end
3. Place the larger element at the end
4. Continue until all elements are placed
5. If nums2 has remaining elements, copy them
""")

