# Design Patterns

## What are design patterns ?
A design pattern is a model solution to a common design problem. It describes the problem and a general approach to solving it.

Each pattern describes a problem which occurs over and over again in our environment and then describes the core of the solution to the problem.

We need design patterns to ensure that our work is consistent, reliable and understandable. The idea is to make the code maintainable so that people who might be responsible for that piece of code in the future find it easy to fix and extend it once its creator is not around.

## Types of design patterns

Design patterns can be classified into following types:

* Creational: Responsible for object creation. eg. Factory, Builder, Singleton
* Structural: Helps in designing the relationships between objects. eg. Adapter, Facade, Composite
* Behavioral: Provide solutions regarding object interaction and responsibility. eg. Command, Observer, Strategy

## SOLID Design Principles

Paper by Robert C. Martin [Design Principles and Design Patterns](https://fi.ort.edu.uy/innovaportal/file/2032/1/design_principles.pdf)

### Single Resposibility Principle
Each class or module should have only a single resposibility or reason to change. This principle states that if we have 2 reasons to change for a class, we have to split the functionality in two classes. Each class will handle only one responsibility and if in the future we need to make one change we are going to make it in the class which handles it.
* [Reading](https://code.tutsplus.com/tutorials/solid-part-1-the-single-responsibility-principle--net-36074)
* Example:
	* [Good](https://github.com/dboyliao/SOLID/blob/master/python_code/good/single_responsibility.py)
	* [Bad](https://github.com/dboyliao/SOLID/blob/master/python_code/bad/single_responsibility.py)
	
### Open Closed Principle
Software entities like classes, modules and functions should be open for extension but closed for modifications. Abstraction is the key to OCP. By using these techniques to conform to the
OCP, we can create modules that are extensible, without being changed. This means
that, with a little forethought, we can add new features to existing code, without
changing the existing code and by only adding new code. 
* [Reading](https://code.tutsplus.com/tutorials/solid-part-2-the-openclosed-principle--net-36600)
* Example:
	* [Good](https://github.com/dboyliao/SOLID/blob/master/python_code/good/open_close.py)
	* [Bad](https://github.com/dboyliao/SOLID/blob/master/python_code/bad/open_close.py)
