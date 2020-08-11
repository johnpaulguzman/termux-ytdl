# Run as: bash <(curl --silent https://raw.githubusercontent.com/johnpaulguzman/termux-ytdl/master/setup.sh)
set -e
pkg install -y python ffmpeg termux-api
pip install -U youtube-dl
mkdir ~/bin
curl --silent https://raw.githubusercontent.com/johnpaulguzman/termux-ytdl/master/termux-url-opener > ~/bin/termux-url-opener
curl --silent https://raw.githubusercontent.com/johnpaulguzman/termux-ytdl/master/ytdl.py > ~/bin/ytdl.py
curl --silent https://raw.githubusercontent.com/johnpaulguzman/termux-ytdl/master/metaconfig.json > ~/bin/metaconfig.json
curl --silent https://raw.githubusercontent.com/johnpaulguzman/termux-ytdl/master/config.json > ~/bin/config.json

chmod +x ~/bin/termux-url-opener
termux-setup-storage
echo "SUCCESS"
