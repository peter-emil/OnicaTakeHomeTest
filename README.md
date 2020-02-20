# Peter's Take-Home Test For Onica

This repository contains Peter's submission for Onica's take-home test.
The deliverables as well as requirements. assumptions, tradeoffs, .. etc. are documented here as well


# Deliverables

 - [x] Amazon DynamoDB Table
 - [x] AWS Lambda
 - [x] API Gateway

# Chosen Technologies

 - For the Infrastructure as Code technology, I chose `serverless`. Although this was my first time using it, I decided to learn something new while working on this take-home. Inside `serverless.yml` I also used raw CloudFormation when I needed to.
 - Here are the `serverless` plugins I used
	 - serverless-python-requirements: Used to automatically install the requirements inside requirements.txt to have our semi-reproducible build
	 - serverless-pseudo-parameters: Used to be able to reference AWS Pseudo Parameters inside the `serverless.yml`
 - For the application code, I chose Python and was careful to build a modular micro-service following the necessary patterns to build a loosely-coupled code-base. The architecture in this project follows the Layered Architecture pattern demonstrated in Eric Evan's Domain Driven Design (The blue book).

# Installing Requirements

 1. Install Python, at least version 3.7. Detailed instructions on this are found [here](https://realpython.com/installing-python/).
 2. Install `virtualenv` by typing `python -m pip install virtualenv`.
 3. Create a virtualenv by typing `python -m virtualenv -p python venv/` and activate by typing `source venv/bin/activate`.
 4. Install Python requirements by typing `python -m pip install -r requirements.txt`
 5. Install `serverless`. Detailed instructions on this are found [here](https://serverless.com/framework/docs/getting-started/).
 6. Install Node and npm from [here](https://nodejs.org/en/).
 7. Install serverless plugins by typing `npm install`.
 8. Authenticate `serverless` with your AWS account. Many methods for accomplishing this can be found [here](https://serverless.com/framework/docs/providers/aws/guide/credentials/).

# Things I Would Change In Production

 - Write tests, tests, and more tests. For the most part, it makes sense here to set using the `doctest` module. It's easy, simple, and gets the job done.
 - Define more custom exceptions to handle different business logic cases, move things like `UserId` and `Name` to another file containing value objects because I just placed them the `entities.py` file for now while they are in fact, value objects.
 - Add a CI/CD pipeline to automate the process of testing the code, integrating with dependencies, and faster deployment.