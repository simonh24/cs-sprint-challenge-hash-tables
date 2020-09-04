#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticks = {}
    route = []
    for ticket in tickets:
        ticks[ticket.source] = ticket.destination
    current = ticks['NONE']
    while not current == "NONE":
        route.append(current)
        current = ticks[current]
    route.append(current)
    return route
