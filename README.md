# Personalized Workout Plan
===================

These are the major functions of Fitness Planner as a service:

1. Service that allows user creation and authentication
2. Users can create their own workout plans and Fitness goals
3. Users are enabled to track their goals and update weight tracking information
4. Users can exercise according to guided workout plan, which gives next exercises in real time

## Getting started
---
### Environment Setup

### Step 1: Setup local repository


Clone the repo

```bash
git clone https://github.com/tmetreveli/Personalized-Workout-Plan.git
```


### Step 2: Setup external requisites

[Docker]

Ensure you have docker running in your machine. [If not, Go to Step 3]

[Docker run]

Run the following command, so docker can initialise on your local.

```bash
docker compose up
````


### Step 3: Setup In your local instead of DOCKER (This is in case docker is not required.)

Install Python 3.9 on your machine.

> Recommended to install [pyenv](https://github.com/pyenv/pyenv) and then install Python 3.9 using pyenv.

#### Linux:

Use your favourite package manager:

Ubuntu:
```bash
sudo apt install python3
```

Fedora:
```bash
sudo dnf install python3
```

RHEL/Centos:
```sh
sudo yum install python3
```

#### Windows:

Recommended to use a package manager like [chocolatey](https://chocolatey.org/) or [winget](https://github.com/microsoft/winget-cli)

OR

Directly [download Python](https://www.python.org/downloads/)

#### Mac

```bash
brew install python
```

>If you are a PyCharm user, run export LC_CTYPE=en_US.UTF-8 to avoid codec errors.
>Add it to your .bash_profile to set it automatically whenever you login


### Step 4: Install dependencies


```bash
pip install -r requirements.txt
```

> Problems installing typed_ast or psycopg2? Get prebuilt binaries from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

In case of M1 Mac, [install postgres using homebrew](https://formulae.brew.sh/formula/postgresql)


### Step 5: Running the Django server

#### 5.1 Start Postgres

Prior to running the server, please ensure that you have your postgres server up and running. 

#### 5.2 Create Database fitness_planner  [This needs to be done ONLY  if DB doesn't exist]
Ensure there is a DB called "fitness_planner" created in your local postgres server.
```bash
psql -U your_admin_username -d your_default_database -c "CREATE DATABASE fitness_planner WITH OWNER postgres IF NOT EXISTS;"
```

#### 5.3 Set DB creds  [This needs to be done ONLY  if DB doesn't exist]
* Go to fitness_planner/settings.py
* Update the DATABASES json to your local credentials for postgres.


#### 5.4 Apply Migrations  

```bash
python manage.py migrate
```

#### 5.4.1 Apply prefilled data

```bash
python manage.py create_sample_dataset
```
#### 5.5 Start the server

Fitness Tracker is a Django application.
To run the django server,

```bash
python manage.py runserver 0.0.0.0:8007
```

[Solutions Engg Onboarding]: https://outline.skit.ai/doc/solutions-engineer-onboarding-OuUiRimbbR
[Redis]: https://redis.io/topics/quickstart
[pyenv]: https://realpython.com/intro-to-pyenv/
[Mac]: https://gitlab.com/vernacularai/voice-services/integration-proxy/-/edit/master/README.md#mac
[Postgres DB]: https://www.postgresql.org/download/




Fitness API Testing: 
===========

## Authentication

To access the API endpoints, you need to create a user and collect the access token provided. Use this access token as a Bearer token in the headers of all subsequent requests for authentication.

### Create a User

- Endpoint: `POST api/create_user/`
- Body: JSON object containing user details (username, password)
- Response: HTTP 200 for the user credentials

### Login

- Endpoint: `POST api/login/`
- Body: JSON object containing user details ( username, password)
  - ``{
"username": "test",
"password": "test"
}``
- Response: access_token and refresh_token.
- Save this access_token for subsequent requests. 

## Workouts and Exercises

### Workout Management

#### Create and Exercise:
- Endpoint: `POST /exercise`
- Body: JSON object containing workout plan details (e.g., name, description)
- Response: JSON object containing the created workout plan

#### Create a Workout Plan

- Endpoint: `POST /workouts`
- Body: JSON object containing workout plan details (e.g., name, description)
- Response: JSON object containing the created workout plan

#### Add an Exercise to a Workout Plan

- Endpoint: `POST /workouts/{workout_id}/exercises`
- Path Parameters:
  - `workout_id`: ID of the workout plan to which the exercise will be added
- Body: JSON object containing exercise details (e.g., name, sets, reps)
- Response: JSON object containing the updated workout plan with the added exercise

#### Add Multiple Exercises to a Workout Plan

- Endpoint: `POST /workouts/{workout_id}/exercises/bulk`
- Path Parameters:
  - `workout_id`: ID of the workout plan to which the exercises will be added
- Body: JSON array containing JSON objects of exercise details (e.g., name, sets, reps)
- Response: JSON object containing the updated workout plan with the added exercises

### Exercise Management

#### Create an Exercise

- Endpoint: `POST /exercises`
- Body: JSON object containing exercise details (e.g., name, description, target muscles)
- Response: JSON object containing the created exercise

## Weight Logs and Fitness Goals

### Weight Logs

#### Add Weight Logs for Yourself

- Endpoint: `POST /weightlogs`
- Body: JSON object containing weight log details (e.g., date, weight)
- Response: JSON object containing the added weight log entry

### Fitness Goals

#### Create a Fitness Goal for Yourself

- Endpoint: `POST /fitnessgoals`
- Body: JSON object containing fitness goal details (e.g., type, target, timeframe)
- Response: JSON object containing the created fitness goal

#### View Fitness Goal Progress

- Endpoint: `GET /fitnessgoals/{goal_id}/progress`
- Path Parameters:
  - `goal_id`: ID of the fitness goal
- Response: JSON object containing progress towards the fitness goal

#### Add an Exercise to a Workout Plan

- Endpoint

**POST** `/workouts/{workout_id}/exercises`

 - Path Parameters

- `workout_id`: ID of the workout plan to which the exercise will be added.

### Body

A JSON object containing the details of the exercise you want to add. For example:

```json
{
  "name": "Push Ups",
  "sets": 3,
  "reps": 12
}
```
### Description

To add an exercise to a workout plan, send a POST request to the /workouts/{workout_id}/exercises endpoint with the workout_id in the path and the exercise details in the request body. The request should be authenticated, as indicated by the IsAuthenticated permission class in the WorkoutPlanViewSet.

The backend functionality for adding an exercise is encapsulated within the WorkoutPlanViewSet, a subclass of viewsets.ModelViewSet. This viewset is configured to use WorkoutPlanExerciseSerializer for serializing data and requires users to be authenticated.

Upon receiving the request, the system will validate the input against the expected schema and, if valid, proceed to add the exercise to the specified workout plan. It's important to ensure that the workout_id corresponds to an existing workout plan. The operation concludes by returning a JSON object representing the updated workout plan, including the newly added exercise.

This operation is distinct from the update_progress action, which is designed to update the completion status of exercises within a workout plan based on the number of sets and reps completed. The code snippet provided earlier demonstrates the handling of progress updates rather than the addition of new exercises.

## Conclusion

This concludes the Fitness API documentation. If you have any questions or need further assistance, please contact me. Happy exercising!
