class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c0=students.count(0)
        c1=students.count(1)
        for i in range (len(sandwiches)):
            if sandwiches[i]:
                c1-=1
            if not sandwiches[i]:
                c0-=1
            if c0<0 or c1<0:
                return len(students)-i
        return 0