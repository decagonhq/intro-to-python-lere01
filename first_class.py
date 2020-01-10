from statistics import mean, median, mode

class FirstClass:
    def __init__(self, mean, median, mode):
        self.mean = mean
        self.median = median
        self.mode = mode
    
    @staticmethod
    def calc_mean(list_of_grades):
        average = mean(list_of_grades)
    
    @classmethod
    def calc_median(cls, list_0f_grades):
        list_median = median(list_of_grades)
    
    
    def calc_mode(self, list_of_nos):
        self.mode = mode(list_of_nos)
