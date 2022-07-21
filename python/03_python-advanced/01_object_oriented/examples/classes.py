class Aircraft:
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
        Modifies the cabin layout so that is can accommodate to either freight or passengers if the model supports it.
        If the cabin layout cannot be changed on this model a ValueError exception will be thrown.
        :param to_cargo:
            Optional, boolean, if specified and set to True, the new cabin layout will be set to cargo, or passengers if set to False.
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


# As we haven't explicitly set the is_cargo,
# our a400m.is_cargo will have the default value of False as specified in the constructor's parameters
a400m = Aircraft('A400M',  is_military=True, is_convertible=True)
print(f'cabin layout is in cargo mode: {a400m.is_cargo}')
new_layout = a400m.convert()
print(f'cabin layout is {new_layout}')
new_layout = a400m.convert(to_cargo=True)
print(f'cabin layout is {new_layout}')
new_layout = a400m.convert(to_cargo=False)
print(f'cabin layout is {new_layout}')


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


class Aircraft:
    """A machine or device, such as an airplane, helicopter, glider, or dirigible, capable of atmospheric flight."""

    def __init__(self, model_name: str, registration_id: str):
        self._registration_id = registration_id
        self._model_name = model_name


class Helicopter(Aircraft):
    """Any kind of helicotpers"""

    def __init__(self, model_name: str, registration_id: str, rotor_power: int, stator_power: int):
        super().__init__(model_name=model_name, registration_id=registration_id)
        self.rotor_power = rotor_power
        self.stator_power = stator_power


class Airplane(Aircraft):
    """Any kind of planes"""
    def __init__(self, model_name: str, registration_id: str, wing_size: int, is_cargo: bool = False):
        super().__init__(model_name=model_name, registration_id=registration_id)
        self.wing_size = wing_size
        self.is_cargo = is_cargo


class TurboProp(Airplane):
    """A turbojet engine used to drive an external propeller."""
    def __init__(self, model_name: str, registration_id: str, propeller_size: int):
        super().__init__(model_name=model_name, registration_id=registration_id)
        self.propeller_size = propeller_size


class Jet(Airplane):
    """an aircraft that uses airbreathing jet engines, which take in air, burn fuel with it in a combustion chamber"""
    def __init__(self, model_name: str, registration_id: str, engine_brand: str):
        super().__init__(model_name=model_name, registration_id=registration_id)
        self.engine_brand = engine_brand


class Glider(Airplane):
    """ heavier-than-air aircraft that do not employ propulsion once airborne"""
    ...