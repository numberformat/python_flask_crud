# Create a CRUD application

Libraries

* Bootstrap <https://getbootstrap.com/>
* Standard form submission (no rest API)

## Installation

After checking out the project and creating the virtual or conda environment, run the following to create the schema.

Enter your python shell and type the following to create the sqlite database in the instance/ directory.

```sh
from App import db, app
with app.app_context():
    db.create_all()
```

## Reference

* <https://www.youtube.com/watch?v=XTpLbBJTOM4>
* Python Website Full Tutorial - Flask, Authentication, Databases & More <https://www.youtube.com/watch?v=dam0GPOAvVI>
