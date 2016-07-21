class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ''
        flag = 0
        while a or b:
            if not a:
                while b:
                    tail = b[-1]
                    b = b[:-1]
                    tail = int(tail)
                    ans = str((tail + flag) % 2) + ans
                    flag = (tail + flag) // 2
                break
            elif not b:
                while a:
                    tail = a[-1]
                    a = a[:-1]
                    tail = int(tail)
                    ans = str((tail + flag) % 2) + ans
                    flag = (tail + flag) // 2
                break
            else:
                tail_a = int(a[-1])
                tail_b = int(b[-1])
                a = a[:-1]
                b = b[:-1]
                ans = str((tail_a + tail_b + flag) % 2) + ans
                flag = (tail_a + tail_b + flag) // 2
        ans = ans if not flag else '1' + ans
        return ans
