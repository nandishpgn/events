from fastapi import FastAPI
from config.database import get_database, sqlalchemy_engine, database
from models.api_logs import metadata, posts
from routes.routes import router as post_router


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(sqlalchemy_engine)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

metadata.create_all(sqlalchemy_engine)
app.include_router(post_router)

# # # @validator("event_date")
# def valid_created_date(event_date):
#         delta=datetime.now()
#         # verify_date=delta.strftime("%d/%m/%y")
#         verify_date=delta.strftime("%m/%d/%y")
#         datetime_object = datetime.strptime(verify_date, '%m/%d/%y ')
#         print(type(datetime_object))
#         print(verify_date, type(verify_date))
#         print(event_date,type(event_date))
#         print(delta,type(delta))
#         if event_date>verify_date:
#             return True
#         elif event_date==verify_date:
#             return "in progress"
#         else:
#             return False

# @validator("created_date")        
# def valid_date(self):
#     delta=datetime.today()
#     self.created_date<delta
#     print("you cannot register")
            

       
    
# @root_validator()
# def date_time(cls,values):
#         created_date = values.get("created_date")
#         updated_date = values.get("updated_date")

#         if created_date>datetime:
#             raise ValueError("you can register")
        
#         elif  created_date<datetime:
#             # print()
#             raise ValueError("event date passed")
       
#         else:
#              return values
# def sort_event_date(event_date):
#     for date in event_date:
                    


