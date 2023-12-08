# Single Responsibility Principle
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
        return '\n'.join(self.entries)
    
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, url):
    #     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

if __name__ == '__main__':
    j = Journal()
    j.add_entry('Book1')
    j.add_entry('Book2')
    j.add_entry('Book3')
    j.add_entry('Book4')
    print(j)

    file = r'./journal.txt'
    PersistenceManager.save_to_file(j, file)

    print(f'Reading from {file}')
    with open(file, 'r') as fh:
        print(fh.read())

    