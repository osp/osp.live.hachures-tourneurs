# Listen to SVG
A script to listen to an SVG basde on its curves.

Processing sketch is a modification of this: http://forum.processing.org/one/topic/make-a-dot-follow-a-svg-path.html

## Requirements
- Processing 2.2.1 (other versions untested)
- Geomerative library
- Pure Data Extended (needed for OSC libraries)

## Usage
- Launch osc.pd and turn on sound processing (Ctrl + L)
- Open lisetntoSVG.pde in Processing (required Processing libraries oscP5 & geomerative)
- Place an SVG file named "image.svg" into the data folder
- Run the Processing sketch

## To Do
- Scale the SVG to fit the sketch window automatically
- Save the sound to a wav file
- Somehow extract the colour and stroke data from the image for use as a sound source
