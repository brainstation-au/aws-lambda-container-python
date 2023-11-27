FROM python:3.10-buster as local

ENV CODE=/opt/code
WORKDIR ${CODE}

ENV VENV_PATH="${CODE}/.venv"
ENV PATH="${VENV_PATH}/bin:${PATH}"

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

FROM public.ecr.aws/lambda/python:3.11 as lambda

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

# Copy requirements.txt
COPY poetry.lock pyproject.toml ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN poetry install --no-root

# Copy function code
COPY src ${LAMBDA_TASK_ROOT}/src

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
# CMD [ "lambda_function.handler" ]
