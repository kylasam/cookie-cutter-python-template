# -------------------------------------------------------------------------------------------------------------------
# Author                       Version          Created_Date              JIRA                 Description
# {{cookiecutter.author}}                    V1.0           2022-03-13             {{cookiecutter.jira_story_nbr}}      {{cookiecutter.project_description}}
# -------------------------------------------------------------------------------------------------------------------

FROM python:3.8.12-slim-buster

LABEL maintainer={{cookiecutter.author}}

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install g++ -y \
    && apt-get install git -y \
    && apt-get install jq moreutils libpq-dev -y \
    && apt-get clean \

WORKDIR /app
COPY src/* /app/*
COPY requirements.txt .

RUN pip install --disable-pip-version-check -r /requirements.txt && rm -rf /var/lib/apt/lists/*


ENTRYPOINT ["bash", "-c", "sleep infinity"]



