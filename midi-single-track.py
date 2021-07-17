from mido import MidiFile
import sys
import subprocess

mid = MidiFile(sys.argv[1])
emptyTracks = []

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

if len(mid.tracks) == 3:
    print("Only 1 track now")
newMidiFileName = f"{sys.argv[1][:-4]}_converted.mid"
mid.save(newMidiFileName)
subprocess.Popen(
    f"E:\EDIROL\SD-20 MIDI File Converter\Midi2Wav.exe \"{newMidiFileName}\"")
