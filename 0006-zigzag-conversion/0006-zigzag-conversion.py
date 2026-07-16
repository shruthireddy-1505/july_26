class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        curr_row = 0
        d = 1
        row = [""]*numRows

        for i in s:
            row[curr_row] += i

            if curr_row == 0:
                d = 1
            elif curr_row == numRows-1:
                d = -1

            curr_row += d
        return "".join(row)
             