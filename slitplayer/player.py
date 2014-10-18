import midi
from PIL import Image
from sys import argv

notes = [midi.B_3, midi.C_4, midi.D_4, midi.E_4, midi.F_4, midi.G_4, midi.A_4, midi.B_4, midi.C_5]
# Ticks per pixel
tpp = 100

channel = 0
instrument = 101

sheet = Image.open(argv[1])
size = sheet.size
pixels = sheet.load()

pattern = midi.Pattern()
track = midi.Track()
track.append(midi.ProgramChangeEvent(value=instrument, channel=channel));

state = [0 for x in range(size[1])]
tick = 1000
for x in range(size[0]):
	for y in range(size[1]):
		note = notes[-(y + 1)]
		if pixels[x,y][0] < 100:
			print x, y, state[y]
			if state[y] == 0:
				track.append(midi.NoteOnEvent(tick=tick, velocity=50, pitch=note, channel=channel))
				tick = 0
				state[y] = 1
		elif state[y] == 1:
			track.append(midi.NoteOffEvent(tick=tick, velocity=50, pitch=note, channel=channel))
			tick = 0
			state[y] = 0
	tick = tpp

pattern.append(track)
print pattern

midi.write_midifile("output.mid", pattern)
