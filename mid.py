import mido
def midi_note_to_name(note_number):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = (note_number // 12) - 1
    note_name = notes[note_number % 12]
    return f'{note_name}{octave}'
def midi_to_notes(midi_file):
    notes = []
    midi = mido.MidiFile(midi_file)
    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on' and msg.velocity > 0:  
                note_name = midi_note_to_name(msg.note)  
                note_duration = 4  
                notes.append(f'"{note_name}:{note_duration}"')
    return notes
midi_file_path = r"C:\Users\tansi\Downloads\Bad Apple.mid"
notes = midi_to_notes(midi_file_path)
print("music.play([", ', '.join(notes), "])")
