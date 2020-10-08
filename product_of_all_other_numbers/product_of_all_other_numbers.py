'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # first pass solution with O(n^2) time complexity
    # result = []
    
    # for i in range(len(arr)):
    #     product = 1
    #     for j in range(len(arr)):
    #         if i != j:
    #             product *= arr[j]
    #     result.append(product)
    
    # return result
    
    # optimized solution with O(n) time complexity
    # traversing the arr three times is O(n) + O(n) + O(n)
    # which is O(3n) which is considered O(n)
    
    # for each number in arr, find the product of
    # all the numbers before it and store it in a new array
    products_before_i = [0 for _ in range(len(arr))]
    product = 1
    for i in range(len(arr)):
        products_before_i[i] = product
        product *= arr[i]
    
    # for each number in arr, find the product of
    # all the numbers after it and store it in a new array
    # easy - just traverse arr backwards
    products_after_i = [0 for _ in range(len(arr))]
    product = 1
    for i in range(len(arr) - 1, -1, -1):
        products_after_i[i] = product
        product *= arr[i]
    
    # for each number in arr, multiply the product of
    # all the numbers before it by the product of
    # all the numbers after it
    products_except_i = [0 for _ in range(len(arr))]
    product = 1
    for i in range(len(arr)):
        products_except_i[i] = products_before_i[i] * products_after_i[i]
    
    return products_except_i
        
    

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
