docker build -t tests .
docker run --name tests_run  tests pytest --browser="chrome"
docker cp tests_run:/app/allure-results .
allure serve allure-results
docker rm tests_run