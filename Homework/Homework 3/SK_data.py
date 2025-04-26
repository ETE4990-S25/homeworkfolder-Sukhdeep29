import json
class person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }
    
class student(person):
    def __init__(self, first_name, last_name, email, student_id):
        super().__init__(first_name, last_name, email)
        self.student_id = student_id

    def to_dict(self):
        return super().to_dict()
    
class saver:
    def save_to_json(self, filename):
        with open(filename, 'r') as file:
            content = json.load(file)
            print(json.dumps(content, indent = 4))

    def display_json(self, filename):
        with  open(filename, 'r') as file:
            content = json.load(file)
            print(json.dumps(content, indent=4))