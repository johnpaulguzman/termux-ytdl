# termux-ytdl
Utility tool for youtube-dl + Termux

## Installation:
- Install Termux and Termux:API from the app store
- Open Termux, and enter `bash <(curl --silent https://raw.githubusercontent.com/johnpaulguzman/termux-ytdl/master/setup.sh)`

## Notes:
- Make sure you enable the scanning of media files that are hidden by `.nomedia`. In MX Player, this is under (Settings > List > Scan > Recognize .nomedia)
- Metaconfig options:
  - storage: can be internal or external
  - directory: can be any valid directory name
  - resolution: 
    - can be a number: the max value of the video height (e.g., 720 for 720p quality), and this takes the best quality that is less than or equal to the specified max value
    - can be a string: like "best" or some [selected format](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#format-selection)

## Usage (via share):
- Share a page or its link to Termux

## Usage (via copied link):
- Copy a link to your clipboard
- Open Termux, and enter `/bin/termux-url-opener` or `bash ~/bin/termux-url-opener`

## References:
- [Documentation](https://github.com/ytdl-org/youtube-dl/blob/master/README.md)
- [Main options](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/YoutubeDL.py)
- [Downloader options](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/downloader/common.py)
