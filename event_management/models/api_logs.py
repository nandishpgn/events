import sqlalchemy

metadata = sqlalchemy.MetaData()
posts = sqlalchemy.Table(
    "event",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("event_name", sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column("event_date",sqlalchemy.DateTime(), nullable=True),
    # sqlalchemy.Column("event_time",sqlalchemy.Time(), nullable=True),
    sqlalchemy.Column("location",sqlalchemy.String(length=100), nullable=True),
    sqlalchemy.Column("event_organiser", sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column("chief_guest", sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column("total_guests", sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime()),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime())
    



)
#     sqlalchemy.Column("title", sqlalchemy.String(length=255), nullable=False),
#     sqlalchemy.Column("content", sqlalchemy.Text(), nullable=False),

