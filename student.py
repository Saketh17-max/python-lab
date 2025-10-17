class student:
	branch="CSE"
	def read_student_details(self,rno,n):
		self.regdno=rno
		self.name=n
	def print_student_details(self):
	`	print("Student regd.no is", self.regdno)
		print("Student name is", self.name)
		print("Student branch is ", student.branch)
s=student()
s.read_student_details("24PA1A05M4", "SAKETH")
s.print_student_details()
