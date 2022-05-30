class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        # instance variables
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    
    # Methods
    def change_name(self, new_name):
       self.name = new_name
       print("Name's changed to ", new_name)
    def change_age(self, new_age):
        self.age = int(new_age)
        print("New age is now ", new_age)
    def add_track(self, new_track):
        self.tracks.insert(-1, new_track)
        print("Track of interest has changed to ", new_track)
    # retrieves instance var
    def get_score(self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print("Score remains", Bob.get_score())
