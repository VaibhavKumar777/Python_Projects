import random
import string
class Robot:
    used_names = set()
    def __init__(self):
        self._name = None
    @property
    def name(self):
        if self._name is None:
            self._name = self._generate_unique_name()
        return self._name
    def reset(self):
        self._name = None
    @classmethod
    def _generate_unique_name(cls):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            digits = ''.join(random.choices(string.digits, k=3))
            name = letters + digits
            if name not in cls.used_names:
                cls.used_names.add(name)
                return name
        
        
