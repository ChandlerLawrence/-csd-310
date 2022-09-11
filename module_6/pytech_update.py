from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.csqemc6.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
print(" Student ID: 1007 \n First Name: Chander \n Last Name: Lawrence \n")
print(" Student ID: 1008 \n First Name: John \n Last Name: Doe \n")
print(" Student ID: 1009 \n First Name: Alex \n Last Name: James \n")
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")
print(" Student ID: 1007 \n First Name: Chander \n Last Name: Lawrence \n")
input("\n\n  End of program, press any key to continue...")