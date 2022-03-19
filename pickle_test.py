__author__ = 'bunny_gg'
import pickle


class my_object:
    def __init__(self, name):
        self.name = name
        self.hobby = []

    def set_tuzi__new_hobby(self, hobby):
        self.hobby.append(hobby)

    def __str__(self):
        string = self.name
        string += "; hobby: "
        for hobby in self.hobby:
            string+=hobby
            string+=", "
        string = string[:-2]
        return string

# define tuzis
tuzi1 = my_object("baundry")
tuzi1.set_tuzi__new_hobby("laundry")
tuzi2 = my_object("bunker")
tuzi2.set_tuzi__new_hobby("working")
tuzi3 = my_object("bunean")
tuzi3.set_tuzi__new_hobby("cleaning")

# write to file
tuzilist = [tuzi1, tuzi2, tuzi3]
pickle.dump(tuzilist, open("tuzi.txt", "w"))

#read from file
zhu_wish_list = pickle.load(open("tuzi.txt", "r"))
for tuzi in zhu_wish_list:
    print tuzi
