
# Object oriented programming

In this course, we'll be discovering how Python deals with OOP.

We'll be building a ```class```, step by step, to introduce some of the more crucials OO paradigms.

At the end of this course, you will have aquired the following concepts:

- the special ```__init__()``` method which one can see as a constructor in other OO languages
- difference between class and instance properties
- class methods
- use of the ```@property``` and ```@property.setter``` decorators to introduce C++ getters et setters
- inheritance, ```abstract classes``` and ```abstract methods```

> See also [python.org](https://docs.python.org/3/tutorial/classes.html) ```class``` tutorial.

## Classes

> Classes provide a means of bundling data and functionality together.

A class is a new type of object which can contain:

- data / properties / attributes (Python variables)
- functionality / methods (Python functions)

Once declared, one can then create new instances of this class like with native types.

### A simple class

Let's create the simplest possible class to start coding around airpcrafts, and then add feature to demonstrate object programming concepts:

```python
# Declaration of our new class
class Aircraft:
    """This new type will be used to model any sort of airplanes"""
```

Now, let's use this new class by creating a new my_plane variable of type Aircraft:

```python
# Instanciation of our new class
my_plane = Aircraft()
```

Let's create 3 planes and assign them some specific properties:

```python
# My first plane
my_a320 = Aircraft()
my_a320.model_name = 'A320'
my_a320.is_military = False
my_a320.is_cargo = False

# I need a second plane in my program
another_plane = Aircraft()
another_plane.model_name = 'A400M'
another_plane.is_military = True
another_plane.is_cargo = False

# and a last one
my_cargo = Aircraft()
my_cargo.model_name = 'C295'
my_cargo.is_military = True
my_cargo.is_cargo = True
```

### Constructors

It is possible to customize the creation of your class by overriding the special ```__init__()``` method.

The ```__init__()``` method (a.k.a. constructor in some other OO languages) is being called automatically by Python when an instance is created.

That, as a class implementer, gives you a chance to eventually pass some parameters or further customize the creation.

- Notice the use of default parameter's values in the below example.
- The ```self``` variable is like ```this``` in java or C++, it simply means 'this instance'

```python
class SimpleAircraft:
    def __init__(self,
                 model_name: str,
                 is_military: bool = False,
                 is_cargo: bool = False):
        self.model_name = model_name
        self.is_military = is_military
        self.is_cargo = is_cargo
```

Now the same 3 planes as earlier, but with the new syntaxical sugar:

The use of named parameters can be helpful:

- to be more explicit when lot of complex parameters are to be passed in
- when you want to rely on default values for most parameters and only pass some overrides (see ```a350``` example beneath)

```python
my_a320 = SimpleAircraft('A320')
another_plane = SimpleAircraft('A400', True)
my_cargo = SimpleAircraft('C295', is_military=True, is_cargo=True)
# in this case, we're happy with 'is_military' having the default value of False, no need to specify it
a350 = SimpleAircraft('A350F', is_cargo=True)
```

### Class methods

classes can (and most probably should...) also contain methods (functions) that can change the state of your internal variables.

In the below example, we'll append a ```convert()``` method that'll change the cabin layout of our ```SimpleAircraft```.

But, in the real world, not all models can support such a transformation, we also want to implement this logic, for that we'll need an additional ```is_convertible``` variable.

The current cabin layout / state is stored in ```is_cargo```.

Because only two layouts are supported (cargo or passengers), a boolean is plainly sufficient to code the layout.

```python
class SimpleAircraft:
    def __init__(self,
                 model_name: str,
                 is_military: bool = False,
                 is_cargo: bool = False,
                 is_convertible: bool = False):
        if not model_name:
            raise ValueError('Error: You must supply a non empty model name')
        self.model_name = model_name
        self.is_military = is_military
        self.is_cargo = is_cargo
        self.is_convertible = is_convertible

    def convert(self, to_cargo: bool = None) -> str:
        """
        Modifies the cabin layout (if the model supports it) so that it can accommodate to either:
          - freight 
          - or passengers
        If the cabin layout cannot be changed on this model a ValueError exception will be thrown.

        :param to_cargo: Optional, boolean
            if specified and set to True, the new cabin layout will be set to cargo, or passengers if set to False.
            If not set, the actual cabin configuration (whose state is reflected by the is_cargo boolean) will be inverted

        :return: a string whose value represents the new cabin configuration (possible values are 'cargo' or 'passengers')
        """
        if self.is_convertible:
            if to_cargo is None:
                self.is_cargo = not self.is_cargo
            else:
                self.is_cargo = to_cargo
            return 'cargo' if self.is_cargo else 'passengers'
        else:
            raise ValueError(f'Sorry, {self.model_name} is not convertible from / to cargo')
```

The A400M is such a aircraft that can accomodate both passengers and freight, let's implement that in code:

```python
# As we haven't explicitly set the is_cargo,
# our a400m.is_cargo will have the default value of False as specified in the constructor's parameters
a400m = SimpleAircraft('A400M',  is_military=True, is_convertible=True)
print(f'cabin layout is in cargo mode: {a400m.is_cargo}')
new_layout = a400m.convert()
print(f'cabin layout is {new_layout}')
new_layout = a400m.convert(to_cargo=True)
print(f'cabin layout is {new_layout}')
new_layout = a400m.convert(to_cargo=False)
print(f'cabin layout is {new_layout}')
```

Result:

```csv
cabin layout is in cargo mode: False
cabin layout is cargo
cabin layout is cargo
cabin layout is passengers
```

### Data members (properties / variables)

> class variables are shared by all instances whilst instances variables as tied to a specific instance.

In the below example:

- the ```_models_list``` is a class variable whose value is shared accross all instances, it'll contain the list of all our planes's ID
- the ```_model_name``` an instance variable whose value can be different for each instance we'll be creating
- notice the use of the ```_``` (single underscore) prefix, this is the Python convention to tell this is a private instance / class variable:
- notice the use of the ```__``` (double underscores) prefix, this is the Python convention to tell this is a protected instance / class variable:
- to distinguish class from instance variables we're using the ```self``` variable to prefix instance variables
- the use of getter (```@property```) and setter as optional as instance variables can be accessed directly, but it provides you with more control.
- the ```all_family``` property is read-only and because a ```list``` in Python is mutable, we purposedly return a shallow copy of our internal list to be sure nobody can modify our list from the outside world!

The below ```A32xFamily``` can be used to modelize a family of planes that are variations of the A320 but in a longer or shorter bodies.

```python
class A32xFamily:
    _models_list: list[str] = []

    def __init__(self, model_name: str, registration_id: str):
        self._registration_id = registration_id
        self._model_name = model_name
        # Well you don't want duplicates, do you?
        if model_name not in A32xFamily._models_list:
            A32xFamily._models_list.append(model_name)

    @property
    def all_family(self) -> list[str]:
        # returs a copy of our internal list to prevent outside code to change it
        return list(A32xFamily._models_list)

    @property
    def details(self) -> str:
        return f"I'm an {self._model_name} registered under id {self._registration_id}"

    @property
    def registration_id(self) -> str:
        return self._registration_id

    @registration_id.setter
    def registration_id(self, new_id: str) -> None:
        self._registration_id = new_id
```

Ok, let's now play a bit with this class to see the difference between the class and instance variables:

```python
plane1 = A32xFamily('A319', '5084Q')
print(plane1.details)
print('plane1.all_family', plane1.all_family)

plane2 = A32xFamily('A320', '1086J')
print(plane2.details)
print('plane2.all_family', plane2.all_family)

plane3 = A32xFamily('A320', '3056K')
print(plane3.details)
print('plane3.details before retail', plane3.details)
# let's imagine we retail this plane and thus need to get a new registration ID in another country
plane3.registration_id = '1234A'
print('plane3.all_family', plane3.all_family)
print('plane3.details after retail', plane3.details)
print(plane3.registration_id)

plane4 = A32xFamily('A321', '2037S')
print(plane4.details)
print('plane1.all_family', plane1.all_family)
print('plane2.all_family', plane2.all_family)
print('plane3.all_family', plane3.all_family)
print('plane4.all_family', plane4.all_family)
```

Output:

```csv
I'm an A319 registered under id 5084Q
plane1.all_family ['A319']
I'm an A320 registered under id 1086J
plane2.all_family ['A319', 'A320']
I'm an A320 registered under id 3056K
plane3.details before retail I'm an A320 registered under id 3056K
plane3.all_family ['A319', 'A320']
plane3.details after retail I'm an A320 registered under id 1234A
1234A
I'm an A321 registered under id 2037S
plane1.all_family ['A319', 'A320', 'A321']
plane2.all_family ['A319', 'A320', 'A321']
plane3.all_family ['A319', 'A320', 'A321']
plane4.all_family ['A319', 'A320', 'A321']
```

## Inheritance

Classes can be inherited / derived (specialized) so that child classes benefit from parent's properties and methods.

Derived classes may override (specialize) methods of their base classes

Python has two built-in functions that work with inheritance:

- Use ```isinstance()``` to check an instance’s type: ```isinstance(obj, int)``` will be True only if ```obj.__class__``` is int or some class derived from int.
- Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.
- An abstract class (inherits from ```ABC```) means it can not be instanciated, but usually acts as a common ancestor for normal inherited classes.

The syntax for a derived class definition looks like this:

```python
class AircraftBase(ABC):
    """A machine or device, such as an airplane, helicopter, glider, or dirigible, capable of atmospheric flight."""

    def __init__(self, model_name: str, registration_id: str):
        self._registration_id = registration_id
        self._model_name = model_name

    @abstractmethod
    def refuel(self) -> int:
        """
        Fill the tank
        :return: the quantity delivered
        """
        ...

    @property
    def registration_id(self) -> str:
        return self._registration_id

    @property
    def model_name(self) -> str:
        return self._model_name


class Helicopter(AircraftBase):
    """Any kind of helicotpers"""

    def __init__(self, model_name: str, registration_id: str, rotor_power: int, stator_power: int):
        super().__init__(model_name=model_name, registration_id=registration_id)
        self.rotor_power = rotor_power
        self.stator_power = stator_power

    def refuel(self) -> int:
        """
        Fill the helicopter's tank (overridden)
        :return: the quantity delivered
        """
        print(f'refueling (adapted for helicopter) {type(self).__name__} type {self._model_name} registered under {self._registration_id}')
        return 177


class AirplaneBase(AircraftBase, ABC):
    """Any kind of planes"""
    def __init__(self, model_name: str, registration_id: str, wing_size: int, is_cargo: bool = False):
        super().__init__(model_name=model_name, registration_id=registration_id)
        self.wing_size = wing_size
        self.is_cargo = is_cargo

    def refuel(self) -> int:
        """
        Fill the helicopter's tank (overridden)
        :return: the quantity delivered
        """
        print(f'refueling (overridden for aiplanes) {type(self).__name__} type {self._model_name} registered under {self._registration_id}')
        return 1023


class TurboProp(AirplaneBase):
    """A turbojet engine used to drive an external propeller."""
    def __init__(self, model_name: str, registration_id: str, propeller_size: int, wing_size: int, is_cargo: bool = False):
        super().__init__(model_name=model_name, registration_id=registration_id, wing_size=wing_size, is_cargo=is_cargo)
        self.propeller_size = propeller_size


class Jet(AirplaneBase):
    """an aircraft that uses airbreathing jet engines, which take in air, burn fuel with it in a combustion chamber"""
    def __init__(self, model_name: str, registration_id: str, engine_brand: str, wing_size: int, is_cargo: bool = False):
        super().__init__(model_name=model_name, registration_id=registration_id, wing_size=wing_size, is_cargo=is_cargo)
        self.engine_brand = engine_brand


class Glider(AirplaneBase):
    """ heavier-than-air aircraft that do not employ propulsion once airborne"""
    def init(self, model_name: str, registration_id: str, wing_size: int):
        super().__init__(model_name=model_name, registration_id=registration_id, wing_size=wing_size)

    def refuel(self) -> int:
        raise(NotImplemented('One cannot refuel a glider because it has no engine!'))
```

Creating some instances of this hierarchy:

```python
my_helicopter = Helicopter(model_name='H175', registration_id='1234A', rotor_power=175, stator_power=1234)
my_jet = Jet(model_name='A220', registration_id='3456H', wing_size=45,  engine_brand='rolls')
my_turbo_prop = TurboProp(model_name='A400M', registration_id='9876Q', wing_size=65, propeller_size=254)
print(f'Total delivered liters: {my_helicopter.refuel()}')
print(f'Total delivered liters: {my_jet.refuel()}')
print(f'Total delivered liters: {my_turbo_prop.refuel()}')
```

Results:

```csv
refueling (adapted for helicopter) Helicopter type H175 registered under 1234A
Total delivered liters: 177
refueling (overridden for aiplanes) Jet type A220 registered under 3456H
Total delivered liters: 1023
refueling (overridden for aiplanes) TurboProp type A400M registered under 9876Q
Total delivered liters: 1023
```