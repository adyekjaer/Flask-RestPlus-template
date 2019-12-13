class Data():

    def __init__(self):

        self.my_string = 'all is well'

        self.cats = [
            {'id': 'felix', 'name': 'Felix'},
        ]

        self.dogs = [
            {'id': 'buddy', 'name': 'Buddy'},
        ]

    def hello_world(self, my_string):
        print(my_string, self.my_string)
