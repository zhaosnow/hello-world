# 滚动数组
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sumup = [[], []]
        zigzag = 0
        for i in range(len(triangle)):
            row = triangle[i]
            if i == 0:
                sumup[zigzag].append(row[0])
                zigzag = 1 - zigzag
            else:
                for j in range(len(row)):
                    if j == 0:
                        if sumup[zigzag]:
                            sumup[zigzag][0] = row[0] + sumup[1 - zigzag][0]
                        else:
                            sumup[zigzag].append(row[0] + sumup[1 - zigzag][0])
                    elif j == len(row) - 1:
                        sumup[zigzag].append(row[-1] + sumup[1 - zigzag][-1])
                    else:
                        if j < len(sumup[zigzag]):
                            sumup[zigzag][j] = min(sumup[1 - zigzag][j], sumup[1 - zigzag][j - 1]) + row[j]
                        else:
                            sumup[zigzag].append(min(sumup[1 - zigzag][j], sumup[1 - zigzag][j - 1]) + row[j])
                zigzag = 1 - zigzag
        return min(sumup[1 - zigzag])
