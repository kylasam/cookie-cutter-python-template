# cookiecutter-python and Docker

This repository is Data Infrastructure team's implementation to get you fully started with your shiny new dockerized python project!

## What is it?

A ready-made template for a standard docker or python project which contains the following:

- A sample python project
- Docker code block
- venv setup


## Quickstart

```shell
# Enter directory to house the newly created project
cd <target_directory>

# Install cookiecutter
pip install cookiecutter

# Run cookiecutter to create your project
cookiecutter gutter.git

# Enter project directory
cd <project_name>

# Env setup
make 

# Initialise, add, and commit newly created project files
git init 
git add --all
git commit -m "initial commit"

# Add remote of the project
git remote add origin <REMOTE_URL> 

# Push to the new repo!
git push -u origin master
```
