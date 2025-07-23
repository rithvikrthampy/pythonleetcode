def trace_example():
    nums = [2, 7, 11, 15]
    target = 9
    new_dict = {}
    
    print("Tracing nums = [2,7,11,15], target = 9")
    print("=" * 40)
    
    for i in range(len(nums)):
        current_num = nums[i]
        complement = target - current_num
        
        print(f"Step {i+1}:")
        print(f"  i = {i}, nums[i] = {current_num}")
        print(f"  complement needed = {target} - {current_num} = {complement}")
        print(f"  current dict = {new_dict}")
        
        if new_dict and complement in new_dict:
            result = [new_dict[complement], i]
            print(f"  ✓ Found {complement} at index {new_dict[complement]}!")
            print(f"  Return [{new_dict[complement]}, {i}]")
            return result
        else:
            print(f"  {complement} not found in dict, adding {current_num}: {i}")
            new_dict[current_num] = i
        print()

trace_example()