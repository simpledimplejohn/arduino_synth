import time
import fluidsynth

# Create a FluidSynth instance (no argument means default driver, which is coreaudio on macOS)
fs = fluidsynth.Synth()

# Start the synth
fs.start()

# Load the SoundFont (update the path to your actual .sf2)
sfid = fs.sfload("/Users/johnblalock/Documents/arduino_synth/soundfont/phonk.sf2")

# Select a preset from bank=0, preset=0
fs.program_select(0, sfid, 0, 0)

# Turn on a middle C (MIDI note 60) at full velocity (127)
print("Playing a note…")
fs.noteon(0, 60, 127)
time.sleep(2)  # sustain for 2 seconds

# Turn the note off
fs.noteoff(0, 60)

print("Played a note successfully!")
