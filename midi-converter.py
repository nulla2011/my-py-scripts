from mido import MidiFile
import sys
import subprocess
import re
import os

mid = MidiFile(sys.argv[1])
ticksPerBeat = mid.ticks_per_beat
emptyTracks = []
headerTracks = [mid.tracks[0], mid.tracks[1]]
converterPath = "E:\EDIROL\SD-20 MIDI File Converter\Midi2Wav.exe"

for i in range(2, len(mid.tracks)):  #前两轨是控制拍号bpm的
    track = mid.tracks[i]
    isEmpty = True
    for message in track:
        if message.type == 'note_on':
            isEmpty = False
            break
    if isEmpty:
        emptyTracks.append(track)
for track in emptyTracks:
    mid.tracks.remove(track)

trackNames = []
for i in range(2, len(mid.tracks)):
    trackNames.append(mid.tracks[i].name)
if len(trackNames) == 1:
    print("only 1 tracks, converting")
    items = [0]
else:
    print(f"Now available tracks:\n")
    for i, n in enumerate(trackNames):
        print(f"{i} ---- {n}")
    input = input(
        "Input tracks you want to convert(just press enter to convert all tracks): "
    )
    if input == "":
        items = list(range(0, len(mid.tracks) - 2))
    else:
        items = re.split('[ ,]', input)
for item in items:
    try:
        n = int(item)
    except Exception:
        print("Illegal Number")
        os.system("pause")
        sys.exit()
    newMid = MidiFile()
    newMid.ticks_per_beat = ticksPerBeat
    newMid.tracks.append(headerTracks[0])
    newMid.tracks.append(headerTracks[1])
    newMid.tracks.append(mid.tracks[int(n) + 2])
    newMidiFileName = f"{sys.argv[1][:-4]}_{trackNames[int(n)]}.mid"
    newMid.save(newMidiFileName)
    P = subprocess.Popen(f"{converterPath} \"{newMidiFileName}\"")
    P.wait()
