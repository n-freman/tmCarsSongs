from django.test import TestCase
from django.core.exceptions import ValidationError

from singers.models import Singer
from songs.models import Song


class SongModelTest(TestCase):

    def test_default_genre(self):
        song = Song()
        self.assertEqual(song.genre, '')

    def test_song_is_related_to_singer(self):
        singer = Singer.objects.create()
        song = Song()
        song.singer = singer
        song.save()
        self.assertIn(song, singer.songs.all())

    def test_cannot_save_song_without_title(self):
        singer = Singer.objects.create()
        song = Song(singer=singer, title='')
        with self.assertRaises(ValidationError):
            song.save()
            song.full_clean()
    
    def test_cannot_save_duplicate_songs_for_one_singer(self):
        singer = Singer.objects.create()
        song1 = Song(
            title='Some interesting title',
            singer=singer
        )
        song2 = Song(
            title='Some interesting title',
            singer=singer
        )
        song1.save()
        with self.assertRaises(ValidationError):
            song2.save()
            song2.full_clean()

    def test_string_representation(self):
        singer = Singer.objects.create(full_name='Singer Name')
        song = Song(
            title='Some interesting title',
            singer=singer
        )
        self.assertEqual(str(song), 'Singer Name: Some interesting title')



