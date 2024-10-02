# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    # Lab4 Started
    def test_quality_is_never_negative(self):
        items = [
            Item(name="Normal Item", sell_in=5, quality= -10),
            Item(name="Aged Brie", sell_in=2, quality= -100),
            Item(name="Elixir of the Mongoose", sell_in=5, quality= -7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality= -80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15,
                 quality= -20),
        ]
        gilded_rose = GildedRose(items)

        for _ in range(10):
            gilded_rose.update_quality()

        for item in items:
            with self.subTest(item=item.name):
                self.assertGreaterEqual(item.quality, 0,
                                        f"{item.name} has negative quality!")

    def test_quality_degrades_twice_as_fast_after_sell_by_date(self):
        items = [
            Item(name="Aged Brie", sell_in=1, quality=10),
            Item(name="Elixir of the Mongoose", sell_in=0, quality=6)
        ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11,
                         "Quality should degrade by 1 before sell by date")
        self.assertEqual(items[1].quality, 4,
                         "Quality should degrade by 2 after sell by date")

    def test_vest_item_with_wrong_quality_type(self):
        items = [
            Item("vest", "aa", "aa")
        ]

        gilded_rose  = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, None)

    def test_conjured_items_degrade_twice_as_fast(self):
        items = [
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),
        ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4,
                         "Conjured items should degrade by 2 before sell-by date")

    # Lab4 Ended


if __name__ == '__main__':
    unittest.main()
