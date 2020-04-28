# Company-Analysis-and-Portfolio-Management


Portfolio management using python
Python programming language is used to manage the portfolio. Various python packages are used to build the portfolio.

Python 
Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter outputs the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.
Matplotlib
Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.

Pandas
Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.Pandas is a Num focus sponsored project. This will help ensure the success of development of pandas as a world-class open-source project and makes it possible to donate to the project.

Pair Plot 

Pair plot is used to understand the best set of features to explain a relationship between two variables or to form the most separated clusters

Application:

Front End GUI – Requesting for the six stocks and the Start, End dates for capturing the adjusted close prices of the corresponding stocks as well as displaying the most active stocks for the period

Stocks Considered: I have preferred to consider the stocks AAPL, SBUX,DIS, GS, JNJ,KO as my preferred stocks to invest. 

Below is the graph of the Stocks daily adjusted closed prices from the date 01-01-2010 to date 01-01-2020.
Annual Returns of each stock:
Pair plot of the stocks to understand the relationship or pattern between two variables
Minimum Variance Portfolio
Maximum Sharpe Portfolio
Efficient Frontier

JSON
•	JSON stands for JavaScript Object Notation
•	JSON is a lightweight data-interchange format
•	JSON is "self-describing" and easy to understand
•	JSON is language independent *

Ex:
var jason = {

"age" : "24",

"hometown" : "Missoula, MT",

"gender" : "male"

}
Syntax Rules
•	Data is in name/value pairs
•	Data is separated by commas
•	Curly braces hold objects
•	Square brackets hold arrays

Live Data Extraction and display of Graphs
 

In the application, I have provided the option to enter the company code for which user wants to know the fundamental and technical analysis.
 
Clicking on enter brings the data(in JSON Format) and displays in the form of a table in the application
Similarly able to extract the income statement, cash flow and balance sheet and display in the application.
Extracting the last 100 days data and Generating the Technical indicators of the stock

Stochastic Fast – Momentum indicator
Bollinger Bands
Aroon-Indicator 
SMA 
EMA
RSI-Indicator 
MACD 

Conclusion:
Able to extract the live prices of a company stock and plot the technical indicators accordingly as well as trace its fundamental indicators that could help in identifying if the company if a good one to invest in and build a portfolio accordingly that could add more value.
Every possible combination of assets that exists is plotted on a graph, with the portfolio's risk on the X-axis and the expected return on the Y-axis. This plot reveals the most desirable portfolios. From the graph, The Portfolio has an min expected return of 13.5% and a standard deviation of 12.4% with the Sharpe ratio 1.03 , and also has an expected return of 19.6% and a standard deviation of 14.5% with Sharpe ratio 1.34(with optimal weights).Drawing an upward sloping hyperbola to connect all the most efficient portfolios together I was able to create an efficient frontier. Investing in any portfolio which are not on this curve would result in undesirable returns.
