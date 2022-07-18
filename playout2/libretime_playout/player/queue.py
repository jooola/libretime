def escape_quotes(value: str) -> str:
    return value.replace('"', '\\"')


def create_liquidsoap_annotation(item: dict):
    """
    Create a liquidsoap annotation string for the item.
    """
    annotations = []

    # We need liq_start_next value in the annotate. That is the value that controls
    # overlap duration of crossfade.
    annotations.append(f'liq_start_next="{0}"')
    annotations.append(f'liq_fade_in="{float(item["fade_in"]) / 1000}"')
    annotations.append(f'liq_fade_out="{float(item["fade_out"]) / 1000}"')
    annotations.append(f'liq_cue_in="{float(item["cue_in"])}"')
    annotations.append(f'liq_cue_out="{float(item["cue_out"])}"')

    annotations.append(f'item_id="{item["id"]}"')
    annotations.append(f'schedule_table_id="{item["row_id"]}"')
    annotations.append(f'replay_gain="{item["replay_gain"]} dB"')

    if "metadata" in item:
        if "artist_name" in item["metadata"]:
            artist_name = item["metadata"]["artist_name"]
            if isinstance(artist_name, str):
                annotations.append(f'artist="{escape_quotes(artist_name)}"')

        if "track_title" in item["metadata"]:
            track_title = item["metadata"]["track_title"]
            if isinstance(track_title, str):
                annotations.append(f'title="{escape_quotes(track_title)}"')

    annotation = ",".join(annotations)
    annotation += ":" + item["dst"]

    return annotation
