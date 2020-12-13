import webbrowser as wb

from meeting_list import MEETING_LIST
from zoom_uri import ZoomURI


def join(command):
    if 'id' not in command.kwargs:
        print('please specify the zoom id!')
        return
    uri = ZoomURI.join(
        command.kwargs['id'],
        command.kwargs.get('pwd', None),
        command.kwargs.get('uname', None))
    wb.open(uri, new=2)


def join_by_name(command):
    if len(command.values) == 0:
        print('please specify the name of the meeting!')
        return
    # search and display the results
    results = MEETING_LIST.get_meetings_by_name(command.values[0])
    print(f'Number of results found: {len(results)}')
    if len(results) == 0:
        return

    # select a choice
    if len(results) == 1:
        print(f'id={results[0].zoom_id}, pwd={results[0].pwd}')
        choice = 0
    else:
        for i, result in enumerate(results):
            print(f'{i}: id={result.zoom_id}, pwd={result.pwd}')
        choice = None
        while choice is None:
            try:
                choice = int(input('Which one do you want to choose? (input the index) '))
            except ValueError:
                choice = None
                continue
            if not 0 <= choice < len(results):
                choice = None
    meeting = results[choice]

    # join zoom meeting
    uri = ZoomURI.join(
        meeting.zoom_id,
        meeting.pwd,
        command.kwargs.get('uname', None))
    wb.open(uri, new=2)


def quit_(command):
    print('Bye')
    quit()
