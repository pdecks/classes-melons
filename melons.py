"""melons.py -- This file should have our melon-type classes in it."""
class MelonOrder(object):

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5

        if self.species == "Casaba" or self.species == "Ogen":
            price = price + 1
        
        if self.imported == True:
            price = price * 1.5
        
        if self.shape == 'square':
            price = 2 * price
        
        if self.species == "Watermelon" and qty > 2:
            price = 0.75 * price

        if self.species == "Cantaloupe" and qty > 4:
            price = 0.5 * price    

        total = qty * price

        return total


class WatermelonOrder(MelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']




class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

   
class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer',"Fall","Winter"]


class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']


class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter','Spring']


class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']


class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']


class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']


class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Summer',"Spring"]

