import unittest
from hw2 import (
    create_rectangle,
    shorter_duration_than,
    songs_shorter_than,
    running_time,
    validate_route,
    longest_repetition
)
from data import Rectangle, Point, Duration, Song

class TestCases(unittest.TestCase):
    # Part 1: Tests for create_rectangle
    def test_create_rectangle_top_left(self):
        point1 = Point(1.0, 5.0)
        point2 = Point(3.0, 2.0)
        expected = Rectangle(Point(1.0, 5.0), Point(3.0, 2.0))
        result = create_rectangle(point1, point2)
        self.assertAlmostEqual(result.top_left.x, expected.top_left.x)
        self.assertAlmostEqual(result.top_left.y, expected.top_left.y)

    def test_create_rectangle_bottom_right(self):
        point1 = Point(3.0, 4.0)
        point2 = Point(1.0, 1.0)
        expected = Rectangle(Point(1.0, 4.0), Point(3.0, 1.0))
        result = create_rectangle(point1, point2)
        self.assertAlmostEqual(result.bottom_right.x, expected.bottom_right.x)
        self.assertAlmostEqual(result.bottom_right.y, expected.bottom_right.y)

    # Part 2: Tests for shorter_duration_than
    def test_shorter_duration_than_true(self):
        duration1 = Duration(2, 30)
        duration2 = Duration(3, 0)
        result = shorter_duration_than(duration1, duration2)
        self.assertAlmostEqual(result, True)

    def test_shorter_duration_than_false(self):
        duration1 = Duration(4, 0)
        duration2 = Duration(3, 45)
        result = shorter_duration_than(duration1, duration2)
        self.assertAlmostEqual(result, False)

    # Part 3: Tests for songs_shorter_than
    def test_songs_shorter_than_one_match(self):
        song1 = Song("Artist1", "Song1", Duration(3, 0))
        song2 = Song("Artist2", "Song2", Duration(2, 30))
        song3 = Song("Artist3", "Song3", Duration(4, 0))
        result = songs_shorter_than([song1, song2, song3], Duration(3, 0))
        expected = [song2]
        self.assertAlmostEqual(len(result), 1)
        self.assertEqual(result, expected)

    def test_songs_shorter_than_multiple_matches(self):
        song1 = Song("Artist1", "Song1", Duration(3, 0))
        song2 = Song("Artist2", "Song2", Duration(2, 0))
        song3 = Song("Artist3", "Song3", Duration(2, 45))
        result = songs_shorter_than([song1, song2, song3], Duration(3, 0))
        self.assertAlmostEqual(len(result), 2)

    # Part 4: Tests for running_time
    def test_running_time_exact(self):
        song1 = Song("Artist1", "Song1", Duration(3, 0))
        song2 = Song("Artist2", "Song2", Duration(2, 30))
        result = running_time([song1, song2], [0, 1])
        expected = Duration(5, 30)
        self.assertAlmostEqual(result.minutes, expected.minutes)
        self.assertAlmostEqual(result.seconds, expected.seconds)

    def test_running_time_with_repeated_indices(self):
        song1 = Song("Artist1", "Song1", Duration(2, 45))
        song2 = Song("Artist2", "Song2", Duration(3, 15))
        result = running_time([song1, song2], [0, 0, 1])
        expected = Duration(8, 45)
        self.assertAlmostEqual(result.minutes, expected.minutes)
        self.assertAlmostEqual(result.seconds, expected.seconds)

    # Part 5: Tests for validate_route
    def test_validate_route_true(self):
        routes = [["CityA", "CityB"], ["CityB", "CityC"], ["CityC", "CityD"]]
        route = ["CityA", "CityB", "CityC", "CityD"]
        result = validate_route(routes, route)
        self.assertAlmostEqual(result, True)

    def test_validate_route_false(self):
        routes = [["CityA", "CityB"], ["CityB", "CityC"]]
        route = ["CityA", "CityB", "CityD"]
        result = validate_route(routes, route)
        self.assertAlmostEqual(result, False)

    # Part 6: Tests for longest_repetition
    def test_longest_repetition(self):
        result = longest_repetition([1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1])
        expected = 7
        self.assertAlmostEqual(result, expected)

    def test_longest_repetition_single_element(self):
        result = longest_repetition([1, 1, 1, 1])
        expected = 0
        self.assertAlmostEqual(result, expected)

# Run the tests
if __name__ == '__main__':
    unittest.main()
