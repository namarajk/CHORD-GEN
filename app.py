from flask import Flask, render_template, request
import music21

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_chord_progression", methods=["POST"])
def generate_chord_progression():
    # Get the chord progression input from the form
    chord_progression = request.form.get("chords")
    # Split the input into individual chords
    chords = chord_progression.split(", ")
    
    # Create a new stream for the MIDI file
    stream = music21.stream.Stream()

    # Set the instrument to piano
    piano = music21.instrument.Piano()
    stream.append(piano)

    # Set the tempo to 120 beats per minute
    tempo = music21.tempo.MetronomeMark(number=120)
    stream.append(tempo)

    # Iterate through each chord in the progression
    for chord in chords:
        # Parse the chord symbol and create a chord object
        chord_obj = music21.harmony.ChordSymbol(chord)
        # Get the notes in the chord
        notes = chord_obj.pitches
        # Create a new chord object with the notes
        chord_notes = music21.chord.Chord(notes)
        # Add the chord to the stream
        stream.append(chord_notes)

    # Write the stream to a MIDI file
    stream.write('midi', fp='chord_progression.mid')

    return "Chord progression generated!"

if __name__ == "__main__":
    app.run(debug=True)
