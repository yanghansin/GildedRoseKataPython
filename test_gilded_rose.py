# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual("fixme", items[0].name)

    # Lab4 Started
    def test_quality_is_never_negative(self):
        items = [Item(name="Normal Item", sell_in=5, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_quality_degrades_twice_as_fast_after_sell_by_date(self):
        items = [Item(name="Normal Item", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)

    # Lab4 Ended


if __name__ == '__main__':
    unittest.main()
