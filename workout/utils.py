import requests

YOUTUBE_API_KEY = 'AIzaSyCpdHRTK-bbF9MR4fwdAn3g40aqj7jgWc4'

def search_youtube_videos(query, max_results=12):
    search_url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'key': YOUTUBE_API_KEY,
        'maxResults': max_results,
        'videoEmbeddable': 'true',
    }

    response = requests.get(search_url, params=params)
    results = []

    if response.status_code == 200:
        data = response.json()
        for item in data.get('items', []):
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnail = item['snippet']['thumbnails']['medium']['url']

            results.append({
                'video_id': video_id,
                'title': title,
                'description': description,
                'thumbnail': thumbnail,
                'embed_url': f'https://www.youtube.com/embed/{video_id}',
            })
    else:
        print("YouTube API Error:", response.status_code, response.text)

    return results
