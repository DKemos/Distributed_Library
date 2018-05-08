from __future__ import print_function
import Pyro4

@Pyro4.expose
class Warehouse(object):
    def __init__(self):
        self.contents = []

    # FUNCTION FOR RETURNING THE BOOKS IN THE LIBBRARY
    def list_contents(self):
        return self.contents

    # FUNCTION FOR STORING A BOOK IN THE LIBRARY AND RETURN ITS UNIQUE ID
    def store(self, book):
        self.contents.append(book)
        return book[0]


    def clear(self):
        self.contents.clear()


    def just_store(self,book):
        self.contents.append(book)

def main():
    warehouse = Warehouse()
    Pyro4.Daemon.serveSimple(
        {
            warehouse: "example.warehouse"
        },
        ns=True)

if __name__ == "__main__":
    main()
