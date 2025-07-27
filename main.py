from idlelib.debugobj_r import remote_object_tree_item

print("python 16th lecture - oop and classes part III")
class Student:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def get_email(self, domain):
        return f"{self.name}_{self.lastname}{self.age}@{domain}.com"

    # __str__ კონსტრუქტორი ინსტანსის გამოძახებისას აბრუნებს კონსტრიქტორში გადაცემულ პირობას
    def __str__(self):
        return f"{self.name} {self.lastname} {self.age} years old"

    # __str__ მეთოდის მსგავსად მუშაობს __repr__, დეველოპერულ მიდგომაა, განსხვავეა ის არის რომ __repr__ ვიყენებ\თ დეველოპერები
    def __repr__(self):
        return f"sutdent({self.name}, {self.lastname}, {self.age})"

# __str__ მეთოდით ვაბრუნებთ ინფორმიაციას მომხმარებლებილათვის, რათა user-friendly იყოს,
# __repr__ მეთოდით ვაბრუნებთ ინფორმაციას დეველოპერებისათვის, dev-friendly რომ იყოს,
# ფუქნციონალი იგივეა, მაგრამ იდეაში და გამოყენებაშია მხოლოდ გასხვავება, მაგრამ თუკი ორივეს ვიყენებთ აუცილებლად __str__ მეთოდს ენიჭება უჭირსტესობა


    def get_full_name(self):
        return f"student name is {self.name} {self.lastname}"






student1 = Student("makho", "okriashvili", 22)
student2 = Student("lasha", "armiranashvili", 25)

print(student1.get_email("gmail"))
print(student1.get_full_name())
# str-ით დაბრუნებული
print(student1)
# repr-ით მითითებული
print(student1.__repr__())
# student2
print(student2.get_email("yahoo"))
print(student2.__repr__())




# ორი ინსტანსის კონკატინაცია/დაჯამება არ შეგვიძლია
try:
    combined_student = (student1 + student2)
except TypeError:
    print("type error, can't concut Class instances")
else:
    print("no error")
    print(combined_student)



# მაგრამ შესაძლებელია class-ების კონკატინაცია/დაჯამება
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    # ინსტანსების კონკატინაცია/დაჯამება მსგავსი მეთოდით არის არასწორი
    # def __str__(self):
    #     return f"{self.x + self.y + self.z}"
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"
    # პასუხს დაგვიბრუნებს მაგრამ ,სგავსი მიდგომა არ არის მიღებული

    # თუმცა, კონკატინაცია/დაჯამება-სათვის ვიყენებთ __add__ მეთოდს
    # def __add__(self, other):
    #     return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)



    # რომელსაც გადაეცემა ორი პარამეტრი, self. და other.
    # self. - აღნიშნავს ამავე კლასის ინსტანსის ატრიბუტებს ხოლო
    # other. - აღნიშნავს იმ ინსტანსის ატრიბუტებს რომელსაც ვამატებთ self.instans-ის ატრიბუტებს

# ამ შემთხვევაში:
# self- აღნიშნავს vector1ის - ატრიბუტბი
vector1 = Vector(1, 2, 3)


# ხოლო other - აღნიშნას vector2-ის ატრიბუტები
vector2 = Vector(4, 5, 6)
# დაკამებისას ჯერ vector2 + vector1 რომ დაგვეწერა იქნებოდა პირიქით, ჯერ რომელიც წერია ეგაა self ხოლო მეორე other
print(vector1 + vector2)
# პირველი ინსტანი გადაეცემა selfად
# მეორე ინსტანსი კი otherად

# isinstance: ამოწმებს მეორე ინსტანსი არის თუ არა პირველი ინსტანსის კლასის მეორე ინსტანსი
# მოკლედ: თუ ორივე ინსტანსი არის ერთი და იმავე კლასის მაშინ isinstance გახდება True,
# ხოლო თუ მეორე ინსტანსი გარე კლასიდან არის შემოტანილი მაშინ გავა Falseზე




# classmethod - კლასმეთოდი: თუ ინსტანსს და კლასის ატრიბუტებს გადავცემთ სხვადასხვა მნიშვნელობას, ზოგადად უპირატესობად მიიღებს ინსტანსის ატრიბუტეს
# მაგრამ თუ გინდა ატრიბუტმა მნიშვნელობად მიიღოს კლასის ატრიბუტის მნიშვნელობა,
# @classmethod უნდა დავადოთ თავზე იმ მეთოდს რომელშიც გვინდა რომ კლასის ატრიბუტის მნიშვნელობა მიიღოს
class Student(object):
    pay = 1000
    discount = 0.7

    def __init__(self, name, age, pay, discount):
        self.name = name
        self.age = age
        self.pay = pay
        self.discount = discount

    def get_pay(self):
        return self.pay * self.discount

    @classmethod
    def student_pay (cls):
        return cls.pay * cls.discount
# როდესაც ვიყენებთ classmethod-ს, def მეთოდს ფრჩხილებში უნდა გადავცეთ cls ნაცვლად selfისა
# მიღებული პრაქტიკაა რომ cls გადავცეთ, ერორზე არ გავა თუკი self-ს გადავცემთ
# cls - არაა საკვანძო სიტყვა



# staticmethod - როდესაც მეთოდს გადავცემთ ისეთ ატრიბუტებს რომელიც არც ინსტანსისაა და არც კლასის,
# და იმისათვის რომ ეს მეთოდი ერორზე არ გავიდეს და გვინდა რომ იმუშაოს, თავზე უნდა დავადოთ @staticmethod
    @staticmethod
    def rest_day():
        day = input("Enter a weekday you want to rest: ")
        return f"you can rest on {day}"

student1 = Student("makho", 22, 800, 0.25)

print(student1.get_pay())
print(student1.student_pay())

# staticmethod-ით შექმნილი მეთოდი
print(student1.rest_day())










class Library:
    def __init__(self, author, age, pay):
        self.authot = author

        # თუკი ატრიბუტს აქვს _ერთი ქვედა ტირე ის არის protected ტიპის
        self._age = age
        # protect-იდ ტიპის ატრიბუტის წვდომა გარედან და მისი შეცვლა შესაძლებელია მაგრამ არაა რეკომენდირებული მისი შეცვლა
        # სინტაქისა ერთი ქვედა ტირე, რომლის დანიშნულებაცაა, მიმანიშნებელია რომ არ შევცვალოთ ეს ატრიბუტი და მასზე წვდომა არ განვახორციელოთ

        # თუკი ორი ქვედა ტირე აქვს მაშინ ის არის private ტიპის
        self.__pay = pay




# protected ატტრიბუტზე წვდომა
    def get_age(self):
        return self._age

# private ატრიბუტებზე წვდომა
    def get_pay(self):
        return self.__pay



    # @property, ატრიბუტად გადააქცევს ჩვენს მიერ შექმნილ მეთოდს
    # მსგავს მეთოდს გამოძახება არ სჭირდება, შეგვიძლია პირდაპირ დავპრინტოთ
    @property
    def get_author_age(self):
        return f"author age is {self._age}"
# @property მეთოდს getterადაც მოიხსენიებენ


# @setter გამოიყენება private მეთოდისთვის, ატრიბუტის მნიშვნელობის შესაცვლელად
# მაგრამ, ჯერ property მეთოდი უნდა გამოვიძახოთ იმავე ატრიბუტზე და შემდგომ setter გამოვიყენოთ
    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def pay(self, value):
        self.__pay = value

    def __str__(self):
        return f"{self.authot} is {self._age} year old"

book1 = Library("dante alighieri", 56, 50)


# private ცვლადებზე წვდომისათვის შეგვიძლია ხელახლა დავუსეტოთ მას მნიშვნელობა და შემდგომ გამოვიძახოთ
book1.__pay = 50
# თუმცა, მსგავსი მიდგომა არასოწრია და არაა მიზანშეწონილი, უმჯობესია კლასში მეთოდი შევქმნათ და იქ გამოვიძახოთ,
# მაგრამ შვილობილ კლასში მშობელი კლასიდან შეუძლებელია გარედან private ატრიბუტებზე წვდომა შეუძლებელია,
# შვილობილ კლასიდან მხოლოდ მეთოდებით შეგვიძლია მათზე წვდომა განვახროციელოთ


# protected ცვლადზე გარედან წვდომა შესაძლებელია და ერორზე არ გავა მარამ უმჯობესია რომ წვდომა არ განვახორციელოთ
print(book1._age)
# პრინტი გამოიტანს _age -ს მაგრამ, მსგავსად მისი გამოტანა არაა სწორი, უმჯობესია რომ კლასში შევქმნათ მეთოდი და ამ მეთოდით  მოვახდინოთ მასზე წვდომა
# როგორც შევქმენით get_age და მეთოდით გამოვიტანეთ იგი
print(book1.get_age())


# მსგავსად, private ცვლადებზე წვდომა არაა მმიზანშეწონილი, უმჯობესია რომ შიგნიდან განვახორციელოთ წვდომა, მეთოდის დახმარებით, როგორ ვიქცეოდით protected ცვლადებზე
# private ატრიბუტებზე გარედან წვდომა შეუძლებელია, გავა ერორზე
print(f"devine comedy costs {book1.__pay} GEL")
# მაგრამ შეგვიძლია private ცვლადს თავიდან დავუსეტოთ მნიშვნელობა და შემდგომ გამოვიძახოთ



# private ატრიბუტებზე წვდომა მეთოდების მეშეობით
print(book1.get_pay())
print(book1.get_author_age)


# getter და setter მეთოდებით მნიშვნელობების შეცვლა!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# setterით pay ატრიბუტის მნიშვნელობა შევცვალეთ 37ით
book1.pay = 37
print(f"discounted price is {book1.pay}")








# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# __call__ მეთოდი ვიყენებთ მეთოდების გამოძახებისას, გადაეცემა ორი პარამეტრი


# class Multiplier:
#     def __init__(self, x):
#         self.x = x
#
#     def str(self, y):
#         return f"{self.x * y}"
#
# num = Multiplier(2)
# print(num(3))
# მსგავასდ str მეთოდის გამოყენება არ შეიძლება და გავა ეროროზე,

# იმისათვის რომ ინსტანსი გამოვიძახოთ უნდა გამოვიყენო call მეთოდი
class Multiplier:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return f"{self.x * y}"

num = Multiplier(2)
# ინსტანსის შექმნისას უნდა გადავცეთ self-ის მნიშვნელობა

print(num(3))
# ხოლო მეთოდის გამოძახებისას უნდა გადავცეთ callის პარამეტრის მნიშვნელობა
# call -ს აუცილებლად გადაეცემა ერთი ატრიბუტი

num2 = Multiplier(4)
print(num2(3))





# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# შევქმნათ დეკორატორი
# დეკორატორის შესაქმნელად ისევ ვქმნით ფუქნციას
# შექმნილ დეკორატორს ქრჩხილებში უნდა გგადაეცე func სიტყვა, რომელიც არ არის საკვანძო სიტყვა მაგრამ მიზანშეწმონილია რომ ესე გადავცეთ
def our_decorator(func):
    def wrapper(*args, **kwargs):
        a = args[0] + 2
        b = args[1] + 2
        return func(a, b)
    return wrapper

# ფუნქციას ისევ გადაეცემა ფუნქცია რომელსაც მიზანშეწონილია რომ სახელად დავარქვათ wrapper
# ამ ფუნქციაში გაუწერეთ ლოგიკა რომ ფუქნციის პირველი და მეორე პარამეტრის მნიშვნელობა უნდა გაზარდოს 2ით
# ფუქნციიაში ჯერ უნდა გამოვიძახოთ func(პარამეტრები), > შემდეგ უნდა გამოვიძახოთ wrapper ფუნქცია

# იმ ფუქნციას რომელსაც თავზე დავადებთ მას დეკორატორის სახით, მათი მნიშვნელობა გაიზრდება 2ით
@our_decorator
def cal_two_number(x, y):
    return f"x = {x}, y = {y}"

print(cal_two_number(3, 4))



# შევქმნათ ფუქნციონალური დეკორეატორი!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import time

# შევქმენით ფუნქცია რომელიც გამოითვლის თუ რა დროს დასჭირდა ალგორითმს შესასრულებლად
# რომელ ფუქნციასაც დავადებთ ამ ფუქნქციუას დეკორატორის სახით გამოგვიტანს იმ დროს რომელიც მას დასჭირდა
def time_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        print(f"function took {time_end - time_start} to execute")
        return result
    return wrapper


@time_decorator
def calculate_area(h, w):
    time.sleep(1)
    return f"area is {h * w * 0.5}"

calculate_area(6, 5)



# class child_vector(Vector):
#     def __init__(self, x, y, z):
#         super.__init__(x, y, z)
#
#
#     def __add__(self, other):
#         return child_vector(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __repr__(self):
#         return f"child_vector({self.x}, {self.y}, {self.z})"
#
# vector2 = child_vector(1, 2, 3)
#
# print(vector1 + vector2)


