import abc
"""
Abstract stripe object
Root class for all stripes

@author: oleksii.slavik
"""


class Stripe:

    @abc.abstractmethod
    def removeStripe(self, surface):
        pass

    def __repr__(self):
        return str(self.__dict__)
