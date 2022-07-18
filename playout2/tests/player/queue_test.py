from libretime_playout.player.queue import create_liquidsoap_annotation


def test_create_liquidsoap_annotation():
    assert create_liquidsoap_annotation(
        {
            "dst": "path/to/some/file.mp3",
            "fade_in": "0.0",
            "fade_out": "0.0",
            "cue_in": "0.5",
            "cue_out": "56.8",
            "id": "1",
            "row_id": "4",
            "replay_gain": "-5.6",
            "metadata": {
                "artist_name": "Some",
                "track_title": 'With a "',
            },
        }
    ) == (
        'liq_start_next="0",'
        'liq_fade_in="0.0",'
        'liq_fade_out="0.0",'
        'liq_cue_in="0.5",'
        'liq_cue_out="56.8",'
        'item_id="1",'
        'schedule_table_id="4",'
        'replay_gain="-5.6 dB",'
        'artist="Some",'
        'title="With a \\""'
        ":path/to/some/file.mp3"
    )
