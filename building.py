class Building:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__stages = dict()

    def __len__(self):
        return len(self.__stages)

    def __setitem__(self, key, value):
        self.__stages[key] = value

    def __getitem__(self, item):
        return self.__stages[item]

    def print_stage(self):
        print(self.__stages)


building = Building('a', 'b')

building['new_key'] = 'Something'
# print(building['new_key'])

building.print_stage()
