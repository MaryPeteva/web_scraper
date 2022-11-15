import json
from defines_json import JSON_FILE

class ReadJson():
    key_search = "title"

    def check_title_json_file(self, titles, dir= JSON_FILE):
        """
            Read Json file and search for given title in it
            param: title,
            param: dir(optional).
        """
        json_file = json.loads(open(dir).read())
        
        for item in json_file:
            for title in titles:
                if title.lower() in item[self.key_search].lower():
                    print(item)
