from views import db
from models import Task
from datetime import date

#
# Create the database and the table
#
db.create_all()
#
# Insert some data
#
db.session.add(Task("Finish this tutorial", date(2015, 3, 13), 10, 1))
db.session.add(Task("Finish Real Python", date(2015, 3, 13), 10, 1))
#
# Commit the changes
#
db.session.commit()
