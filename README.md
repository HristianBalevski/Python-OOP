# Python-OOP
This is a repository with solutions of problems in SoftUni Course: Python OOP - February 2023.
<br/>
[Click Here for more information about the course Python OOP](https://softuni.bg/trainings/3964/python-oop-february-2023#lesson-49394)
<br/>
<br/>
![OOP](https://user-images.githubusercontent.com/114162692/219875827-5ce8ffd1-1db3-475e-9295-b046bb7453c2.png)

## First Steps in OOP

**What is Scope**
Обхватът в програмирането определя областта на видимост на променливите. В Python, има два основни вида обхват:

1. **Локален обхват (Local Scope):** Дефиниран е в рамките на функцията и включва променливите, декларирани в тази функция.
```
def my_function():
    x = 10  # Локална променлива
    print(x)

my_function()
print(x)  # Грешка: x не е видима тук
```
2. **Глобален обхват (Global Scope):** Дефиниран е извън функциите и включва променливите, декларирани на върховно ниво в скрипта.
```
y = 20  # Глобална променлива

def another_function():
    print(y)

another_function()
print(y)
```
**Namespaces**

Namespaces представляват местата, където се съхраняват имената на променливите и функциите, за да може програмата да ги разпознае. В Python, има няколко видове пространства от имена:

1. **Local Namespace:** Съдържа имената на променливите, дефинирани в момента в дадена функция. Това пространство се създава, когато функцията се извика и се унищожава, когато функцията завърши изпълнението си.

2. **Global Namespace:** Съдържа имената на променливите, дефинирани на върховно ниво в скрипта. Това пространство съществува от момента на стартирането на скрипта и продължава до края му.

3. **Built-in Namespace:** Съдържа вградени имена като функции и обекти в Python, като например print(), len(), и други.

Когато програмата изпълнява код, тя търси имената в тези пространства от имена, според правилата за обхват. Ако не може да открие дадено име в локалното пространство от имена, тя ще потърси в глобалното пространство и така нататък. Това се нарича "LEGB Rule" (Local, Enclosing, Global, Built-in).

**What is Object Oriented Programming (OOP)**

Това е най-популярната парадигма за програмиране. Тя се основава на концепцията за класове и обекти, класът се използва за създаване на индивидуална инстанция на обект.

**Advantages of OOP**

- Осигурява ясна структура на програмата и чист код.
- Улеснява писането на код за многократна употреба.
- Може да тествате всяко поведение на даден обект поотделно.
- Улеснява поддържането и модифицирането на съществуващия код.

**What is an Object**

- 


---

## 5.Inheritance

**В обектно-ориентираното програмиране има четири основни концепции:**

- **Inheritance**: Дава възможност на един клас да наследява методи и свойства от друг клас.
- **Encapsulation**: Ограничава взаимодействието на обекти, за да предпази данните на класа.
- **Abstraction**: Скрива детайлите на имплементацията и се показват само важни методи и свойства.
- **Polymorphism**: Позволява на различни класове да имат методи с еднакви имена.

1. Наследяване

Наследяването е ключова концепция в ООП. То позволява да се създаде нов клас (дете), който наследява свойства и методи от съществуващ клас (родител). Това помага за **повторно използване на кода** и добавяне на функционалности към класовете без промяна на оригиналния им код.

**Има 4 типа наследяване**

**1. Single Inheritance**:<br>
Когато клас наследява от един родителски клас.
```
class Animal:
    def eat(self):
        return "eating..."

class Dog(Animal):
    def bark(self):
        return "barking..."

dog = Dog()
print(dog.eat())  # eating...
print(dog.bark())  # barking...
```
**2. Multiple Inheritance**:<br>
Когато клас наследява повече от един родителски клас.
```
class Father:
    def __init__(self):
        self.father_name = 'Taylor Evans'

class Mother:
    def __init__(self):
        self.mother_name = 'Bet Williams'

class Daughter(Father, Mother):
    def get_parent_info(self):
        return f'Father: {self.father_name}, Mother: {self.mother_name}'

child = Daughter()
print(child.get_parent_info())  # Father: Taylor Evans, Mother: Bet Williams
```
**3. Multilevel Inheritance**:<br>
Когато клас наследява клас, който на свой ред е наследник на друг клас.
```
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

grand_child = GrandChild("John", 19, "Street 15")
print(grand_child.name)  # John
print(grand_child.age)   # 19
print(grand_child.address)  # Street 15
```
**4. Hierarchical Inheritance**:<br>
Когато множество класове наследяват от един родителски клас.
```
class Animal:
    def eat(self):
        return "eating..."

class Dog(Animal):
    def bark(self):
        return "barking..."

class Cat(Animal):
    def meow(self):
        return "meowing..."

# Инстанциране на обекти от класовете Dog и Cat
dog = Dog()
cat = Cat()

print(dog.eat())   # eating... (наследено от Animal)
print(dog.bark())  # barking... (метод на Dog)

print(cat.eat())   # eating... (наследено от Animal)
print(cat.meow())  # meowing... (метод на Cat)
```

**Hybrid Inheritance**
комбинира повече от един тип наследяване. То е смес от **Single, Multiple, Multilevel and Hierarchical Inheritance**. В Python, хибридното наследяване позволява изграждането на по-сложни йерархии на класове, като комбинира предимствата на различни форми на наследяване.
```
class Animal:
    def eat(self):
        return "Eating..."

class Mammal(Animal):
    def walk(self):
        return "Walking..."

class Bird(Animal):
    def fly(self):
        return "Flying..."

class Bat(Mammal, Bird):  # Множествено наследяване
    def sleep(self):
        return "Sleeping..."

# Създаваме обект от клас Bat
bat = Bat()

# Bat има достъп до методи от Animal, Mammal и Bird
print(bat.eat())   # Eating... (от Animal)
print(bat.walk())  # Walking... (от Mammal)
print(bat.fly())   # Flying... (от Bird)
print(bat.sleep()) # Sleeping... (от Bat)
```
![Python inheritance types](https://github.com/user-attachments/assets/f4101ed6-ad2d-4e0f-ad90-f279e10fd6bf)

2. Методът ```super()```

Методът ```super()``` позволява достъп до методите на родителския клас от дъщерния. Използва се за разширяване на функционалността на наследен метод.
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name} is {self.age} years old.'

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_id(self):
        return self.student_id

student = Student("Leo", 20, 10035464)
print(student.get_info())  # Leo is 20 years old.
print(student.get_id())    # 10035464
```
3. Method Resolution Order(MRO)

Методът **MRO** дефинира реда, по който се търсят методи в йерархията при множествено наследяване. В Python се използва **C3 linearization** алгоритъм.
```
class Parent:
    pass

class FirstChild(Parent):
    pass

class SecondChild(Parent):
    pass

class GrandChild(SecondChild, FirstChild):
    pass

print(GrandChild.mro())
# [<class '__main__.GrandChild'>, <class '__main__.SecondChild'>, 
#  <class '__main__.FirstChild'>, <class '__main__.Parent'>, <class 'object'>]
```
4. Mixins

**Mixins** са класове, които предоставят специфични функционалности, но не могат да бъдат инстанцирани самостоятелно. Те се използват за **разширяване на функционалността** на други класове.

Пример: Mixin
```
class RadioMixin:
    def play_song(self, station):
        return f'Playing song on {station}'

class Car(RadioMixin):
    pass

car = Car()
print(car.play_song(95.0))  # Playing song on 95.0
```
Наследяването в Python е мощен инструмент за създаване на гъвкав и преизползваем код. Разбирането на различните форми на наследяване и правилното им прилагане е ключово за ефективното разработване на Python приложения
