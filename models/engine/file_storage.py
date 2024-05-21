#!!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    """
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        """
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        """
        serialized_obj = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                json_file = json.load(file)
                for key, value in json_file.items():
                    class_name, obj_id = key.split(',')
                    module = __import__('models', + class_name, fromlist=[class_name])
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except Exception:
            pass
