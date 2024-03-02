class Solution:

    def isPalindrome(s: str) -> bool:
        right_ptr = len(s) - 1
        left_ptr = 0
        s_list = []
        for i in s.lower():
            if i.isalpha():
                s_list.append(i)

        while left_ptr < right_ptr:
            print()
            if s_list[right_ptr] != s_list[left_ptr]:
                return False
            left_ptr = left_ptr + 1
            right_ptr = right_ptr - 1

        return True


def main():
    result = Solution.isPalindrome("0P")
    print(result)

if __name__ == "__main__":
    main()
