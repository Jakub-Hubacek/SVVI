import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Importing the dataset
dataset = pd.read_csv("dataset_c3.csv")

# Extracting the relevant columns
X = dataset["Pocet hodin ucenia"].values.reshape(-1, 1)  # Independent var
y = dataset["Znamka"].values  # Dependent var

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1 / 3, random_state=1
)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Visualize the Training Set
plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Training Set: Hours of Study vs Grade")
plt.xlabel("Hours of Study")
plt.ylabel("Grade")
plt.show()

# Visualize the Test Set
plt.scatter(X_test, y_test, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Test Set: Hours of Study vs Grade")
plt.xlabel("Hours of Study")
plt.ylabel("Grade")
plt.show()
