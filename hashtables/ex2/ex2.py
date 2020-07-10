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

    # initialize route list with the length that is passed in
    route = [None] * length

    # initialize dictionary to hold the tickets for lookup
    ticket_lookup = {}

    # loop through each ticket and store the destination as a value to the source key
    for ticket in tickets:
        ticket_lookup[ticket.source] = ticket.destination

    # first ticket has a source of "NONE" -- start there
    destination = "NONE"

    # look up each ticket's next destination and add it to the route
    for leg in range(length):
        # get ticket destination
        destination = ticket_lookup[destination]

        # add destination to trip 
        route[leg] = destination


    return route
