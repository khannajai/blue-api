# API for Blue Harvest
See `task_specification.md` for more details.

## Setup and run the Backend API manually

Follow the steps below if you want to install requirements and run the app manually.

1. Install `virtualenv` and activate it the environment:
```
pip install virtualenv
pip install --upgrade virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

To deactivate the environment:
```
deactivate
```

2. Install required packages
```
pip install -r requirements.txt
```

## Run swagger UI to test API and make requests
```
python app/app.py
```

## Run unit tests
```
python app/test_blue_api.py
```
This will run a development server and make the test requests. To exit the server and see the test results, press `Ctrl-C`