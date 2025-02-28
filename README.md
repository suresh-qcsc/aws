# Illustration of how Lambda handles traffic bursts

## 📌 Overview
This code illustrates how AWS Lambda manages traffic bursts by depicting the number of requests, concurrency limits, and the scaling of concurrent executions. I would like to know how the application will react to a sudden influx of requests. Notably, all of the account's concurrency may not be available immediately, which can result in requests being throttled for several minutes, even when the overall limit exceeds the incoming surge.

## 🖥️ Features
📊 Displays the number of requests and concurrent executions over time. 
🔹 Emphasizes AWS Lambda's concurrency scaling with annotations. 
🌑 Utilizes a **dark-themed** visualization for enhanced readability.

## 📦 Requirements
Ensure you have Python and the following libraries installed:

pip install matplotlib numpy

## 🚀 Usage
Run the script to generate and display the graph:

python lambda_concurrency_plot.py

## 📝 Explanation

- Green Line: Represents the number of requests.
- Blue Line: Represents concurrent executions.
- Orange Line: Represents the AWS Lambda’s concurrency limit.
- Annotations: Explain how Lambda scales up concurrency.

## 📸 Output

![Lambda Concurrency](Lambda_concurrency_v1.gif)


## 💡 Contributing
Feel free to fork this repository and submit pull requests to improve the script.

## 🛠️ License
This project is licensed under the MIT License.

## Initialize a Git Repository
Inside the project folder, run:

git init
git add .
git commit -m "Initial commit: Lambda Concurrency Graph"

## Push to GitHub
1) Create a GitHub repository with a relevant name like lambda-concurrency-graph.
2) Link the remote repository:
git remote add origin https://github.com/YOUR-USERNAME/lambda-concurrency-graph.git
3) Push the code:
git branch -M main
git push -u origin main

## Add a .gitignore File (Optional)
To avoid uploading unnecessary files, create a .gitignore file:

__pycache__/
1) *.png 2) *.gif

## Final Notes
- If you make changes, always commit and push:
1) git add . 2) git commit -m "Updated the graph annotations" 3) git push origin main

