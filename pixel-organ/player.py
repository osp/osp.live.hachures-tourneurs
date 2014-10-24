import argparse
import midi
from PIL import Image

parser = argparse.ArgumentParser(description="")
parser.add_argument('file', help='Path to the file you would like to play')
parser.add_argument('-o', '--out-file', dest='out', type=str, default=False, help='Path to the output, by default it\'s the [inputfile].mid')
parser.add_argument('-i', '--instrument', dest='instrument', type=int, default=0, help='Integer defining the instrument range: 0 -> 127. Default 0 (Grand Piano)')
parser.add_argument('-t', '--ticks', dest='ticks', type=int, default=40, help='Integer defining the amount of ticks it takes to play one pixel. The greater the amount of ticks per pixel the longer it plays. Default 100')
parser.add_argument('-c', '--channel', dest='channel', type=int, default=0, help='Integer defining the channel the notes are written to')
parser.add_argument('-v', '--velocity', dest='velocity', type=int, default=100, help='Integer defining the velocity')

args = parser.parse_args()

input_file = args.file
output_file = "{0}.mid".format(args.file) if args.out == False else args.out
instrument = args.instrument
tpp = args.ticks
channel = args.channel
velocity = args.velocity

# List of available notes
notes = [midi.C_1,midi.D_1,midi.E_1,midi.F_1,midi.G_1,midi.A_1,midi.B_1,midi.C_2,midi.D_2,midi.E_2,midi.F_2,midi.G_2,midi.A_2,midi.B_2,midi.C_3,midi.D_3,midi.E_3,midi.F_3,midi.G_3,midi.A_3,midi.B_3,midi.C_4,midi.D_4,midi.E_4,midi.F_4,midi.G_4,midi.A_4,midi.B_4,midi.C_5,midi.D_5,midi.E_5,midi.F_5,midi.G_5,midi.A_5,midi.B_5,midi.C_6,midi.D_6,midi.E_6,midi.F_6,midi.G_6,midi.A_6,midi.B_6,midi.C_7,midi.D_7,midi.E_7,midi.F_7,midi.G_7,midi.A_7,midi.B_7,midi.C_8,midi.D_8,midi.E_8,midi.F_8,midi.G_8,midi.A_8,midi.B_8]

sheet = Image.open(input_file)
size = sheet.size
pixels = sheet.load()

pattern = midi.Pattern()
track = midi.Track()
track.append(midi.ProgramChangeEvent(value=instrument, channel=channel));

# Set all notes to off
state = [0 for x in range(size[1])]

tick = 0
for x in range(size[0]):
	for y in range(len(notes)):
		note = notes[-(y + 1)]
		value = pixels[x,y] if isinstance(pixels[x,y], int) else pixels[x,y][0]
		if value < 200:
			if state[y] == 0:
				track.append(midi.NoteOnEvent(tick=tick, velocity=velocity, pitch=note, channel=channel))
				tick = 0
				state[y] = 1
		elif state[y] == 1:
			track.append(midi.NoteOffEvent(tick=tick, velocity=velocity, pitch=note, channel=channel))
			tick = 0
			state[y] = 0
	tick = tick + tpp

pattern.append(track)

midi.write_midifile(output_file, pattern)
