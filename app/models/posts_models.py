import datetime
import pymongo
from bson.objectid import ObjectId


client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["kenzie"]

class Posts:
    def __init__(self, *args, **kwargs) -> None:
        self.title = kwargs["title"]
        self.authon = kwargs["author"]
        self.tags = kwargs["tags"]
        self.content = kwargs["content"]
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
        id_list = []
        for post in list(db.posts.find()):
            id_list.append(post['id'])
        self.id = 1 if len(id_list) == 0 else max(id_list) + 1

    def post_posts(self):
        db.get_collection("posts").insert_one(self.__dict__)
    
    @staticmethod
    def serialize_posts(data):
        if type(data) is list:
            for post in data:
                post.update({"_id": str(post["_id"])})
        elif type(data) is Posts:
            data._id = str(data._id)
        elif type(data) is dict:
            data.update({"_id": str(data["_id"])})
        
    
    @staticmethod
    def patch_posts(id: int, **kwargs) -> None:
        update_date = datetime.datetime.now().isoformat()
        kwargs.update({"updated_at": update_date})
        return db.get_collection("posts").find_one_and_update({"id": id}, {"$set":kwargs})

    
    @staticmethod
    def get_posts(id: int = None) -> list:
        if id:
            return db.get_collection("posts").find({"id": id})
        else:
            return db.get_collection("posts").find()

    @staticmethod
    def delete_posts(id: int):
        return db.get_collection("posts").find_one_and_delete({"id": id})

        