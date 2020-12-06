def seat_id(row, col):
    return row * 8 + col

def traverse_row(seat, row=[0, 127]):
    seat = seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    row = int(seat[:7], 2)
    col = int(seat[7:], 2)

    return seat_id(row, col)

def main():
    seats = [seat.strip("\r\n") for seat in open('input5.txt', 'r').readlines()]
    results = sorted([traverse_row(seat) for seat in seats])
    for i in results:
        if results[i+1] != results[i]+1:
            seat = results[i+1]-1
            break

    print("Seat #: %d" % seat)
    print("Highest seat ID: %d" % max(results))

if __name__ == '__main__':
    main()
