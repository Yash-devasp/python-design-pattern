# Design Pattern
#SRP SOC - Single Responsibility Code Or Seperation Of Concern

# It prevents the anti pattern of GOD objects which is an object that has all the functionalities

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)
    
    # This is a secondary responsibility of persistance that can be used by other functionalities

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass
    
class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
            file = open(filename, 'w')
            file.write(str(journal))
            file.close()

j = Journal()
j.add_entry("I went to office today.")
j.add_entry("I ate sandwich today.")
print(f'Journal entries:\n{j}')

file = r'/Users/yashgoswami/Documents/py_tuts/design_patterns/journal.txt'
PersistanceManager.save_to_file(j,file)

with open(file) as fh:
     print(fh.read())