# EXPLORATORY DATA ANALYSIS (EDA):

Exploratory Data Analysis is an approach to analyze the data using visual techniques. It is used to discover trends, patterns, or to check assumptions with the help of statistical summary and graphical representations.

Mainly we have two types of analysis: 
* Univariate Analysis
* Multivariate Analysis


# UNIVARIATE ANALYSIS:

Univariate analysis is the simplest form of analyzing data. Uni means one, so in other words the data has only one variable.The main purpose of univariate analysis is to describe the data and find patterns that exist within it.

We have several options for describing data with univariate data:
1. Frequency Distribution Tables
2. Bar Charts
3. Histogram
4. Pie Charts

## Frequency Distribution Tables:

Frequency tells you how often something happened. The frequency of an observation tells you the number of times the observation occurs in the data.
* Tables can show either categorical variables (sometimes called qualitative variables) or quantitative variables (sometimes called numeric variables). You can think of categorical variables as categories (like eye color or sex) and quantitative variables as numbers.
Eg: df['Sex'].value_counts() \
    male      577 \
    female    314 \
    Name: Sex, dtype: int64 \
    
## Bar Charts:

A bar chart is a graph with rectangular bars. The graph usually compares different categories. Although the graphs can be plotted vertically (bars standing up) or horizontally (bars laying flat from left to right), the most usual type of bar graph is vertical.
* The horizontal (x) axis represents the categories; The vertical (y) axis represents a value for those categories.

## Histogram:

Histograms are similar to bar charts; they are a way to display counts of data. A bar graph charts actual counts against categories; The height of the bar indicates the number of items in that category. A histogram displays the same categorical variables in “bins”.

## Pie Charts:

A Pie Chart is a type of graph that displays data in a circular graph. The pieces of the graph are proportional to the fraction of the whole in each category. In other words, each slice of the pie is relative to the size of that category in the group as a whole. The entire “pie” represents 100 percent of a whole, while the pie “slices” represent portions of the whole.


# MULTIVARIATE ANALYSIS:

Multivariate analysis is part of Exploratory data analysis. Based on MULTIVARIATE ANALYSIS, we can visualize the deeper insight of multiple variables.

Multivariate analysis (MVA) is a Statistical procedure for analysis of data involving more than one type of measurement or observation. It may also mean solving problems where more than one dependent variable is analyzed simultaneously with other variables.

There are many different techniques for multivariate analysis, and they can be divided into two categories:

* Dependence techniques 
* Interdependence techniques 

## Dependence Techniques:

Dependence methods are used when one or some of the variables are dependent on others.In machine learning, dependence techniques are used to build predictive models. 
* The analyst enters input data into the model, specifying which variables are independent and which ones are dependent—in other words, which variables they want the model to predict, and which variables they want the model to use to make those predictions.

## Interdependence Techniques:

Interdependence methods are used to understand the structural makeup and underlying patterns within a dataset. In this case, no variables are dependent on others, so you’re not looking for causal relationships. Rather, interdependence methods seek to give meaning to a set of variables or to group them together in meaningful ways.








         