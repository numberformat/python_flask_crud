# CRUD application

Manage a list of employees. Add, Edit, Delete.

## Step by step Instructions

Check the commit log for a step by step guide on how to create this application.

## Libraries

* Bootstrap via a CDN <https://getbootstrap.com/>
* Standard form submission (no rest API)

## Prerequisites

Ensure you have Python 3.11 installed on your system. This project uses a Conda environment, but you can also use a virtual environment of your choice.

## Environment Setup

1. **Create and activate a Conda environment:**

    ```sh
    conda create --name flask_login python=3.11
    conda activate flask_login
    ```

2. **Install required packages:**

    ```sh
    pip install Flask python-dotenv
    ```

## Installation

Follow these steps to set up the project:

**Clone the repository** to your local machine.

After checking out the project and creating the virtual or conda environment, run the following to create the schema.

Enter your python shell and type the following to create the sqlite database in the instance/ directory.

```sh
from App import db, app
with app.app_context():
    db.create_all()
```

This will create the SQLite database in the `instance/` directory.

Test it by running sqlite3 instance/database.db and type ".tables". It should show the user table. ".exit" to exit.

## How to run

```sh
# cd to the same directory as the crud folder and execute:
flask run
```

## Reference

* <https://www.youtube.com/watch?v=XTpLbBJTOM4>
* Python Website Full Tutorial - Flask, Authentication, Databases & More <https://www.youtube.com/watch?v=dam0GPOAvVI>
