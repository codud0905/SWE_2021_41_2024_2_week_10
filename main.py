from typing import List

# even_list 함수 구현
def even_list(int_list: List[int]) -> List[int]:
    """
    짝수인지 확인하고 짝수 리스트를 반환합니다.
    
    Args:
        int_list: 정수 리스트.
        
    Returns:
        짝수로만 이루어진 리스트.
    """
    return [x for x in int_list if x % 2 == 0]

# sum_of_squares_of_even 함수 구현
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    모든 짝수의 제곱의 합을 계산합니다.
    
    Args:
        even_int_list: 짝수 리스트.
        
    Returns:
        모든 짝수의 제곱의 합.
    """
    return sum(x ** 2 for x in even_int_list)

# Main function
def main():
    # 예제 리스트
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

# Boilerplate code
if __name__ == "__main__":
    main()
