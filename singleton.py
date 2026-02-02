class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value=None):
        self.value = value
        
        

s1 = Singleton(1)
s2 = Singleton(1)
print(id(s1), id(s2))
