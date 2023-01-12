class Solution:
    def totalNQueens(self, N: int):
        self.ans = 0
        def place(i: int, vert: int, ldiag: int, rdiag:int) -> None:
            if i == N: self.ans += 1
            else:
                for j in range(N):
                    vmask, lmask, rmask = 1 << j, 1 << (i+j), 1 << (N-i-1+j)
                    if vert & vmask or ldiag & lmask or rdiag & rmask: continue
                    place(i+1, vert | vmask, ldiag | lmask, rdiag | rmask)
        place(0,0,0,0)
        return self.ans
'''
First, we should consider how the queens will be placed. Since each row can only have one queen, our basic process will be to place a queen and then recurse to the next row. On each row, we'll have to iterate through the possible options, check the cell for validity, then place the queen on the board.

Rather than store the whole board, we can save on space complexity if we only keep track of the different axes of attack in which a queen might be placed. Since a queen has four axes of attack, we'll need to check the three remaining axes (other than the horizontal row, which our iteration will naturally take care of) for validity.

There are N possible columns and 2 * N - 1 possible left-downward diagonals and right-downward diagonals. With a constraint of 1 <= N <= 9, each of the two diagonal states represents up to 17 bits' worth of data and the vertical state up to 9 bits, so we can use bit manipulation to store these states efficiently.

So for each recursive call to place a queen, we should pass along the board state in the form of only three integers (vert, ldiag, rdiag). We can then use bitmasks to check for cell validity before attempting to recurse to the next row.

If we successfully reach the end of the board without failing, we should increment our answer counter (ans).

Time Complexity: O(N!) which represents the maximum number of queens placed
Space Complexity: O(N) for the recursion stack
'''

