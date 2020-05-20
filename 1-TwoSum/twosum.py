class Solution:
    
    ### One pass hash map (Best solution)
    # A simplification of Two pass hash map since we are checking the hashmap as we build it
    # so we only go through it once
    # Time Complexity: O (n)
    # Space Complexity: O(n) for the hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        # Add the number to the hash map with its index
        # Keep track of multiple instances of the same number
        for index, n in enumerate(nums):
            if not n in hash_map:
                hash_map[n] = [index]
            else:
                hash_map[n].append(index)
                
            complement = target - n
            
            if complement in hash_map:
                # if the key is not the same, return
                if not complement == n:
                    return [hash_map[n][0], hash_map[complement][0]]
                
                # if the key is the same, but it has more than one index
                # return the two indices
                elif len(hash_map[n]) >=2:
                    return hash_map[n][:2]
                
                
    
    # Two pass hash map
    # Store all the distinct number in a map
    # If a number occurs more than once track all the indices that it shows up
    # Calculate the complement and search for it in the hash map
    # Time Complexity: O(n + n) -> O(n), where n is the length of nums. Since we have to iterate
    # though all of nums and then through all of the map which could be of size n
    # Space complexity: O(n) for the haspmap
    def twoSum_two_pass_map(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        # Add the number to the hash map with its index
        # Keep track of multiple instances of the same number
        for index, n in enumerate(nums):
            if not n in hash_map:
                hash_map[n] = [index]
            else:
                hash_map[n].append(index)
            
        for key, indices in hash_map.items():
            complement = target - key
            
            # if the complement is in the set
            if complement in hash_map:
                
                # if the key is not the same, return
                if not complement == key:
                    return [hash_map[key][0], hash_map[complement][0]]
                
                # if the key is the same, but it has more than one index
                # return the two indices
                elif len(hash_map[key]) >=2:
                    return hash_map[key][:2]
        
        
            
    
    # Nested Loops
    # This is the brute force solution.
    # 7000 ms, 15 MB. O(n^2) time complexity, O(1) Space complexity
    # For every element of the array, compare it to every other element of the array
    def twoSum_nested_loops(self, nums: List[int], target: int) -> List[int]:
        
        for j_index, j_value in enumerate(nums):
            for i_index, i_value in enumerate(nums):
                if i_value + j_value == target and not i_index == j_index:
                    return [i_index, j_index]
                
    # Two Pointers
    # 50 ms, 15 MB
    # Sorts the array and uses two pointers, one at the start and one at the end
    # Increase the left pointer if temp sum in smaller than target
    # Decreese the right pointer if temp sum in larger than target
    # O(n log(n) ), while the two pointer algorithms is O(n) we have to account for the sort which is O (n log(n))
    # O(1) space complexity since our only extra memory is for the pointers
    def twoSum_two_pointers(self, nums: List[int], target: int) -> List[int]:
        
        sorted_nums = sorted(nums)
        #print(sorted_nums)
        
        # Left Pointer
        left_pointer = 0
        
        # Right Pointer
        right_pointer = len(sorted_nums) - 1
        
        
        while(not left_pointer == right_pointer):
        
            temp_sum = sorted_nums[left_pointer] + sorted_nums[right_pointer]

            if temp_sum == target:
                left = nums.index(sorted_nums[left_pointer])
                nums[left] = float("inf")
                
                right = nums.index(sorted_nums[right_pointer])
                return [left, right]

            if temp_sum < target:
                left_pointer += 1
                
            if temp_sum > target:
                right_pointer -= 1
                
        return []
        
        
        