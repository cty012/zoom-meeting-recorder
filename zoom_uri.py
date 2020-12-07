class ZoomURI:
    join_str = ['zoommtg://zoom.us/join?confno={}', '&pwd={}', '&zc={}', '&uname={}']
    # start_str = 'zoommtg://zoom.us/start?confno={}&zc={}&uname={}'

    @classmethod
    def join(cls, zoom_id, pwd, username):
        uri = cls.join_str[0].format(zoom_id)
        if pwd is not None:
            uri += cls.join_str[1].format(pwd)
        uri += cls.join_str[2].format(0)
        if username is not None:
            uri += cls.join_str[3].format(username)
        return uri
