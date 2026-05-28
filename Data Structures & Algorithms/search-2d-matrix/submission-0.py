class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ml=0
        mr=len(matrix)-1
        mm=0
        nl=0
        nr=len(matrix[0])-1
        nm=0

        while ml<=mr:
            mm= ml +((mr-ml)//2)

            if target<matrix[mm][nl]:
                mr=mm-1
            elif target>matrix[mm][nr]:
                mr=mm+1
            else:
                if not target in matrix[mm]:
                    return False
                while nl<=nr:
                    nm = nl + ((nr-nl)//2)

                    if target<matrix[mm][nm]:
                        nr=nm-1
                    elif target>matrix[mm][nm]:
                        nl=nm+1
                    else:
                        return True
        return False
