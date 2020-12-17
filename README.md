# Machine Learning to Influence Soccer Betting

<img src="https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Ftimes%2Fprod%2Fweb%2Fbin%2Fefe61ce4-a3e3-11ea-a585-dcb14d2bcd47.jpg?crop=3812%2C2144%2C124%2C326&resize=1180">

# Objective
My goal is to predict the outcome of soccer matches in the biggest leagues in the world. The UEFA Champions League, English Premier League, German Bundesliga, and the Spanish La Liga are the main focus. These leagues indicate the highest level of play and viewership in the sport. <br>  
The sports betting industry as a whole is a multi-hundred-billion dollar behemoth, with soccer taking the top spot. This tool was constructed with the goal of influencing betting habits by analyzing trends in past match results to help the gambler have a more nuanced look at the match in question and therefore place a more educated bet. 

# Data
![FiveThirtyEight](Images/538.png)
The FiveThirtyEight website hosts years of match history, club SPI(Soccer Performance Index) data and odds. The match data also includes projected scores, relative importance, XG(expected goals), and score. To keep the interface simple, and not overwhelm the user, the model takes only the team SPIs and odds. From those inputs, it calculates the expected winner, and the user can use that information to make an even more educated decision on their betting. 

# Insights
Aside from the EDA side, most of my time on this project was spent tuning model hyperparameters. Some of the classifiers I had tested ended up performing pretty poorly due to some class imbalance and low number of features. The currently deployed model is a K-nearest neighbor model, but this is subject to change as the project evolves. I will be testing a neural network on this data, as I think those types of algorithms are capable of performing well in this context. 

# Results
The final KNN model performed 22% better than the baseline, and will be continued to test on live matches over the winter. As I learn more and see how the model performs outside the vacuum of this notebook, I'll continue to make changes. 

# Process
1. Data was collected from FiveThirtyEight. 
2. Data was preprocessed and cleaned up in the DataCleaning.ipynb.
3. More EDA and all modeling is in Main.ipynb. 
4. Final KNN model was then tuned and pickled to be used to deploy via Streamlit/Heroku. 

# Presentation
Further analysis and slide show can be found here.
