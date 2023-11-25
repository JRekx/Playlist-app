from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Playlist(db.Model):
    """Playlist model."""

    __tablename__ = 'playlists'

    # Primary Key for the Playlist model
    id = db.Column(db.Integer, primary_key=True)

    # Name of the playlist (e.g., "Workout Mix")
    name = db.Column(db.String(50), nullable=False)

    # Description of the playlist (optional)
    description = db.Column(db.String(255))

class Song(db.Model):
    """Song model."""

    __tablename__ = 'songs'

    # Primary Key for the Song model
    id = db.Column(db.Integer, primary_key=True)

    # Title of the song (e.g., "Shape of You")
    title = db.Column(db.String(100), nullable=False)

    # Artist of the song (e.g., "Ed Sheeran")
    artist = db.Column(db.String(50), nullable=False)

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song model."""

    __tablename__ = 'playlists_songs'

    # Primary Key for the PlaylistSong model
    id = db.Column(db.Integer, primary_key=True)

    # Foreign Key linking to the Playlist model
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)

    # Foreign Key linking to the Song model
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

    # Relationship with the Playlist model to easily access playlist information
    playlist = db.relationship('Playlist', backref='playlists_songs')

    # Relationship with the Song model to easily access song information
    song = db.relationship('Song', backref='playlists_songs')
