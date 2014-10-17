https://github.com/tlevine/sheetmusic
>>> import sheetmusic
>>> sheetmusic.init()
>>> sheetmusic.play('F2:H12')

>>> from mingus.midi import fluidsynth
>>> fluidsynth.init("FluidR3_GM2-2.sf2")

http://sudoit.blogspot.be/2009/08/starting-with-timidity-and-soundfonts.html
https://code.google.com/p/mingus/wiki/tutorialFluidsynth
http://www.hammersound.net/
http://www.sf2midi.com/tag/seashore/
http://www.swamiproject.org/download/
http://www.polyphone.fr/index.php?lang=en&page=download

http://askubuntu.com/questions/233060/recording-speaker-audio-using-avconv
pactl list sources | grep analog-stereo.monitor
ffmpeg -f pulse -i alsa_output.pci-0000_00_1b.0.analog-stereo.monitor  alsa-output_analog-stereo_monitor.wav

CONVERT MIDI TO WAV:
timidity -Ow [filename]
