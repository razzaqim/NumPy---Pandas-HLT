import pandas as pd

maths_results = pd.DataFrame ([[29, 40, "fail"], [18 , 85, "pass"], [21, 98, "pass"], [26, 76, "pass"], [20, 30, "fail"]], 
                        index = ["Hana", "Bella", "Jay", "Terry", "Niya"],
                        columns = ["Age", "Percentage score", "Outcome",])
print(maths_results)

print()
print("Niya's results")
print(maths_results.loc["Niya"])
print()
print("Percentage score mean")
results_mean = maths_results["Percentage score"].mean()
print(results_mean)
print()
print("Students who scored less than or equal to 40%")
myfilter = maths_results["Percentage score"] <= 40
print(myfilter)
print()
print("Top 3 students")
filterr = maths_results["Percentage score"] > 40 
highscores = maths_results[filterr]
print(highscores.head(3))
print()
print("Students over 20 that passed")
double_filter = (maths_results["Outcome"] == "pass") & (maths_results["Age"] > 20)
filtered = maths_results[double_filter]
print(filtered)
print()
print("Highest Score")
top_score = maths_results["Percentage score"] 
print(top_score.max())
print()
print("Youngest Student")
top_score = maths_results["Age"] 
print(top_score.min())
print()
print("Ages of all students")
print(maths_results["Age"])
print()
print("Outcome of all students")
print(maths_results.iloc[0: , 2]) 
print()
print("Sorting students in age order")
print(maths_results.sort_values("Age"))
print()
print("Rename score column")
print(maths_results.rename(columns={"Percentage score":"Score(%)"}))