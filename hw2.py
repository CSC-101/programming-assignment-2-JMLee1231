import data
from data import Rectangle, Point, Duration, Song
# Write your functions for each part in the space below.

# Part 1
# Function to create a Rectangle object from two given Point objects.
# Input:
#   There are two inputs of type:
#   Point - each parameter is of type Point, which represents a 2D coordinate (x, y) on a plane.
# Output:
#   Rectangle - a Rectangle object defined by top-left and bottom-right points, determined by comparing x and y values.
def create_rectangle(point1: Point, point2: Point) -> Rectangle:
    top_left = Point(min(point1.x, point2.x), max(point1.y, point2.y))
    bottom_right = Point(max(point1.x, point2.x), min(point1.y, point2.y))

    return Rectangle(top_left, bottom_right)

# Part 2
# Function to determine if the first Duration is shorter than the second.
# Input:
# There are two inputs of type:
#   Duration - each parameter is of type Duration, representing a time period in minutes and seconds.
# Output:
#   bool - True if the first Duration is shorter than the second, otherwise False.

def shorter_duration_than(duration1: Duration, duration2: Duration) -> bool:
    if duration1.minutes * 60 + duration1.seconds < duration2.minutes * 60 + duration2.seconds:
        return True
    else:
        return False

# Part 3
# Function to return a list of Song objects with a duration shorter than a given Duration.
# Input:
#   list[Song] - the first parameter is a list of Song objects, each representing a song with a title and duration.
#   Duration - the second parameter, representing an upper bound for song duration.
# Output:
#   list[Song] - a list containing Song objects from the input list that have a duration shorter than the specified Duration.
def songs_shorter_than(list1:list[Song], duration1: Duration) -> list[Song]:
    upperBound = duration1.minutes*60+duration1.seconds
    returnList = []

    for song in range(len(list1)):
        song_duration = list1[song].duration.minutes*60 + list1[song].duration.seconds
        if song_duration < upperBound:
            returnList.append(list1[song])
    return returnList

# Part 4
# helper function - returns a songs duration in seconds
def song_in_seconds(song1: Song) -> int:
    return song1.duration.minutes*60+song1.duration.seconds

# Function to calculate the total running time of selected songs in a playlist.
# Input:
#   list[Song] - the first parameter is a list of Song objects, each with a title and a Duration.
#   list[int] - the second parameter is a list of integers representing song indices for the playlist.
# Output:
#   Duration - a Duration object representing the total running time of the playlist, with seconds under 60 and non-negative.


def running_time(list1: list[Song], list2:[int]) -> Duration:
    total_time = 0
    for idx in range(len(list2)):
        if list2[idx]<0 or list2[idx]>len(list1)-1:
            list2.remove(idx)
    for idx in range(len(list2)):
        total_time += song_in_seconds(list1[list2[idx]])
    duration_minutes = total_time//60
    duration_seconds =total_time%60
    return Duration(duration_minutes,duration_seconds)
# Part 5
# helper function to determine if a connection exists within the routes list
def route_exists(list1: list[list[str]], city1:str, city2: str) -> bool:
    for connection in list1:
        # Check both possible orders
        if (connection[0] == city1 and connection[1] == city2) or (connection[0] == city2 and connection[1] == city1):
            return True
    return False

# Function to validate if a route through cities is connected as per given city links.
# Input:
#   list[list[str]] - the first parameter is a list of city link pairs, with each link as a list of two city names (str), where order is not meaningful.
#   list[str] - the second parameter is a list of city names representing a route from the first to the last city in sequence.
# Output:
#   bool - True if the route is valid, with consecutive cities linked; otherwise False.

def validate_route(list1: list[list[str]], list2: list[str]) -> bool:
    if len(list2)<2:
        return True
    for idx in range(len(list2)-1):
        if not (route_exists(list1, list2[idx], list2[idx+1])):
            return False
    return True

# Part 6
# Function to find the starting index of the longest contiguous repetition of an integer in a list.
# Input:
#   list[int] - a list of integers where we seek the longest contiguous repetition of the same integer.
# Output:
#   Optional[int] - the starting index of the longest contiguous repetition, or None if the list is empty.

def longest_repetition(list1:list[int]):
    if len(list1) == 0:
        return None
    longest_reps = 0
    rep_counter = 1
    index_of_longest = 0

    for idx in range(1, len(list1)):
        if list1[idx] == list1[idx-1]:
            rep_counter+=1
        else:
            if rep_counter > longest_reps:
                longest_reps = rep_counter
                index_of_longest = idx -rep_counter
            rep_counter = 1

        if rep_counter > longest_reps:
            index_of_longest = len(list1) - rep_counter

    return index_of_longest
