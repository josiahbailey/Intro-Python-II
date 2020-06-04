# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def check_room(self, dire):
        if dire == 'n':
            if hasattr(self, 'n_to'):
                return self.n_to
        elif dire == 's':
            if hasattr(self, 's_to'):
                return self.s_to
        elif dire == 'e':
            if hasattr(self, 'e_to'):
                return self.e_to
        elif dire == 'w':
            if hasattr(self, 'w_to'):
                return self.w_to
        elif dire == 'q':
            return 'Quit'
        else:
            return None

            # def north(self):
            #     if self.n_to:
            #         return self.n_to
            #     else:
            #         return False

            # def south(self):
            #     if self.s_to:
            #         return self.s_to
            #     else:
            #         return False

            # def east(self):
            #     if self.e_to:
            #         return self.e_to
            #     else:
            #         return False

            # def west(self):
            #     if self.w_to:
            #         return self.w_to
            #     else:
            #         return False
