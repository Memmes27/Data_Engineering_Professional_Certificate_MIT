# Import libraries
import threading
import time

# Create lists
titles = ["Harry Potter", "Pride and Prejudice"]
pages = ["250", "430"]
first_name = ["J.K", "Jane"]
last_name = ["Rowling", "Austen"]
location = ["UK", "UK"]

# Create function
def build_book_dict(titles, pages, first_name, last_name, locations):
    inputs = zip(titles, pages, first_name, last_name, locations)
    d = {}
    
    for t, p, f, l, loc in inputs:
        d[t] = {
            'Pages': int(p),
            'Author': {'First': f, 'Last': l},
            'Publisher': {'Location': loc}
        }
    
    time.sleep(3)
    return d

# Print dictionary to test function
print("Testing function:")
print(build_book_dict(titles, pages, first_name, last_name, location))

# Create timer
timer = threading.Timer(5.0, lambda: print("This will not be printed"))
timer.start()
print("\nTimer started...")

# Cancel timer
timer.cancel()
print("Timer Cancelled")