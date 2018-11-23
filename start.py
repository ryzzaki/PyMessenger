import json
from datetime import datetime

class Snail:
    def __init__(self):
        self.sender = ""
        self.message_array = []
        self.me_count = 0
        self.sender_count = 0
        self.clean_messages =[
                {
                    "sender": "",
                    "human_date": "",
                    "week_day": "",
                },
            ]

    def load_json_pls(self):
        self.sender = input('Enter the name of the person: ')
        path = "facebook-ngvtcng/messages/inbox/" + self.sender + '/message.json'
        with open(path) as f:
            self.message_array = json.load(f)
    
    def count_messages_include_old_acc(self):
        for msg in self.message_array['messages']:
            if (msg['sender_name'] == "Cuong Nguyen") or (msg['sender_name'] == "Facebook User"):
                self.me_count = self.me_count + 1
            else:
                self.sender_count = self.sender_count + 1

    def count_messages(self):
        for msg in self.message_array['messages']:
            if (msg['sender_name'] == "Cuong Nguyen"):
                self.me_count = self.me_count + 1
            else:
                self.sender_count = self.sender_count + 1
    
    def simple_count_results(self):
        print('\nYour number of messages sent: ' + str(self.me_count))
        print(self.sender + "'s number of messages sent: " + str(self.sender_count))
        print('\nTotal count of messages in this inbox: ' + str(self.me_count + self.sender_count))
    
    def test_read_json(self):
        print(self.message_array)

    def test_data_grab(self):
        # print(self.message_array['messages'])
        print(self.message_array['messages'][0]['content']) # syntax is working

    def test_convert_time(self):
        unix_time = int(self.message_array['messages'][0]['timestamp_ms']) / 1000 # divide by 1000 (ms)
        human_time = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d')
        print(human_time)

if __name__ == "__main__":
    sn = Snail()
    sn.load_json_pls()
    # sn.test_read_json()
    # sn.test_data_grab()
    sn.count_messages()
    sn.simple_count_results()
    sn.test_convert_time()