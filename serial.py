"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Making a new generator with a start defaulting at 0"""
        self.start = self.next = start

    def __repr__(self):
        """making it easier to read/ showing the current status"""
        return f"start = {self.start} | next = {self.next}"
    

    def generate(self):
        """ Increment self.next and return what comes before it"""
        self.next +=1
        return self.next - 1

    def reset(self):
        """Reset to original start number"""
        self.next = self.start



