a brief overview of the CI/CD workflow for the Streamlit app that uses data from the yfinance API to show 10 popular stocks trends.



The CI/CD workflow for this app uses GitHub Actions to build and deploy the app to a Docker Hub. The workflow has the following steps:

1:Checkout code: The workflow checks out the code from the GitHub repository.

2:Set up Python:  sets up a Python environment.

3:Install dependencies:  installs the required dependencies for the Streamlit app.

4:Run Pylint: The workflow runs Pylint to check the code for potential errors and styling issues.

5:Run Pytest: The workflow runs Pytest to run the unit tests for the Streamlit app.

6:Build Docker image: Then builds a Docker image for the Streamlit app.

7:Push Docker image to Docker Hub: The workflow pushes the Docker image to Docker Hub.


<img width="1440" alt="Screenshot 2024-01-06 at 12 52 57" src="https://github.com/Malatesh-Patil-67/streamlit/assets/107174504/a43ceed1-5e1f-462d-9de4-1e30e4e4c4c5">




![image](https://github.com/Malatesh-Patil-67/streamlit_cicd/assets/107174504/d7000042-138e-4c59-82bd-1cb474a9b764)




