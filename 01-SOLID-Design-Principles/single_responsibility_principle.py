# SRP (Single Responsibility Principle) aka SOC (Seperation of Concern)

# Anti-pattern: God Object (Single object with all the responsibilities)

class Journal:
    
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
        
    def add_entry(self, text: str) -> None:
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
        
    def remove_entry(self, pos: int) -> None:
        del self.entries[pos]
        
    def __str__(self) -> str:
        return '\n'.join(self.entries)
    
    """
    Below code violates the SRP priciple as we are adding
    persistence responsibility to the class. So instead of 
    adding persistence features it's better to create new class.
    """ 
    # def save(self, filename: str) -> None:
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
        
    # def load(self, filename: str) -> None:
    #     pass
    
    # def load_from_web(self, uri: str) -> None:
    #     pass
    
class PersistenceManager:
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def save_to_file(journal: Journal, filename: str) -> None:
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()
    