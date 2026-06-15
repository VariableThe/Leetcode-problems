class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        failed = 0

        while students and sandwiches and failed < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                failed = 0
            else:
                students.append(students.pop(0))
                failed += 1

        return len(students)
