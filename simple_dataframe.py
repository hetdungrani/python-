def create_dataframe(data):
    columns = ['Roll No', 'Student Name', 'Age', 'Course']
    
    rows = [dict(zip(columns, values)) for values in data]

    return rows

student_data = [
    (101, 'het', 19, 'ps'),
    (102, 'krish', 18, 'os'),
    (103, 'shrey', 18, 'cfa')
]

dataframe_like_structure = create_dataframe(student_data)

for row in dataframe_like_structure:
    print(row)
