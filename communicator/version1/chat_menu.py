class ChatMenu():
    def choice(self):
        while 1:
            try:
                self.choice = int(input("press 1 to start\npress 2 to stop\n:>"))
            except ValueError as err:
                print("This is not int, ERROR: {}.".format(err))
            except (KeyboardInterrupt, SystemExit):
                raise
            if self.choice not in range(1, 3):
                print("not in range 1 - 2")
            elif self.choice == 2:
                print("Exiting")
                return self.choice
                break
            else:
                return self.choice

