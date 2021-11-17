import unittest

class Song:
    def lines(self, howMany):
        song = """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
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
On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""
        if type(howMany) is int:
            if howMany>0 and howMany<=12:
                songList = song.split("\n")
                return songList[howMany-1]
            else:
                raise Exception("Bad number")
        
        elif howMany == "all":
            return song

        elif type(howMany) is tuple:
            if howMany[0] <= howMany[1] and howMany[0]>0 and howMany[0]<=12 and howMany[1]>0 and howMany[1]<=12:
                songList = song.split("\n")
                return "\n".join(songList[howMany[0]-1:howMany[1]])
            else:
                raise Exception("Bad tuple interval")

        else:
            raise Exception("Bad data type")


lines = Song().lines

class WriteLinesSongTest(unittest.TestCase):

    def test_first_line(self):
        self.assertEqual(lines(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_ninth_line(self):
        self.assertEqual(lines(9), """On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.""")

    def test_last_line(self):
        self.assertEqual(lines(12), "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_all_lines(self):
        self.assertEqual(lines("all"), """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
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
        self.assertEqual(lines((1,9)), """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
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

    @unittest.skip("not done yet")
    def test_exception_bad_string(self):
        with self.assertRaises(Exception):
            lines("string")

    @unittest.skip("not done yet")
    def test_exception_no_parameter(self):
        with self.assertRaises(Exception):
            lines()

    @unittest.skip("not done yet")
    def test_exception_empty_string(self):
        with self.assertRaises(Exception):
            lines("")

    @unittest.skip("not done yet")
    def test_exception_empty_tuple(self):
        with self.assertRaises(Exception):
            lines(())

    @unittest.skip("not done yet")
    def test_exception_list(self):
        with self.assertRaises(Exception):
            lines([])

    @unittest.skip("not done yet")
    def test_exception_dictionary(self):
        with self.assertRaises(Exception):
            lines({})

    @unittest.skip("not done yet")  
    def test_exception_tuple_with_dictionary_and_list(self):
        with self.assertRaises(Exception):
            lines(([],{}))

    @unittest.skip("not done yet")
    def test_exception_tuple_with_string_and_int(self):
        with self.assertRaises(Exception):
            lines(("",4))
