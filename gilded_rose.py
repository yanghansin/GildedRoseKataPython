# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# Lab5 Started
class ItemStrategy:
    def update(self, item: Item):
        pass


class NormalItemStrategy(ItemStrategy):
    def update(self, item: Item):
        item.quality = min(50, item.quality)
        item.sell_in -= 1
        if item.sell_in < 0:
            degrade = 2
        else:
            degrade = 1
        item.quality = max(0, item.quality - degrade)

class AgedBrieStrategy(ItemStrategy):
    def update(self, item: Item):
        item.sell_in -= 1
        if item.sell_in < 0:
            increase = 2
        else:
            increase = 1
        item.quality = min(50, item.quality + increase)  # Ensure quality doesn't exceed 50

class SulfurasStrategy(ItemStrategy):
    def update(self, item: Item):
        pass

class BackstagePassStrategy(ItemStrategy):
    def update(self, item: Item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)

class ConjuredItemStrategy(ItemStrategy):
    def update(self, item: Item):
        item.sell_in -= 1
        if item.sell_in < 0:
            degrade = 4
        else:
            degrade = 2
        item.quality = max(0, item.quality - degrade)


class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Conjured Mana Cake": ConjuredItemStrategy()
        }

    def update_quality(self):
        for item in self.items:
            strategy = self.strategies.get(item.name, NormalItemStrategy())
            strategy.update(item)

# Lab5 Ended