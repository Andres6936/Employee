### Screenshot

<p align="center">
    <img src="./Docs/Home.png" alt="Home" width="40%">
</p>

### How to run

This project uses Pipenv to manage its Python dependencies.
Pipenv is a tool that helps you to install, manage, and deploy Python packages.
It also creates and manages virtual environments for your projects.

To install Pipenv, you can run the following command:

`pip install pipenv`

Once you have installed Pipenv, you can initialize a new project by running the following command:

`pipenv install`

This will create a new Pipfile and Pipfile.lock file in your project directory.
The Pipfile contains a list of the dependencies for your project, and the
Pipfile.lock file contains the specific versions of those dependencies that
have been installed.

Once you have installed the dependencies for your project, you can run it by
activating the virtual environment and then running the main script:

`pipenv shell`
`python __main__.py`