# -------------------------------------------------------------------------------------------------------------------
# Author                       Version          Created_Date              JIRA                 Description
# {{cookiecutter.author}}                    V1.0           2022-03-13             {{cookiecutter.jira_story_nbr}}      {{cookiecutter.project_description}}
# -------------------------------------------------------------------------------------------------------------------

BIN=venv/bin/

all : clean venv
.PHONY : all


clean :
	@clear
	@echo "===========================================STAGE 1=========================================================="
	@rm -rf venv
	@echo "removed venv (if exists)"
	@echo "Cleaning completed"
	@echo "\n\n"

venv :
	@echo "===========================================STAGE 2=========================================================="
	@echo "Python Env=`python --version`"
	@echo "Installing Venv"
	@python -m venv venv
	@$(BIN)pip install -r requirements.txt
	@echo "Successfully Installed venv & requirements for the project. Happy Coding!!!"
	@echo "\n\n"

