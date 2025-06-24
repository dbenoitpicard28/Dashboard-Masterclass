"""
1. Data cleaning:
- Handling duplicates, missing values, and outliers
How do we know if we have duplicated values?
- We need to have an key ID - Unique ID
(After importing your data, you have to look for an UniqueID to be able to remove duplicates)
- Howc do we know if a variable contains missing values?
(There are somecdedicated functions that detect missimg values based on the software you are using)

- How do we detect an outlier and how does it help?
10,000
20,000
80,000
190,000
290,000
350,000
"""

# Install important packages
# tHE MOST IMPORTANT PACKAGES: PANDAS, NUMPY
# pip install django
# pip install pandas
# pip install numpy 
# pip install matplotlib
# pip install seaborn   
# pip install scikit-learn

name = "Celestin"
dob = "2000-01-01"
age = 23
age= "23"
age=int(age)
print(age)
#Howdoweexecutepythonfunction functions?
#function_name(parameters)
print(20)
print("This is my name")
print(str(age))
age1 = 23
age2=20
age3="20"
print(age3*3)

# How to create a list
# Lists are mutable, meaning they can be changed after creation
# They are used to store multiple items in a single variable
# Lists are defined using square brackets []
# Example of a list
# Lists can contain different data types
# Lists can be used to store multiple items in a single variable
# Lists are mutable, meaning they can be changed after creation
# Lists are defined using square brackets []
# Example of a list
name_list = ["Celestin", "John", "Doe"]
print(name_list)
name_list.append("Jane")
print(name_list)


# How to create a tuple
# Tuples are immutable, meaning they cannot be changed after creation
# They are used to store multiple items in a single variable
# Tuples are defined using parentheses ()
# Example of a tuple
# Tuples can contain different data types
# Tuples can be used to store multiple items in a single variable
# Tuples are immutable, meaning they cannot be changed after creation
# Tuples are defined using parentheses ()
name_turple = ("Celestin", "John", "Doe")
print(name_turple)
name_turple = name_turple + ("Jane",)
print(name_turple)


# How to create a dictionary
# Dictionaries are mutable, meaning they can be changed after creation
# They are used to store data in key-value pairs
# Dictionaries are defined using curly braces {}    
# Example of a dictionary
# Dictionaries can contain different data types
# Dictionaries can be used to store multiple items in a single variable
# Dictionaries are mutable, meaning they can be changed after creation
# Dictionaries are defined using curly braces {}
# Example of a dictionary
# Dictionaries can contain different data types
# Dictionaries can be used to store multiple items in a single variable
# Dictionaries are mutable, meaning they can be changed after creation
# Dictionaries are defined using curly braces {}
# Example of a dictionary
# Dictionaries can contain different data types
# Dictionaries can be used to store multiple items in a single variable
# Dictionaries are mutable, meaning they can be changed after creation
# Dictionaries are defined using curly braces {}
# Example of a dictionary
# Dictionaries can contain different data types
# Dictionaries can be used to store multiple items in a single variable
# Dictionaries are mutable, meaning they can be changed after creation
# Dictionaries are defined using curly braces {}
# Example of a dictionary
# Dictionaries can contain different data types
# Dictionaries can be used to store multiple items in a single variable 
my_dict = {
    "name": "Celestin",
    "age": 23,
    "dob": "2000-01-01"
}
print(my_dict)
my_dict["name"] = "John"
print(my_dict)  


# How to create a set
# Sets are unordered collections of unique items
# Sets are defined using curly braces {}
# Example of a set
# Sets can contain different data types
# Sets can be used to store multiple items in a single variable
# Sets are unordered collections of unique items
my_set = {"Celestin", "John", "Doe"}
print(my_set)
my_set.add("Jane")
print(my_set)           
# How to create a frozenset
# Frozensets are immutable sets
# Frozensets are defined using the frozenset() function
# Example of a frozenset
# Frozensets can contain different data types               
my_frozenset = frozenset({"Celestin", "John", "Doe"})
print(my_frozenset)
my_frozenset = my_frozenset.union(frozenset({"Jane"}))
print(my_frozenset)

# How to import a dataset using pandas
# Pandas is a powerful data analysis library in Python
# It provides data structures and functions needed to work with structured data
# Pandas can read data from various file formats such as CSV, Excel, SQL, etc
# To use pandas, you need to install it first using pip
# pip install pandas
# After installing pandas, you can import it in your Python script
# Importing pandas
import pandas as pd 
# Reading a CSV file using pandas
# You can read a CSV file using the read_csv() function
# The read_csv() function takes the file path as an argument
# Example of reading a CSV file     
data = pd.read_csv( "/Users/picard/Documents/GitHub/Dashboard-Masterclass/Dataset_1.csv", encoding="latin" , low_memory=False )
print(data.head())  # Display the first 5 rows of the dataframe   

print(data.info())  # Display information about the dataframe
print(data.describe())  # Display statistical summary of the dataframe
# Display the columns of the dataframe
print(data.columns)  # Display the columns of the dataframe
print(data.dtypes)  # Display the data types of the columns
# Display the shape of the dataframe
print(data.shape)  # Display the shape of the dataframe (rows, columns)
# Display the first 5 rows of the dataframe
print(data.tail())  # Display the last 5 rows of the dataframe

data.isna().sum()  # Display the number of missing values in each column

slice_1 = data.iloc[0:5, 0:3]  # Slicing the dataframe to get the first 5 rows and first 3 columns
print(slice_1)  # Display the sliced dataframe