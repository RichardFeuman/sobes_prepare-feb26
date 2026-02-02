class MyCls:
    
    def __init__(self, power, health, hearth):
        self.power = power 
        self.health = health
        self.hearth = hearth
    
    def __getattribute__(self, name):
        if name == 'hearth':
            raise AttributeError('доступ к сердцу запрещен')
        else:
            super().__getattribute__(name)
        
    """def __getattr__(self, name):
        if name not in self.__dict__():
            return "Атрибут не найден"
    """        
    def __setattr__(self, item, value):
        if item not in ("hearth"):
            super().__setattr__(item, value)
        else:
            return "Нельзя изменить значение атрибута"
            
    def __delattr__(self, name):
        if name not in ("hearth"): 
            super().__delattr__(name)
        else:
            raise AttributeError('нельзя удалить')
            
            
            
cl = MyCls("power1", 95, "iron")

print(cl.hearth)
