import json
import os


class Meeting:
    def __init__(self, name, zoom_id, pwd):
        self.name = name
        self.zoom_id = zoom_id
        self.pwd = pwd


class MeetingList:
    def __init__(self, path='./resources/meetings.json'):
        self.path = os.path.abspath(path)
        self.meetings = json.load(open(self.path, 'r'))

    def _get(self, meeting):
        return Meeting(meeting['name'], meeting['zoom_id'], meeting['pwd'])

    def get(self, index):
        return self._get(self.meetings[index])

    def get_meetings_by_name(self, name):
        return [self._get(meeting) for meeting in self.meetings if meeting['name'] == name]

    def add(self, name, zoom_id, pwd):
        self.meetings.append({'name': name, 'zoom_id': zoom_id, 'pwd': pwd})

    def save(self):
        json.dump(self.meetings, open(self.path, 'w'), indent='    ')


MEETING_LIST = MeetingList()
