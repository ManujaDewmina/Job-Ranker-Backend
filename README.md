# Job Ranker - LSTM based sentiment analysis system
<div align='center'>
    <img src="https://github.com/ManujaDewmina/JobRanker-frontend/assets/92631934/105316f1-57d5-4492-bbee-6d78f26eac8b" width="150" align="center">
</div>

Job Ranker Frontend Repository : https://github.com/ManujaDewmina/Job-Ranker-Frontend

Job Ranker Backend Repository : https://github.com/ManujaDewmina/Job-Ranker-Backend

## Overview
This project is a job ranker system that uses sentiment analysis to score job reviews, rank jobs under different categories and classify ranked jobs according to user preferences. The system is designed to help job seekers find the best jobs that match their interests and requirements, and to help employers get feedback on their jobs and identify areas for improvement. 

The system uses an LSTM model to extract the sentiments of job reviews and generate a rating for the job. The system also takes into account user preferences, such as work-life balance, culture and diversity to rank and classify jobs. Job Ranker provides a user-friendly mobile interface for users to easily find the best jobs that match their needs and interests.

The evaluation of the system is conducted on the Glassdoor job reviews data set, resulting in an accuracy of 81\% in sentiment classification. This indicates the system's effectiveness in extracting sentiments from job reviews and generating accurate job ratings. 

Furthermore, the use of MySQL for complex database management of review data enables the storage and management of large amounts of data, ensuring reliable and accurate results for the system. The application backend follows a RESTful API
design pattern, providing a set of operations to interact with the underlying MySQL database and LSTM model.

## Video Demonstration
<div align='center'>
<video src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/1e3f428f-da3f-442c-90ff-c4dc0fd661b7">
</div>

## Objectives
  - Rate job reviews based on sentiment analysis and rank jobs under different categories. This will help job seekers to quickly identify the best jobs in a particular category.
  - Classify ranked jobs according to user preferences. This will help job seekers to find jobs that match their interests and requirements.
  - Provide a new review adding system that automatically analyzes and rates reviews in real time. This will help to ensure that the system is always up-to-date with the latest feedback from users.
  - Develop a user-friendly mobile interfaces and easy to use functionalities. This will make it easy for job seekers to find and manage their favourites.

## Used Technologies

- Languages
  <ul>
      <li>Dart - For frontend mobile application development</li>
      <li>Python - For model and backend services development</li>
      <li>SQL - For managing data held in MySQL database</li>
    </ul>
- Tools
  <ul>
    <li>Android Studio, Visual Studio Code, Kaggle, Google Colab</li>
  </ul>
- Libraries
  <ul>
    <li>Tensorflow, Scikit Learn, Pandas, Numpy, Matplotlib, Seaborn, nltk, Keras </li>
  </ul>
- Database / Storage 
  <ul>
    <li>MySQL - Used as the relational database management system because of its simplicity, performance,and scalability. MySQL helps to implement complex business logic with large dataset for the system.</li>
  </ul>
- Authentication
  <ul>
    <li>Firebase Authentication</li>
  </ul>
- Deployment
  <ul>
    <li>Docker</li>
    <li>Google Cloud Platform</li>
    <li>Virtual Machine</li>
  </ul>
- Dataset : https://www.kaggle.com/datasets/davidgauthier/glassdoor-job-reviews

## Development Architecture Diagram
<div align='center'>
    <img src="https://github.com/ManujaDewmina/JobRanker-frontend/assets/92631934/63cddab1-71f6-4d57-83d4-0f94e1ddebc1" width="600" align="center">
</div>

## LSTM Model Architecture Diagram
<div align='center'>
    <img src="https://github.com/ManujaDewmina/JobRanker-frontend/assets/92631934/5ed8b6b7-e0f5-4207-bdfd-a900f227c974" width="600" align="center">
</div>

## LSTM Model Performance
<div align='center'>
    <img src="https://github.com/ManujaDewmina/JobRanker-frontend/assets/92631934/99c74e68-911e-4308-ba6d-6dc8351bef1d" width="600" align="center">
</div>

## Deployment Architecture Diagram
<div align='center'>
    <img src="https://github.com/ManujaDewmina/JobRanker-frontend/assets/92631934/29505680-711a-4210-90ca-b0789a4d6201" width="600" align="center">
</div>

## Features
### 1. Login
This feature allows users to create an account and log in to the application.User aslo have forgot password option. Once logged in, users will have access to all of the features of the application. And user can logout anytime.
<div align='center'>
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/c5c5d797-76f8-44d9-9aff-6f453d0149bc" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/f46ea1a5-515c-4a06-8ae3-992167d7599a" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/44ea76ed-3a82-47f3-8e14-de9c3a7a4f21" width="150" align="center">
</div>

### 2. Add New Reviews
This feature allows users to add new reviews of jobs that they have worked at. Users can rate the job under categories work life balance, culture values, diversity inclusion, career opportunities, company benefits, senior management, recommend, and CEO approval.And also users can write a review about the job. Once they submit the new reviews they will evaluate automatically using LSTM sentiment analysing  model in real time and give a score for that review. After that firm total ratings will be updated by the system using the average of all reviews for that firm.\\
This feature is essential for a job ranking application. It allows users to contribute to the database of job reviews, which is used to rank jobs and provide users with recommendations.
<div align='center'>
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/b950bfc8-1dc7-4437-a638-f16cab745401" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/30e33acc-546b-4767-ae49-3452f7709cc5" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/c39bbebd-90b0-4c71-b267-eddb6c3ea078" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/a0b12db0-ff1d-4781-a718-a210ce07323a" width="150" align="center">
</div>

### 3. Rated Job Details
This feature allows users to view a list of all of the jobs that have been rated by other users. Users can filter the list by firm name. Users can  view detailed reviews about each firm, such as overall score calculated using given reviews by LSTM model, work-life balance, culture, diversity, career opportunities, compensation and benefits, senior management, recommendation and CEO approval. Also users can get an idea about submitted users job titles and review submitted years for better understanding.
<div align='center'>
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/0c1245f6-187a-46fc-a6bb-2acf7f32ccbc" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/24cd3c62-5649-4747-b5c9-023da1cd538d" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/119da193-dc3e-484d-9e29-35c25c33d064" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/e6301f08-bdca-4017-bc5e-f856a516f41c" width="150" align="center">
</div>

### 4. Job Classifier
This feature helps users to find best jobs according to their preferences. Once user select their preferred categories user will get a company list best suits for their preferences and ranked them using total score from all selected categories.
<div align='center'>
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/8081446b-0fcd-43cf-a43a-1cd8cf80e353" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/6d03bc96-d27a-499c-852c-a4627dd47248" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/c561b8c0-950f-4f8b-a5d9-8f0eacabfd09" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/ef004a27-2c96-4a0a-b79b-2484cb4f64ab" width="150" align="center">
</div>

### 5. User profile
Using user profile section user can see firms he marked as favourites and see the present ratings of that firms.
<div align='center'>
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/034f29cf-2611-49a6-85f9-6e183fd6d47e" width="150" align="center">
  <img src="https://github.com/ManujaDewmina/Job-Ranker-backend/assets/92631934/09d695e6-76a3-4c73-9b03-ff5de0f0b84c" width="150" align="center">
</div>

## Conclusion

In conclusion, the Job Ranker application is a valuable tool for both job seekers and employers. It uses sentiment analysis and user preferences to rank and classify jobs, helping job seekers find the best jobs that match their needs and interests. Job Ranker also provides valuable feedback to employers, helping them identify areas for improvement.

Using LSTM for sentimental analysis improve the review analysis process by giving better ratings for reviews after getting deeper insights from reviews. Database management using MySQL database give real-time data management with LSTM model and also MySQL helps to implement complex business logic for the system. Furthermore, front-end mobile application gives better user experience by providing users with a clear and intuitive interface to interact and better visualisation over analysed data.

Overall, Job Ranker can show as a useful tool that empowers individuals to navigate the job market effectively and assists businesses in making informed hiring decisions. Its effectiveness come from its ability to combine sentiment analysis, user preferences, and a robust data management system. With its user-friendly interface and comprehensive data visualisation capabilities, Job Ranker proves to be an invaluable resource for both job seekers and employers.
