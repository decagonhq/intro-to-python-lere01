## Introduction to Python

Github Classroom Assignment Link : https://classroom.github.com/a/oUE_Og9m

Tasks Definition : https://docs.google.com/document/d/1V1gYEKLtOPYzZL7F9koaDVdgIlOXl_ALspjyzOZJN7Q/edit?usp=sharing

## Understanding SOLID Principles

SOLID is an acronym for five principles proposed by Robert C. Martin popularly known as Uncle Bob, to guide Object Oriented Design. The goal is for programmers to be able to develop softwares that are easy to maintain and extend as well as avoid code smells and refactor codes easily. These principles also form a core philosophy of operation among AGILE Teams. The five principles are:

- Single Responsibility Principle (S. R. P)
  A common way of putting this principle is that a class should should have one and only one reason to change. In other words, a class should have only one responsibility or job. The logic behind this is that the more responsibilities a class has, the more likely it will receive requests to change and this makes it difficult to maintain such class. Note that a change in responsibility of a class leads to change in other responsibilities of the class. As illustration, think of a system that is built to bring members of a community together. It is best that if that system has a social media integration, it should be separated from other functions in the system. Another illustration is that of an area_calculator. This is a program that calculates the area of different objects depending on their shapes. S.R.P demands that this program should not be concerned with other things such as the output of the result. If we want the user to be able to get the result in different formats, then that responsibility should be delegated to another program.

- Open-Closed Principle
  As Uncle Bob said, 'this principle is the foundation for building maintainable and reusable code'. This principle demands that one should be able to extend a class' behaviour without modifying it. In essence, a class is open to extension and closed to modification. As requirements change, the class should be able to change its behaviour to meet the new requirements while the source code of the class remains set in stone. This is made possible using abstraction. For example, say we have a system that makes use of different shapes, we would want to have difference classes e.g. Circle, Rectangle etc. But, we would have to introduce an abstraction in the form of a Shapes class. Hence, the system does not depend directly on the individual shape classes. It depends interacts with an instance of Shapes which acts as an interface. This way, we can always add new classes of shapes to the interface without altering the source code of the dependent system. Let us consider the program which calulates the area of objects depending on their shapes. It would become burdensome if eveytime we have to cater for the area of a new shape, we have to modify the source code to able to calculate a new area. It is easier and better to include the area method as part of the different shape classes so that the program only calls this method for each shape. But it is even better to have an interface that defines the methods that every shape class must implement. This way, the program that calculates the area of the objects only depends on the interface to get the shape attributes and methods.

- Liskov Substitution Principle
  In the words of Babara Liskov, 'Derived classes must be substitutable for their base classes'. This principle guides on deciding what should be a class and what should be an interface. To put it another way, classes should not just extend classes without guide. Uncle BOb suggests that we should design by contract. That is, each method should have preconditions and postconditions defined. The preconditions must hold true for a method to execute and the postconditions must hold true after the method executes. It is recommended that precondition be replaced by a weaker one, and postcondition by a stronger one. For example, if a base class requires a member to be an integer and a subtype requires that member to be a positive integer, the precondition is replaced by a strengthened one and any code that was working perfectly fine with negative integers, gets broken. On another hand, if the base class has guaranted that a member would remain positive after being called and then the sub type changes the behaviour to allow negative integers, code that makes use of the method assuming that the integer would remain positive now breaks. In summary, if S is a subtype of T, then objects of type T may be replaced with objects of type S (i.e. an object of type T may be substituted with any object of a subtype S) without altering any of the desirable properties of the program (correctness, task performed, etc.)

- Interface Segregation Principle
  This principle suggests that it is better to have multiple client-specific interfaces than to have one general interface. For example to have an Animal interface which has eat, sleep and walk methods would not be a perfect abstraction because some animals can fly. It would be better to break the Animal interface into CanEat, CanSleep and CanWalk interface. Also, borrowing from our Shapes Interface example, it would become complicated when we need the interface to be able to calculate volume in addition to area. This is a requirement that cannot be met for squares but can be met for cubes. In this case, it would be better to have different interfaces like SolidShapesInterface which would have volume and area methods and 2DShapesInterface which would have just area methods.

- Dependency Inversion Principle
  This principle demands that high level module and low level module depend on abstractions. It removes the need for direct interaction betwwen low level and high level modules.

Reference

1. Dhurim Kelmendi. 2017. SOLID Principles made easy. Hackernoon. Accessed on Wednesday, 08 January, 2020 at https://hackernoon.com/solid-principles-made-easy-67b1246bcdf

2. Samuel Oloruntoba. 2015. S.O.L.I.D: The First 5 Principles of Object Oriented Design. Scotch. Accessed on Wednesday, 08 January, 2020 at https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design

3. Liskov Substitution Principle. Wikipedia

## Data Types Categorization

| Mutable | Immutable |
| ------- | --------- |
| list    | bool      |
| set     | int       |
| dict    | float     |
|         | str       |
|         | frozenset |
