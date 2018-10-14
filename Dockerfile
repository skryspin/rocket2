FROM python:3.7

# Set up working directory
WORKDIR /app

# Copy everything into working directory
COPY . /app

# Install everything
RUN pip install pipenv
RUN pipenv install

# We don't have anything to run yet, so we'll run the tests
CMD ["pipenv", "run", "pytest", "tests/"]
