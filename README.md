# Python-OOP
This is a repository with solutions of problems in SoftUni Course: Python OOP - February 2023.
<br/>
[Click Here for more information about the course Python OOP](https://softuni.bg/trainings/3964/python-oop-february-2023)
<br/>
<br/>
![OOP](https://user-images.githubusercontent.com/114162692/219875827-5ce8ffd1-1db3-475e-9295-b046bb7453c2.png)

## 01.First Steps in OOP

**1.Project Architecture**

**Разделяне на кода на логически части**: Основната идея е да се разделя кодът на функции и методи, които изпълняват определени задачи. Това прави кода по-четим и лесен за дебъгване. Например, кодът за обработка на различни действия може да се раздели в отделни функции:

```
def move_enemies():
    # логика за движение на враговете

def killer_check():
    # логика за проверка на убиец

def move_player(move):
    # логика за движение на играча

for move in moves:
    move_enemies()
    killer_check()
    move_player(move)
```

**2.Splitting Code into Functions**

**Принципи**: Всяка функция трябва да изпълнява само една задача.

- ```withdraw()```: само за теглене.
- ```deposit()```: само за внасяне.
- Избягва се комбинирането на функционалност, като ```deposit_and_get_balance()```, тъй като това прави функцията по-сложна и трудна за поддръжка.

**3.Scope and Namespace**

**Namespace**: Представлява пространството, където се съхраняват имената на обектите. В Python имаме три основни пространства от имена:

- Вградено (Built-in)
- Глобално (Global)
- Локално (Local)

```
def scopes():
    text = "global text"
    
    def local_scope():
        text = "local text"
    
    def nonlocal_scope():
        nonlocal text
        text = "nonlocal text"
    
    def global_scope():
        global text
        text = "global text"
```

**4.Basics of OOP**

**What is an Object-Oriented Programming?**

Обектно-ориентираното програмиране е един от най-популярните подходи за програмиране, който организира кода чрез обекти и класове. Това е методология, която цели да структурира програмите така, че да бъдат по-разбираеми, поддържани и разширяеми.

**Objects in Python**

Всичко в Python е обект и има тип.

- 10.5
- "Python"
- [1, 2, 3, 4]
-  {"name": "Peter", "age": 26}

Можем да създаваме колкото си искаме обекти, да ги манипулираме, или да ги премахваме.

**What is an Object?**

- Обектът е абстракция на данни, който има състояние (атрибути) и поведение (методи).

  ```
  class Phone:
    def __init__(self, color, size):
        self.color = color
        self.size = size
    
    def turn_on(self):
        return "The phone is turned on"
  ```
**What is a Class?**

- Класът е шаблон, от който се създават обекти. В класа се дефинират атрибутите и методите, които обектите от този клас ще притежават.
- Всеки обект на класа има собствено състояние, но споделя еднакво поведение с останалите обекти от същия клас.
 
**What is an Instance?**
- Инстанцията е конкретен обект, създаден от даден клас. Процесът на създаване на обект от клас се нарича **инициализация** или **инстанциране**.
  ```
  my_phone = Phone("blue", 4.7)
  ```
      
**Advantages of OOP**

- **Ясна структура на програмата**:
  - ООП организира кода около **класове** и **обекти**, което създава логическа структура на програмата. Това прави програмата по-лесна за разбиране и поддръжка.

- **Намалена сложност**:
  - ООП позволява разделянето на сложни проблеми на по-малки, по-управляеми части. Всяка част от проблема се решава чрез класове, които дефинират обекти с определено поведение.

- **Многократна употреба на код**:
  - Един от най-големите плюсове на ООП е възможността за повторна употреба на код. **Наследяването** позволява създаването на нови класове на базата на вече съществуващи. Това намалява дублирането на код и подобрява ефективността на разработката.
 
- **Лесно тестване на поведението на обектите**:
  - Чрез инкапсулиране на поведението на обектите вътре в класовете, можеш лесно да тестваш отделни части от програмата, без да се налага да стартираш цялата система. Всеки метод може да бъде тестван изолирано, което улеснява **юнит тестинга**.
 
- **Улеснява поддръжката и модификацията на кода**
  - Поради ясната структура и капсулирането на поведението в обектите, ООП улеснява **поддръжката и разширението на програмата**. Можеш да добавяш нови функционалности без да се налага да променяш големи части от съществуващия код.
 
**5.Creating and Using Classes**

- **Пример за клас Book**: Приема име, автор и брой страници при инициализация.
  
  ```
  class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

  book = Book("My Book", "Me", 200)
  print(book.name)  # My Book
  print(book.author)  # Me
  print(book.pages)  # 200
  ```
- **Методите** са функции, които работят само вътре в съответния клас.
  
  ```
  class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine
    
    def get_info(self):
        return f'This is {self.name} {self.model} with engine {self.engine}'

  car = Car("Kia", "Rio", "1.3L B3 I4")
  print(car.get_info())  # This is Kia Rio with engine 1.3L B3 I4
  ```
  ООП предоставя ясна структура на програмата, намалява сложността и улеснява поддръжката и модификацията на съществуващия код.

---

## 02. Classes and Objects

**1.Classes and Instances**

- **Класовете** в Python поддържат две основни операции:
  - **Достъп до атрибути** с оператор ```.```.
  - **Инстанция** (създаване на обект) чрез извикване на класа като функция.

  Пример:

  ```
  class Example:
    text = 'Hello'
    def print_text(self):
        return 'SoftUni'

  Example.text  # референция към атрибут на класа
  Example.print_text  # референция към метод на класа
  x = Example()  # инстанциране

  ```

**2.Instantiation**

Инстанцирането създава нов обект от класа:

```
class Person:
    name = "George"
    age = 25

person = Person()
print(person.name)  # George
print(person.age)  # 25
```

- Методът ```__init__``` се извиква автоматично при създаване на нов обект:
- ```self``` служи за референция към конкретната инстанция на класа и се използва за свързване на атрибутите с дадените аргументи.
  ```
  class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model

  my_laptop = Laptop("Inspiron 15", "Dell")
  print(my_laptop.name)   # Inspiron 15
  print(my_laptop.model)  # Dell
  ```

**3.Attributes**

Атрибутите са два вида:

- Methods.
- Data Attributes.

**4.Methods**

- Методите са функции, които описват поведението на обектите.
- Първият аргумент на методите по конвенция е **self**.

Пример:

```
class MyClass:
    def say_hello(self):
        return 'Hello'

x = MyClass()
x.say_hello()  # конвенционален начин
MyClass.say_hello(x)  # еквивалентен начин
```

**5.Special / Dunder Methods**

Това са вградени методи, обградени с двойни долни черти, които обогатяват дизайна на класа и подобряват четливостта.
Например: ```__init__```, ```__str__```, ```__repr__```, ```__dict__``` и др.

```
class Dog:
    def__init__(self, name):
        self.name = name

x = Dog("Max")
print(x.__dict__) # {"name": "Max"}
```

**6.Data Attributes**

- **Data attributes** са стойности, които се съхраняват вътре в един обект и определят неговото състояние. Те могат да бъдат:
  - **Инстанционни атрибути** (instance variables) – уникални за всяка инстанция на класа.
  - **Класови атрибути** (class variables) – споделени между всички инстанции на класа.
 
**Инстанционни атрибути**

- Дефинират се вътре в метода ```__init__()```, и техните стойности могат да бъдат различни за всеки обект.

**Класови атрибути**

- Определят се директно в тялото на класа (извън методите) и тяхната стойност е обща за всички инстанции на класа.

**Пример: Instance vs Class Variables**

```
class Laptop:
    brand = "Dell"  # Класов атрибут, споделен от всички обекти

    def __init__(self, model):
        self.model = model  # Инстанционен атрибут, уникален за всеки обект

# Създаваме две инстанции на класа Laptop
laptop1 = Laptop("Latitude 5300")
laptop2 = Laptop("Inspiron 15")

# Достъп до инстанционни и класови атрибути
print(laptop1.brand)  # Dell (класов атрибут)
print(laptop2.brand)  # Dell (същия класов атрибут)

print(laptop1.model)  # Latitude 5300 (уникален за laptop1)
print(laptop2.model)  # Inspiron 15 (уникален за laptop2)
```

**Пример за лоша практика с класови променливи**

Ако класов атрибут се използва за съхраняване на данни, които трябва да бъдат уникални за всяка инстанция, всички инстанции ще споделят една и съща стойност. Това може да доведе до неочаквани резултати:

```
class Dog:
    tricks = []  # Класов атрибут, споделен от всички инстанции

    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.tricks.append('roll over')  # Добавяме трик на dog1
print(dog2.tricks)  # ['roll over'] - споделено с dog2, което е нежелано
```

**Добра практика за инстанционни променливи**

За да се избегне нежелано споделяне на стойности, атрибути, които трябва да са уникални за всяка инстанция, трябва да се декларират като **инстанционни променливи**:

```
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []  # Инстанционен атрибут, уникален за всяка инстанция

dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.tricks.append('roll over')  # Добавяме трик на dog1
dog2.tricks.append('play dead')  # Добавяме трик на dog2

print(dog1.tricks)  # ['roll over']
print(dog2.tricks)  # ['play dead']
```

---

## 03.Inheritance

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
Обобщение:

Наследяването в Python е мощен инструмент за създаване на гъвкав и преизползваем код. Разбирането на различните форми на наследяване и правилното им прилагане е ключово за ефективното разработване на Python приложения.

---

## 04.Encapsulation

Енкапсулацията е основен принцип в обектно-ориентираното програмиране, който позволява обединяването на данни и методи в един компонент (клас), и контролирането на достъпа до тях.
Python използва конвенции за енкапсулация, вместо строго налагане от езика:

- **Public**: по подразбиране всички атрибути и методи са публични.
- **Protected**: използва един долен индикатор ```_```, достъпът е само вътре в класа и неговите подкласове.
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

person = Person('Peter', 25)
print(person.name)  # Peter
print(person._age)  # 25 (достъпно, но по конвенция не трябва да се използва извън класа)
```
- **Private**: използва два долни индикатора ```__```, достъпът е ограничен само в класа, чрез механизма **name mangling**.
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def info(self):
        print(f"I am {self.name}, {self.__age} years old.")

person = Person('Peter', 25)
person.info()  # I am Peter, 25 years old.
print(person.__age)  # AttributeError
```
**1. Name Mangling**

Python използва ```name mangling``` за атрибути с двойно подчертаване. Това променя името на атрибута, за да се избегне конфликти в подкласовете.
```
class Car:
    def __init__(self):
        self.__max_speed = 200
    
    def drive(self):
        print(f"Driving max speed {self.__max_speed}")

car = Car()
car.drive()  # Driving max speed 200
car.__max_speed = 300  # Това създава нов атрибут, не променя оригиналния
car.drive()  # Все още извежда: Driving max speed 200
print(car._Car__max_speed) # 200 - достъп до частен атрибут чрез name mangling
```
**2. Getters and Setters**:

Гетърите и сетърите позволяват контрол върху това как се достъпват и променят частни атрибути.

Пример:
```
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age

person = Person("Peter", 25)
print(person.get_age())  # 25
person.set_age(30)
print(person.get_age())  # 30
```
**Properties**:

Декоратора ```@property``` е "Pythonic" начин за използване на гетъри и сетъри.
```
class Person:
    def __init__(self, age):
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError("Age must be positive")

person = Person(25)
print(person.age)  # 25
person.age = 30
print(person.age)  # 30
```
**3. Вградени функции за достъп до атрибути**

- ```getattr(object, attribute)```: достъп до атрибут по име.
- ```hasattr(object, attribute)```: проверка дали обектът има даден атрибут.
- ```setattr(object, attribute, value)```: задаване на стойност на атрибут.
- ```delattr(object, attribute)```: изтриване на атрибут.

```
class Person:
    def __init__(self, name):
        self.name = name

person = Person('Peter')
print(getattr(person, 'name'))  # Peter
print(hasattr(person, 'age'))   # False
setattr(person, 'age', 25)
print(person.age)               # 25
delattr(person, 'age')
print(hasattr(person, 'age'))   # False
```

Тези концепции са ключови за създаването на добре структуриран и поддържаем Python код, особено в контекста на уеб разработката, където правилното управление на данните и контролът на достъпа са от съществено значение.

---

## 05.Static and Class Methods

**1.Static Methods**

Статичните методи са независими от състоянието на класа или инстанцията. Те се дефинират с декоратора ```@staticmethod```.

- Статичният метод не знае нищо за състоянието на обекта или класа, на който е извикан.
- Той не може да променя състоянието на обекта или класа.
- Може да бъде извън класа, но се използва вътре, когато е логически свързан с него.
- Статичните методи не приемат параметъра ```self```, тъй като не работят със състоянието на обекта.

```
class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age):
        return age >= 18

print(Person.is_adult(5))  # False
girl = Person("Amy")
print(girl.is_adult(20))   # True
```
В този пример методът ```is_adult``` е независим от състоянието на класа или обекта и може да се извика както с клас, така и с инстанция.

**Предимства на статичните методи:**

- Показват, че даден метод е независим от останалото в класа.
- Помагат да се избегнат случайни модификации, които противоречат на оригиналния дизайн.
- Лесни са за тестване, защото са напълно изолирани.

**2.Class Methods**

- Дефинират се с декоратора ```@classmethod```.
- Те са свързани с класа, а не с конкретна инстанция.
- Могат да променят състоянието на класа, което ще се отрази на всички инстанции.
- Първият параметър е самият клас (обикновено се нарича cls)

```
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(["tomato sauce", "parmesan", "pepperoni"])

    @classmethod
    def quattro_formaggi(cls):
        return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])

first_pizza = Pizza.pepperoni()
second_pizza = Pizza.quattro_formaggi()
```
В този пример клас методите се използват за създаване на различни видове пици. Методите като ```pepperoni``` и ```quattro_formaggi``` създават инстанции на класа с предварително дефинирани съставки.

**Предимства на клас методите:**

- Клас методите предоставят лесен начин за създаване на нови обекти (т.нар. "factory methods").
- Следват принципа DRY (Don't Repeat Yourself), като се избягват излишни повторения при създаване на инстанции.

**3.Overriding Using Class Methods**

Методите могат да бъдат пренаписани в наследени класове, като се използват класови методи за валидиране.

```
class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(value):
        if value < Person.min_age or value > Person.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

--------------------------------------------------------------------------

class Employee(Person):
    min_age = 16
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(value):
        if value < Employee.min_age or value > Employee.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value
```

---

## 06.Polymorphism and Abstraction

- Polymorphism се състои от 2 Гръцки думи, poly(много) и morphism(форми).
- Полиморфизмът означава, че различни класове могат да използват един и същ метод, но с различна реализация. Това е ключова концепция в OOP, защото позволява на различни обекти да бъдат обработвани чрез общ интерфейс.

**Пример:**

```
class Shape:
    def calculate_area(self):
        return None

class Square(Shape):
    side_length = 2
    def calculate_area(self):
        return self.side_length ** 2

class Triangle(Shape):
    base_length = 4
    height = 3
    def calculate_area(self):
        return 0.5 * self.base_length * self.height

shapes = [Square(), Triangle()]
for shape in shapes:
    print(shape.calculate_area())
```
В този пример методът ```calculate_area``` е полиморфен – различните фигури (квадрат и триъгълник) го реализират по различен начин, но можем да ги обработваме по един и същи начин чрез основния клас ```Shape```.

**Compile-Time Polymorphism:**

Python не поддържа **compile-time polymorphism** или **method overloading**. Ако се опитаме да създадем два метода с едно и също име, вторият ще замести първия.

```
class Person:
    def say_hello():
        return "Hi!"
    def say_hello():
        return "Hello"

print(Person.say_hello())  # Hello
```

**Overloading Built-in Methods**

- Можем да променим поведението на функции като **len**, **abs**, **str**, **repr** и др.
- За да направим това, трябва просто да дефинираме съответния магически метод.

```
class MyClass:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __len__(self):
        return self.size


my_class = MyClass("Class Name", 3)
print(len(my_class))  # 3
```

Пример: Overloading ```__add__()```

- Ако имаме **class Purchase** и искаме да сметнем всички разходи използвайки оператора **+**, можем да ползваме ```__add__``` метода.

```
class Purchase:
    def __init__(self, product_name, cost):
        self.product_name = product_name
        self.cost = cost

    def __add__(self, other):
        name = f'{self.product_name}, {other.product_name}'
        cost = self.cost + other.cost
        return Purchase(name, cost)

first_purchase = Purchase('sofa', 650)
second_purchase = Purchase('table', 150)
total = first_purchase + second_purchase
print(total.product_name, total.cost)  # sofa, table; 800
```

Пример: Overloading ```__gt__()```

- Ако имаме **class Person** и искаме да сравним техните заплати ползвайки оператора **>**, можем да ползваме  метода ```__gt__```.

```
class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

person_one = Person('John', 20)
person_two = Person('Natasha', 36)
print(person_one > person_two)  # False
```

**Duck Typing**

Duck Typing е подход в Python, при който типът на обекта не е важен, стига обектът да има необходимите методи. Това ни позволява да използваме един и същ код за различни типове обекти, които споделят сходна функционалност.

Пример:

```
class Cat:
    def sound(self):
        print("Meow!")

class Train:
    def sound(self):
        print("Sound from wheels slipping!")

def make_sound(obj):
    obj.sound()

make_sound(Cat())   # Meow!
make_sound(Train())  # Sound from wheels slipping!
```

**What is an Abstraction**

- Абстракцията е принцип в OOP, който скрива ненужните детайли и показва само съществената информация за обекта. Абстрактните класове са класове, които съдържат абстрактни методи – методи без имплементация, които задължават наследниците си да ги реализират.
- Абстрактен метод е метод, който се декларира но не се имплементира.

Пример:

```
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return 3.14 * self._radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self._radius
```

В този пример класът ```Shape``` е абстрактен и съдържа два абстрактни метода, които класът ```Circle``` трябва да имплементира.

---

## 07.SOLID

**1.Single Responsibility Principle (SRP)**

Всеки клас трябва да има само една причина за промяна, тоест трябва да бъде отговорен за само една задача или функционалност.

**Пример за нарушение на SRP:**

```
class Student:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def register(self, student):
        # Регистрация в база данни
        pass
```
Тук, класът ```Student``` отговаря както за управление на данните на студента, така и за регистрацията му в базата данни. Това нарушава **SRP**, защото при промяна на начина на управление на данните или на базата данни, ще трябва да променяме класа.

**Решение:**
Разделяме отговорностите на два класа:

```
class Student:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class StudentRecords:
    def register(self, student):
        # Регистрация в база данни
        pass
```
Тук всеки клас има една отговорност: ```Student``` е отговорен за информацията на студента, а ```StudentRecords``` за работата с базата данни.

**2.Open/Closed Principle (OCP)**

Софтуерните единици (като класове, модули, функции) трябва да са отворени за разширяване, но затворени за промени. Това означава, че трябва да можем да добавяме нова функционалност, без да променяме съществуващия код.

**Пример за нарушение на OCP:**

```
class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4
        elif self.average_grade > 4:
            return self.semester_tax * 0.2
        return 0
```
Ако искаме да добавим нова отстъпка (например за студенти с оценка над 3), ще трябва да променим класа, което нарушава OCP.

**Решение:**
Можем да наследим класа и да добавим нова логика, без да променяме вече съществуващия код:

```
class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        result = super().get_discount()
        if result:
            return result
        if 3 < self.average_grade <= 4:
            return self.semester_tax * 0.1
        return 0
```
Тук използваме наследяване, за да добавим новата функционалност, без да пипаме оригиналния клас.

**3.Liskov Substitution Principle (LSP)**

Наследените класове да могат да заменят базовия клас, без да нарушават функционалността на програмата. Тоест, обектите на подтипове трябва да могат да се използват навсякъде, където се използват обекти на базовия тип.

**Пример за нарушение на LSP:**
Ако имаме клас Person и клас Student, но Student променя основното поведение на Person, тогава това ще наруши LSP.

**Решение:**
При създаване на нови класове, трябва да внимаваме наследените класове да разширяват функционалността, а не да я променят или премахват.

**4.Interface Segregation Principle (ISP)**

Клиентите не трябва да бъдат принуждавани да зависят от методи, които не използват. В Python, въпреки че нямаме официални интерфейси, можем да използваме **миксинообразни класове**, за да разделим различни поведения.

**Пример за нарушение на ISP:**

```
class Shape:
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError

class Rectangle(Shape):
    def draw_rectangle(self):
        # Логика за правоъгълник
        pass
    
    def draw_circle(self):
        pass  # Този метод не е нужен
```
Тук класът ```Rectangle``` има метод ```draw_circle```, който не му е нужен. Това нарушава ISP.

**Решение:**
Разделяме поведението в различни класове:

```
class Shape:
    def draw(self):
        raise NotImplementedError

class Rectangle(Shape):
    def draw(self):
        # Логика за рисуване на правоъгълник
        pass

class Circle(Shape):
    def draw(self):
        # Логика за рисуване на кръг
        pass
```

Сега всеки клас имплементира само методите, които са му необходими.

**5.Dependency Inversion Principle (DIP)**

Високо ниво модули не трябва да зависят от ниско ниво модули. И двата трябва да зависят от абстракции. Това ни помага да намалим зависимостите между различни компоненти.

**Пример за нарушение на DIP:**

```
class Email:
    def send_email(self):
        pass

class Notification:
    def __init__(self):
        self.email = Email()  # Пряка зависимост

    def send(self):
        self.email.send_email()
```
Тук ```Notification``` зависи директно от ```Email```, което прави класа труден за промяна или тестване.

**Решение:**
Използваме абстракции, за да премахнем директната зависимост:

```
class MessageService:
    def send_message(self):
        pass

class Email(MessageService):
    def send_message(self):
        # Логика за изпращане на имейл
        pass

class Notification:
    def __init__(self, service: MessageService):
        self.service = service

    def send(self):
        self.service.send_message()
```
Сега класът ```Notification``` зависи от абстракцията ```MessageService```, което ни позволява лесно да сменяме имейла с други услуги (SMS, push notifications и т.н.).

**Summary:**

Всички тези принципи имат за цел да направят кода по-гъвкав, лесен за поддръжка и по-малко податлив на грешки при промени.

![SOLID Principles](https://github.com/user-attachments/assets/68d37931-2ad8-4d25-a341-9410b5936eba)

---

## 08.Iterators and Generators

**What are Iterators?**

Итератор е обект, който позволява да преминаваш през елементите на колекция (като **list, tuple, string**) един по един. Той имплементира два специални метода.

- ```__iter__()```: Връща самия итератор.
- ```__next__()```: Връща следващата стойност от итератора. Ако няма повече елементи, връща ```StopIteration```.

**Пример:**

```
my_list = [4, 7, 0, 3]

# Получаване на итератор от списъка
my_iter = iter(my_list)

print(next(my_iter))  # 4
print(next(my_iter))  # 7
print(next(my_iter))  # 0
print(next(my_iter))  # 3
```
След като итераторът изчерпи елементите, опит за извличане на следващия елемент ще генерира грешка:

```
next(my_iter)  # Изхвърля StopIteration
```

**For Loops and Iterators**

For цикълът е имплементиран по следния начин:

```
iter_obj = iter(my_list)  # Получаване на итератора

while True:
    try:
        element = next(iterable)  # Получаване на следващия елемент
        print(element)
    except StopIteration:
        break  # Излизане от цикъла, когато няма повече елементи
```

**What are Generators?**

Генератор е по-прост начин за създаване на итератори. Вместо да създаваме клас и да дефинираме ```__iter__()``` и ```__next__()```, можем да използваме функция с ключовата дума ```yield```.

- Ключовата дума ```yield``` паузира функцията, като връща стойност, без да я приключва. При всяко следващо извикване на генератора, функцията продължава от мястото, където е била спряна, запазвайки състоянието си.

**Пример:**

```
def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_first_n = sum(first_n(5))
print(sum_first_n) # Извежда -> 10
```

Разлика между ```yield``` и ```return```:

- ```return``` спира функцията незабавно.
- ```yield``` паузира функцията и запазва състоянието й за следващото извикване на генератора.

**Generators vs Normal Functions**

- Генераторите са функции, които връщат множество резултати един по един, докато обикновените функции връщат една стойност и приключват.
- Когато генераторът достигне ```yield```, той се паузира. Локалните променливи се запомнят и изпълнението продължава при следващо извикване.

**Пример:**

```
def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

gen = my_gen()
next(gen)  # This is printed first, връща 1
next(gen)  # This is printed second, връща 2
next(gen)  # This is printed at last, връща 3
```

**Generator Expression**

Подобно на ```list comprehension```, ```generator expression``` тn позволява да създадем генератори в по-компактен вид.

```
my_list = [1, 3, 6, 10]

# Използване на list comprehension (създава целия списък в паметта)
print([x**2 for x in my_list])  # [1, 9, 36, 100]

# Използване на generator expression (генерира стойности една по една)
gen_expr = (x**2 for x in my_list)
print(next(gen_expr))  # 1
print(next(gen_expr))  # 9
```

**Summary**

- Итераторите са обекти, които позволяват да се преминава през елементите на колекция един по един.

- Генераторите са функции, които използват ```yield```, за да върнат множество стойности поетапно.

- Функции, които връщат итератори се наричат генератори.

- Generator expression са като List comprehension, но генерират елементи един по един, вместо да създават цялата колекция наведнъж.
