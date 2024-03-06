import os

from googleapiclient.discovery import build


class Video:
    api_key = os.getenv('YOUTUBE_API_KEY')

    def __init__(self, video_id: str):
        try:
            self.video_id = video_id
        except self.video_response() is not None:
            self.title = self.video_response()['items'][0]['snippet']['title']
            self.description = self.video_response()['items'][0]['snippet']['description']
            self.url = f'https://www.youtube.com/watch?v={self.video_id}'
            self.view_count = self.video_response()['items'][0]['statistics']['viewCount']
            self.like_count = self.video_response()['items'][0]['statistics']['likeCount']
            self.comment_count = self.video_response()['items'][0]['statistics']['commentCount']
        else:
            self.title = None
            self.description = None
            self.url = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None

    def __str__(self):
        return self.title

    def get_service(self):
        return build('youtube', 'v3', developerKey=self.api_key)

    def video_response(self) -> dict:
        if self._video is None:
            self._video = self.get_service().videos().list(
                part='snippet,statistics',
                id=self.video_id
            ).execute()
        return self._video


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.video_title = self.title
        self.video_url = self.url
        self.video_view_count = self.view_count
        self.video_like_count = self.like_count
        self.playlist_id = playlist_id
        self._video = None
        self.playlist_title = self.get_service().playlists().list(
        )
