---
title: "Play a playlist every day"
tags: [draft, automation, macOS, VLC, how-to]
---



I'd like to play a playlist of videos every day. 



## Tools

- Operating system: MacOS
- Video player: VLC
- Video downloader: YT-DLP
  - Mac Homebrew
- Terminal
  - `cron` / `crontab -e`



## Process

### Download videos to your computer using `yt-dlp`

```
cd ~/_Routines/Daily/Morning Video/(Folder for Videos)

# Ensure YT-DLP is up to date
brew upgrade yt-dlp

# Download each video file locally
yt-dlp (video options) "(Video URL)"

# Open this folder in Finder
open .
```

### Open VLC, and videos to playlist

- Open VLC.app
- Drag files from Video folder into VLC
- Save as Playlist (M3)
  - Save it in your Video Folder

Test the videos out

- Open the Playlist file
  - Ensure it opens with VLC
  - Ensure it plays videos. Check
    - Sound OK?
    - Sound device correct?
    - Set to Random?
    - Set to Loop?

## Automate it

- Review Cron / Crontab documentation
  - (Resources)
- Open Terminal
- Show currently scheduled jobs: `crontab -l` (lower-case L)
- Review `vim` documentation
  - (Guide to `vim` text editor)
  - (Quick reference / cheat sheet to `vim` text editor)
- Run `crontab -e` to edit



Example: 

"Every day at 20:00 (8 PM), open VLC video player and play Learn Blues Piano Improvisation playlist"

```
# Practice Piano every day at 8pm
0 20 * * * open -a /Applications/Video/VLC.app /Users/jro/JRO-Sync/_Routines/DAY/learn-blues-improvisation-piano.m3u
```



Test it

```
# TEST: Display a pop-up at 11:15 AM
15 11 * * * osascript -e 'display notification "Cron job ran" with title "Cron Job"'
```







