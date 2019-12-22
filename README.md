# Offline Transcription

Use pocketsphinx to do speech to text transcription right on your local machine!

## Install from source
Download the repository, create a virtual environment, package into an executable and copy to your PATH.  Mac/Linux instructions below; Windows instructions are the same except for running pyinstaller and adding the produced executable to path.

```
git clone https://github.com/aayc/offline-transcription
cd offline-transcription
python3 -m venv env
source env/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
sh build.sh
cp dist/transcribe /usr/local/bin/
```

## Usage
From executable:

```
transcribe <input_file>.(mp3|wav|m4a|etc.) --output <output_file>.txt
transcribe my_podcast.mp3 --output my_podcast.txt
```
