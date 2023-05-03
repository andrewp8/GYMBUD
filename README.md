#GYMBUD

## About:

### Built using Python, Flask, MySQL, Jinja, HTML, CSS

### Efficient Note Taking:
- Developed a modern web-based note-taking application using Python, Flask, MySQL, Jinja, HTML, and CSS for the fitness industry. 
- The application allows users to take notes of their exercise sets and reps, including the exercise name and maximum lifting weight. 
- The save button stores the data in the database and displays the notes ordered by muscle group on the right side.
### Nutrition Note Taking:
- The application allows users to enter the nutrition details of each meal, including meal type, total calories, and protein. 
- Users can add as many meals as they want, and the data will be saved in the database. 
- Using SQL, the application processes the saved data to calculate the total protein intake of the day, which is displayed below the target protein intake set by the user. 
- This feature helps users to monitor and adjust their nutrition intake to support their fitness goals.
### Body Fat Percentage Calculator: 
- The application includes an integrated fitness API that allows users to calculate their body fat percentage (BFP). 
- The result displays below the set target BFP, and a BFP chart allows users to compare their results.
### Additional Features: 
- The main page of the application includes an integrated YouTube API that allows users to search for exercise videos. 
- The application also includes a fitness receipts API, which allows users to search for healthy recipes that show nutrition details and protein per serving. 
- These additional features enhance the user experience and provide users with more information to support their fitness goals.
### Security and validation: 
- Implemented security measures such as password hashing using bcrypt and email validation using Python’s class method to ensure user privacy, protection, and validation for registration and logging-in
- User can also add, update their profile picture and profile’s information.

## Installation:
<ol>
  <li> Navigate to your project folder</li>
  <li> Open terminal from the folder and run:
    <ul>
      <li><code>pip install pipenv</code></li>
      <li><code>pipenv install flask pymysql flask-bcrypt</code></li>
      <li><code>pipenv shell</code></li>
      <li><code>python3 server.py</code></li>
    </ul>
  </li>
</ol>

## Usage:
<ol>
  <li>Create an account
    <p align="center" width="100%">
      <img alt="log-in and register" width="80%" src="https://user-images.githubusercontent.com/69804999/236039941-1c9a79d5-af0b-4adf-8426-978856de5756.png"/>
    </p>
  </li>
  <li>If necessary, resources on healthy bodybuilding diets and daily exercise videos are available for reference  
    <p align="center" width="100%">
      <img alt="home page" width="80%" src="https://user-images.githubusercontent.com/69804999/236043081-2e4d13de-ce4f-4b74-aaea-26f87c0e2c6e.png"/>
    </p>
  </li>

</ol>



