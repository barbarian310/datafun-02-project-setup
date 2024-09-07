''' Final Iteration

Module: Foreshadow Intelligence - Reusable Module for My Data Analytics Projects

Enhance the byline to include key statistics. The statistics for client satisfaction and 
ideal temperatures are now integrated into the byline. Comments are also added for clarity.

'''

import statistics

is_student: bool = True
age_in_years: int = 24
names_of_IDEs_installed: list = ['CLion', 'IntelliJ', 'Pycharm', 'VSCode', 'Visual Studio']
ideal_human_temperatures: list = [98.9, 98.6, 98.5, 98.4, 37.0, 36.9, 36.8]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#Statistics for client satisfaction
satisfaction_min: float = min(client_satisfaction_scores)
satisfaction_max: float = max(client_satisfaction_scores)
satisfaction_mean: float = statistics.mean(client_satisfaction_scores)
satisfaction_stdev: float = statistics.stdev(client_satisfaction_scores)

#Statistics for ideal human temperatures
temp_min: float = min(ideal_human_temperatures)
temp_max: float = max(ideal_human_temperatures)
temp_mean: float = statistics.mean(ideal_human_temperatures)
temp_stdev: float = statistics.stdev(ideal_human_temperatures)

byline: str = f"""Foreshadow Intelligence: Your outlook has never been so good.
It is {is_student} that I am still a student at {age_in_years} years old. However, I have a plethora
of tools at my disposal, including {names_of_IDEs_installed}. As a side note, normal human temperatures are {ideal_human_temperatures} in fahrenheit and celsius respectively. 
The lowest client satisfaction score was {satisfaction_min}, while the highest was {satisfaction_max}.
The average satisfaction score was {satisfaction_mean}, and the standard deviation was {satisfaction_stdev}.
The lowest ideal temperature was {temp_min}, while the highest was {temp_max}.
The average ideal temperature was {temp_mean}, and the standard deviation was {temp_stdev}."""

# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# No parameters are required

#main() function definition
def main() -> None:
    '''Print the statistical information from our global variables.'''
    print(client_satisfaction_info, '\n')
    print(temperature_info, '\n')
    
    
#get_byline() definition
def get_byline() -> str:
    '''This function returns the byline variable, and does not automatically print it'''
    return byline

#main() is only called if the module __name__ is set to '__main__', not when it is imported

if __name__ == '__main__':
    print(get_byline())
