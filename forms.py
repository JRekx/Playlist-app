from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Use StringField for name and TextAreaField for description
    name = StringField('Playlist Name', validators=[InputRequired(message="Name is required")])
    description = TextAreaField('Playlist Description')


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Use StringField for title and artist
    title = StringField('Song Title', validators=[InputRequired(message="Title is required")])
    artist = StringField('Artist', validators=[InputRequired(message="Artist is required")])

class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to a playlist."""

    song = SelectField('Song To Add', coerce=int)
