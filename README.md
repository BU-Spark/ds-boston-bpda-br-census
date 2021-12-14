# CS506-BDPA-Team 1
Repository containing code and reports related to Boston University's Spark Project Brazilian Community Census Analysis (CS 506) collaboration with Boston Planning & Development Agency (BPDA).

# Introduction

## Project Overview and Goal
Our goal was to analyze public data that tracks the Brazilian community in Massachusetts between the years 2005-2011. By doing this, we are able to tell a story about the Brazilian community over the years and apply our data science skills to explore and analyze the data so that the client can also learn valuable information on the Brazilian community by looking at trends and correlations. 
Our code is easily changeable so that it can be applied to analyze trends in the Brazilian community within any state. This will help identify how trends and correlations vary by state and provide helpful insights into the story of the Brazilian population during these years.   
## Dependencies
To start, make sure Python is installed on your computer which can be done using python --version. To process the data, we used Pandas and NumPy. To perform our visualizations, we used the following Machine Learning libraries: matplotlib.pyplot and seaborn. Please make sure you have the dependencies installed before running any code in this repository. If not installed, make sure pip is installed using pip -V, and then execute the following commands: pip install matplotlib, pip install pandas, pip install numpy, and pip install seaborn. 
## How to Use Code
Use jupyter notebook or google collab depending on selected place to run the notebooks.
Some code produces csv where you can see the result there, others produce the results right below the cell.
The code that we wrote can be used to retrieve the data on the Brazilian population for any state by only changing a few lines of codes. Anytime that we got information from the dataset “years,” we would write something such as years[25][4]. The 25 in the example is referencing the State Code (see the State Codes tab in the Brazilian Immigrants.xlxs document) for Massachusetts, and if one wants to focus on another state then they will change that 25 anytime that we call the dataset “years” to the State Code for that specific state. Changing the State Code anytime we call the dataset years and then running all of the cells in order will result in visualizations for every feature above for the Brazilian population in that state over the years 2005-2011. 
## File paths for notebooks to run code
All of our data is within github -> Team 1 branch -> folder "Notebook Files"
Our actual code is found within the Brazilian Immigrant Population Over Time.ipynb file
Our data is split up by year, with the file being named Brazilian Immigrants 20**.xlsx where the ** represents the ending digits of the year.
## Data
The data that we used for this project was received from the client and is from the Public Use Microdata Sample (PUMS) 2005 - 2011.
## Future Work
For future work, our clients can easily change our code in order to apply the analysis to other states so that we can see how trends vary state by state. Moreover, our client discussed making an interactive website with a map of the United States, and information about that state's Brazilian population over the years would pop up when a user clicked on a state. 
# Thank You To The BPDA and BU Spark!

