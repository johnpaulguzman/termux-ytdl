from youtube_dl import YoutubeDL

import json
import os
import sys
import traceback

urls = sys.argv[1: ]
script_dir = os.path.dirname(os.path.realpath(__file__))
metaconfig_path = os.path.join(script_dir, "metaconfig.json")
config_path = os.path.join(script_dir, "config.json")
json_kwargs = {'indent': 4}

def load_json(path, verbose=False):
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    if verbose:
        print(f"Loaded {path}: {json.dumps(data, **json_kwargs)}")
    return data

def update_metaconfig(metaconfig):  # in-place
    do_update = input("\nUpdate metaconfig? (y - yes; blank - no): ")
    if do_update != "y":
        return
    for key in metaconfig.keys():
        value = input(f"\nCurrent value for [{key}] is [{metaconfig[key]}].\nEnter a new value or blank to keep the current value: ")
        if value == "":
            continue
        metaconfig[key] = value
    with open(metaconfig_path, 'w') as json_file:
        json.dump(metaconfig, json_file, **json_kwargs)
    print(f"Updated metaconfig: {json.dumps(metaconfig, **json_kwargs)}")

def generate_config(metaconfig):
    config_json = load_json(config_path)
    _format = f"best[height={metaconfig['resolution']}]/bestvideo[height<={metaconfig['resolution']}]+bestaudio/best" if metaconfig['resolution'].isnumeric() else metaconfig['resolution']
    root_dir = "~/storage/shared" if metaconfig['storage'] == 'internal' else "~/storage/external-1"
    abs_dir = os.path.join(root_dir, metaconfig['directory'])
    _outtmpl = os.path.join(abs_dir, "%(title)s.%(ext)s")
    config = {
        'format': _format,
        'outtmpl': _outtmpl,
        **config_json
    }
    print(f"Loaded config: {json.dumps(config, **json_kwargs)}")
    return config

if __name__ == '__main__':
    try:
        metaconfig = load_json(metaconfig_path, verbose=True)
        update_metaconfig(metaconfig)
        config = generate_config(metaconfig)
        with YoutubeDL(config) as ytdl:
            ytdl.download(urls)
    except Exception as e:
        print(f"Exception: {e}")
        traceback.print_exc()
        sys.exit(1)
