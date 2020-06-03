import datetime
import json


class JsonObject:
    ''' Constructing Day, Hour, and Minute attributes.
        Default value will be the present Day, Hour and Minute.
    '''
    def __init__(self,
                 day='today',
                 hour=datetime.datetime.now().hour,
                 minute=datetime.datetime.now().minute
                 ):
        self.day = day
        self.hour = hour
        self.minute = minute

    def write_to(self, file):
        """ Store Day, Hour, and Minute in Json file.
        :argument
            :file :- The file to write data in or read data from.
        """
        # Create key value pairs
        data = {
            "day": self.day,
            "hour": self.hour,
            "minute": self.minute,
        }

        # Serialize the key value pairs
        json_data = json.dumps(data)

        # Write json data to a file
        with open(file, 'w') as f:
            f.write(json_data)

    def read_from(self, file):
        with open(file, 'r') as data:
            return json.loads(data.read())


if __name__ == '__main__':
    print('\nTesting Program: \n ')
    # Write to Json
    obj = JsonObject(day='today', hour=10, minute=23)
    obj.write_to('test.json')

    # Read From Json
    obj = JsonObject().read_from('test.json')
    print(obj)
    print(obj['day'], obj['hour'], obj['minute'])
