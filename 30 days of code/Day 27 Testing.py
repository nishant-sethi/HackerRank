
from random import randint

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):

    data = set()
    while len(data) < 10:
        data.add(randint(0, 100))

    @staticmethod
    def get_array():
        # complete this function
        data = TestDataUniqueValues.data
        return list(data)


    @staticmethod
    def get_expected_result():
        # complete this function
        data = TestDataUniqueValues.get_array()
        return data.index(min(data))

class TestDataExactlyTwoDifferentMinimums(object):

    data = set()
    while len(data) < 9:
        data.add(randint(0, 100))
    newData = list(data)
    newData.append(min(newData))

    @staticmethod
    def get_array():
        # complete this function
         data =  TestDataExactlyTwoDifferentMinimums.newData
         return data

    @staticmethod
    def get_expected_result():
        # complete this function
        data = TestDataExactlyTwoDifferentMinimums.get_array()
        return data.index(min(data))