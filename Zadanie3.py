import unittest

class WriteLinesSongTest(unittest.TestCase):

    def test_first_line(self):
        self.assertEqual(lines(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_ninth_line(self):
        self.assertEqual(lines(9), """On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.""")
    
    def test_all_lines(self):
        self.assertEqual(lines(all), """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.""")
    
    def test_lines_from_one_to_three(self):
        self.assertEqual(lines((1,3)),"""On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.""")

     def test_lines_from_one_to_nine(self):
        self.assertEqual(lines(9), """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.""")

    def test_lines_from_six_to_seven(self):
        self.assertEqual(lines((6,7)), """On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.""")

    def test_lines_from_five_to_fife(self):
        self.assertEqual(lines((5,5)), """On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.""")
   

   #Exceptions
    def test_exception_wrong_number(self):
        with self.assertRaises(Exception):
           lines(53)

    def test_exception_zero_as_parameter(self):
        with self.assertRaises(Exception):
            lines(0)
    
    def test_exception_negative_number(self):
        with self.assertRaises(Exception):
           lines(-3)

    def test_exception_float_number(self):
        with self.assertRaises(Exception):
            lines(1.4)
    
    def test_exception_bad_tuple_interval1(self):
        with self.assertRaises(Exception):
            lines((1,42))

    def test_exception_bad_tuple_interval2(self):
        with self.assertRaises(Exception):
            lines((91,3))

    def test_exception_bad_tuple_interval3(self):
        with self.assertRaises(Exception):
            lines((3,1))

    def test_exception_bad_tuple_interval4(self):
        with self.assertRaises(Exception):
            lines((-5,1))

    def test_exception_bad_tuple_interval5(self):
        with self.assertRaises(Exception):
            lines((5,-1))

    def test_exception_bad_string(self):
        with self.assertRaises(Exception):
            lines("string")

    def test_exception_no_parameter(self):
        with self.assertRaises(Exception):
            lines()

    def test_exception_empty_string(self):
        with self.assertRaises(Exception):
            lines("")

    def test_exception_empty_tuple(self):
        with self.assertRaises(Exception):
            lines(())

    def test_exception_list(self):
        with self.assertRaises(Exception):
            lines([])

    def test_exception_dictionary(self):
        with self.assertRaises(Exception):
            lines({})
    
    def test_exception_tuple_with_dictionary_and_list(self):
        with self.assertRaises(Exception):
            lines(([],{}))

    def test_exception_tuple_with_string_and_int(self):
        with self.assertRaises(Exception):
            lines(("",4))
