class Fibonacci():

    def init_(self):
        pass

    def compute(self, number_of_months, produced_couples):
        mature_rabbits = 0
        young_rabbits = 1
        result = 0

        if number_of_months == 0 or number_of_months < 0:
            raise Exception("The value is zero or negative")
        elif number_of_months == 1 or number_of_months == 2:
            result = 1
        else:
            for generation in range(1, number_of_months):
                temporary = mature_rabbits
                mature_rabbits = young_rabbits + mature_rabbits
                young_rabbits = temporary * produced_couples
                result = young_rabbits + mature_rabbits
                generation += 1

        return result
