"""

"""
# ------------------------------------------------------- #
#                     imports
# ------------------------------------------------------- #
from invoke import task

# ------------------------------------------------------- #
#                   definitions
# ------------------------------------------------------- #
VIRTUALENV_NAME = "py310_AniWorldScraper"

# ------------------------------------------------------- #
#                   global variables
# ------------------------------------------------------- #


# ------------------------------------------------------- #
#                      functions
# ------------------------------------------------------- #
def _update_requirements_txt(c):
    c.run("pip freeze > requirements.txt")

# ------------------------------------------------------- #
#                      classes
# ------------------------------------------------------- #


# ------------------------------------------------------- #
#                       tasks
# ------------------------------------------------------- #
@task
def update_requirements(c):
    with c.prefix("workon {}".format(VIRTUALENV_NAME)):
        _update_requirements_txt(c)
