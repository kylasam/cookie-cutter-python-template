#!/usr/bin/env python3

# -------------------------------------------------------------------------------------------------------------------
# Author                       Version          Created_Date              JIRA                 Description
# {{cookiecutter.author}}                    V1.0           2022-03-13             {{cookiecutter.jira_story_nbr}}      {{cookiecutter.project_description}}
# -------------------------------------------------------------------------------------------------------------------
import logging
from datetime import datetime
import os
import sys

SCRIPT_NAME = os.path.basename(sys.argv[0])
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
GLOBAL_CONFIG_DIR = os.path.join(CURRENT_DIR, 'config')
CURRENT_DATE = datetime.now().strftime('%Y%m%d')
LOG_FILE_NAME = datetime.now().strftime('/logs/' + SCRIPT_NAME + '_%Y%m%d%H%M%S.log')
logging.basicConfig(filename=LOG_FILE_NAME,
                    format='%(levelname)s::%(asctime)s.%(msecs)03d  From Module = ":%(funcName)s:" Message=> %(message)s.',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
logging.info("Code Execution started now!")


def main():
    logging.info("Data processing for begins...")


if __name__ == '__main__':
    logging.info("Calling the main function...")
    main()
