
class Anagram:

    def anagram(s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        s_list.sort()
        t_list.sort()

        if len(s_list) != len(t_list):
            return False

        for i in range(len(s_list)):
            if s_list.pop() != t_list.pop():
                return False

        return True
