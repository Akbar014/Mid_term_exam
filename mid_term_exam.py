

class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no ) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        self.seats = {}
        self.show_list = []
        self.entry_hall(self)
        super().__init__()


    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

            
    def book_seats(self, show_id, seats_to_book):
        if show_id in self.seats:
            for row, col in seats_to_book:
                if 0 <= row < self.rows and 0 <= col < self.cols :
                    if self.seats[show_id][row][col] == 0:
                        self.seats[show_id][row][col] = 1
                        print(f"Seat ({row}, {col}) booked successfully for Show ID {show_id}.")
                    else:
                        print(f"Seat ({row}, {col}) is already booked for Show ID {show_id}.")
                else:
                    print(f"Seat ({row}, {col}) is invalid for Show ID {show_id}.")
        else:
            print(f"Show ID {show_id} not found.")


    def view_show_list(self):
        for i in self.show_list:
            print(i)


    def view_available_seats(self, show_id):
        if show_id in self.seats:
            print(f"Seat Matrix for Show ID: {show_id}")
            for row in self.seats[show_id]:
                print(row)
        else:
            print(f"Show ID {show_id} not found.")


hall1 = Hall(5, 3, 1)   

hall1.entry_show(111,'Try to be pure muslim', '11 pm')
hall1.entry_show(222,'Proud to be muslim', '11 pm')




attempt = True
while(attempt):

    print("1. View all show today")
    print("2. View available tickets")
    print("3. Book Tickets")
    print("4. Exit")
    action = int(input("Enter option : "))

    if action==1:
        hall1.view_show_list()
    elif action==2:
        show_id = int(input("Enter show id :  "))
        hall1.view_available_seats(show_id)
    elif action == 3:
        show_id = int(input("Enter show id :  "))
        seat_no = int(input("Enter seat number which you want to book :"))
        seats_to_book = []
        for i in range(seat_no):
            row = int(input("Enter row: "))
            col = int(input("Enter col:"))
            seats_to_book.append((row, col))
        hall1.book_seats(show_id, seats_to_book)
    else:
        attempt = False




