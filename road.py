class Road:
    __available_attributes = ('width', 'number_of_lanes', 'material', 'color', 'length')
    __not_deletable = ('width',)

    def __init__(self, color: str):
        self.length = 500
        self.color = color
        # self.color = 'Green'

    # def __repr__(self):
    #     return 'Hello world'

    def __str__(self):
        return f'{self.__class__.__name__}\n{{\n\tlength: {self.length}\n}}'

    def __setattr__(self, key, value):
        if key not in self.__available_attributes:
            raise Exception(f'{key} is not supported supported values are: {self.__available_attributes}')
        return super().__setattr__(key, value)

    def __getattr__(self, item):
        return None

    def __getattribute__(self, item):
        if item.startswith('_Road__'):
            raise Exception('No no no')
        return super().__getattribute__(item)

    def __bool__(self):
        return False

    def __delattr__(self, item):
        if item in self.__not_deletable:
            print(f'{item} is not deletable')

    # def __dir__(self):
    #     print(super().__dir__())


if __name__ == '__main__':
    road = Road('Green')
    # if road.bla:
    #     print('Perform some actions')
    #     road.color = 'Black'
    #     print(road.color)
    # else:
    #     print('Other scenario')
