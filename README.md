# 🎬 YouTube Playlist Duration Calculator

This Python script calculates the **total duration** of a YouTube playlist by summing the durations of all its videos using the YouTube Data API v3.

## 🚀 Features

- Accepts a YouTube playlist **ID** or full **URL**
- Handles playlists of any length via **pagination**
- Outputs total duration in `HH:MM:SS` format

## 🧰 Requirements

- Python 3.6+
- [Google API Python Client](https://github.com/googleapis/google-api-python-client)
- A valid **YouTube Data API v3 key**

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/yt-playlist-duration.git
   cd yt-playlist-duration
   ```
2. Recreate the environment from requirements.txt using setup.sh(For Linux) or setup.bat(For Windows)

```bash
./setup.sh # or bat setup.bat 
source yt_timer_env/bin/activate  # Activate the environment (Linux/macOS)
venv\Scripts\activate  # Activate the environment (Windows)
```
3. Generate a Youtube Data API Key
If you dont know how to generate a YouTube Data API v3 key, you can visit [this site](https://docs.themeum.com/tutor-lms/tutorials/get-youtube-api-key/https://docs.themeum.com/tutor-lms/tutorials/get-youtube-api-key/)

4. Set the API key as an environment variable
To set the API key as an environment variable, you can export it (recommended)

    ```bash
    echo 'export YT_KEY="Your YouTube API Key"' >> ~/.bashrc
    ```
Or modify the API Key in the script directly (Not recommended)

## 🧪 Usage
- Run the script by passing a YouTube playlist ID or a full playlist URL as an argument:

    ```bash
    python3 playlist_duration.py [PLAYLIST_ID or URL]
    ```

#### Example 1: Using a Playlist ID

```bash
python3 playlist_duration.py PLynWqC6VC9_vgM1PKHjvHjX7g9cT96i4B
```

#### Ex 2: Using an entire youtube playlist URL
```bash
python3 playlist_duration.py "https://www.youtube.com/playlist?list=PLynWqC6VC9_vgM1PKHjvHjX7g9cT96i4B"
```

#### Ex 3: With no Arguments
```bash
python3 playlist_duration.py
```
- The script prompts you to enter a playlist ID or URL
```bash
Enter a playlist ID:
```

## Output
- The total duration of the playlist is printed in the format ```[Playlist Name] ~ HH:MM:SS```

## 🙋 FAQ
Q: Can I use this with private playlists?
A: No. The YouTube Data API only works with public playlists.

Q: What happens to unavailable videos?
A: They are skipped and not included in the total duration.
