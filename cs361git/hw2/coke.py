import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
cp = pd.read_csv("/Users/shefalisharma/Downloads/pepsicoke - Sheet1.csv")


cp = cp.filter(['COKE', 'PEPSI'])

x_vals = np.array([np.min(cp["COKE"]), np.max(cp["COKE"])])
x_vals_standardized = (x_vals-cp["COKE"].mean())/cp["COKE"].std(ddof=0)
y_predictions_standardized = cp.corr()["COKE"]["PEPSI"]*x_vals_standardized
y_predictions = y_predictions_standardized*cp["PEPSI"].std(ddof=0)+cp["PEPSI"].mean()
plt.figure(figsize=(8,8))
plt.scatter(cp['COKE'], cp['PEPSI'])
plt.xlabel("COKE")
plt.ylabel("PEPSI")
plt.title("Scatter plot of PEPSI vs. COKE with prediction line")
plt.plot(x_vals, y_predictions, 'r', linewidth=5)
plt.show()