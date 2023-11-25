from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql import text 
from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

# Create a Flask app
app = Flask(__name__)

# Configure the PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist_app?host=/var/run/postgresql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Connect the app to the database and set the secret key
connect_db(app)
app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Enable the Debug Toolbar; explicitly show redirects
# If you want to turn off the toolbar for redirects, uncomment the line below
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


# Homepage route, redirects to /playlists
@app.route("/")
def root():
    """Homepage: redirect to /playlists."""
    return redirect("/playlists")


##############################################################################
# Playlist routes

# Show all playlists route
@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""
    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


# Show a specific playlist route
@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on a specific playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    return render_template("playlist_detail.html", playlist=playlist)


# Add a playlist route
@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - If the form is not filled out or invalid: show the form
    - If the form is valid: add the playlist to SQLA and redirect to the list-of-playlists
    """
    form = PlaylistForm()

    if form.validate_on_submit():
        new_playlist = Playlist(name=form.name.data, description=form.description.data or None)
        db.session.add(new_playlist)
        db.session.commit()
        return redirect("/playlists")

    return render_template("add_playlist.html", form=form)


##############################################################################
# Song routes

# Show all songs route
@app.route("/songs")
def show_all_songs():
    """Show a list of songs."""
    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


# Show a specific song route
@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """Return details for a specific song."""
    song = Song.query.get_or_404(song_id)
    return render_template("song_detail.html", song=song)


# Add a song route
@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - If the form is not filled out or invalid: show the form
    - If the form is valid: add the song to SQLA and redirect to the list-of-songs
    """
    form = SongForm()

    if form.validate_on_submit():
        new_song = Song(title=form.title.data, artist=form.artist.data)
        db.session.add(new_song)
        db.session.commit()
        return redirect("/songs")

    return render_template("add_song.html", form=form)


# Add a song to a playlist route
@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a song to a playlist and redirect to the playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist
    curr_on_playlist = [ps.song_id for ps in playlist.playlists_songs]
    form.song.choices = [(s.id, s.title) for s in Song.query.filter(Song.id.notin_(curr_on_playlist)).all()]

    if form.validate_on_submit():
        song_id = form.song.data
        playlist_song = PlaylistSong(playlist_id=playlist_id, song_id=song_id)
        db.session.add(playlist_song)
        db.session.commit()
        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html", playlist=playlist, form=form)


if __name__ == '__main__':
    app.run(debug=True)
