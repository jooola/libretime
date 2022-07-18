
%include "input.liq"
%include "output.liq"

queue1 = request.queue(id="queue1")
queue2 = request.queue(id="queue2")

use_queue1 = interactive.bool("use_queue1", false)
use_queue2 = interactive.bool("use_queue2", false)

live_main_enabled = interactive.bool("live_main_enabled", false)
live_show_enabled = interactive.bool("live_show_enabled", false)
scheduled_enabled = interactive.bool("scheduled_enabled", false)

show_name = interactive.string("show_name", "")
show_url = interactive.string("show_url", "")

station_name = interactive.string("station_name", "")
station_url = interactive.string("station_url", "")

webstream_enabled = interactive.bool("webstream_enabled", false)
webstream_id = interactive.int("webstream_id", -1)
webstream_url = interactive.string("webstream_url", "")

queues = switch(
    id="queues",
    track_sensitive=false,
    [(use_queue1, queue1), (use_queue2, queue2)]
)

live_main = create_live_source("main", "/main", 8001)
live_show = create_live_source("show", "/show", 8002)

radio = fallback(
    track_sensitive=false,
    [
        live_main,
        live_show,
        queue1,
        queue2,
        noise(id="safe_noise"),
        blank(id="safe_blank"),
    ]
)

outputs = ref([])

list.iter(
    fun(item) -> outputs := list.append(
        create_icecast_output(
            item.id,
            protocol=item.icecast_protocol,
            host=item.icecast_host,
            port=item.icecast_port,
            password=item.icecast_password,
            mount=item.icecast_mount,
            name=item.name,
            url=item.url,
            description=item.description,
            genre=item.genre,
        ),
        !outputs
    ),
)

output_device_enabled = interactive.bool("output_device_enabled", false)
output_archive_enabled = interactive.bool("output_archive_enabled", false)
output_icecast_enabled = interactive.bool("output_icecast_enabled", false)
output_icecast_mounts = ref([])

output_hls_enabled = interactive.bool("output_hls_enabled", false)


# output_to(s1_output, s1_type, s1_bitrate, s1_host, s1_port, s1_pass,
#             s1_mount, s1_url, s1_description, s1_genre, s1_user, s, "1",
#             s1_connected, s1_name, s1_channels)

# if s2_enable == true then
#     if s2_output == 'shoutcast' then
#         s2_namespace := "shoutcast_stream_2"
#     else
#         s2_namespace := s2_mount
#     end
#     server.register(namespace=!s2_namespace, "connected", fun (s) -> begin log("#{!s2_namespace}.connected") !s2_connected end)
#     output_to(s2_output, s2_type, s2_bitrate, s2_host, s2_port, s2_pass,
#                 s2_mount, s2_url, s2_description, s2_genre, s2_user, s, "2",
#                 s2_connected, s2_name, s2_channels)

# end

# if s3_enable == true then
#     if s3_output == 'shoutcast' then
#         s3_namespace := "shoutcast_stream_3"
#     else
#         s3_namespace := s3_mount
#     end
#     server.register(namespace=!s3_namespace, "connected", fun (s) -> begin log("#{!s3_namespace}.connected") !s3_connected end)
#     output_to(s3_output, s3_type, s3_bitrate, s3_host, s3_port, s3_pass,
#                 s3_mount, s3_url, s3_description, s3_genre, s3_user, s, "3",
#                 s3_connected, s3_name, s3_channels)
# end

# if s4_enable == true then
#     log("Stream 4 Enabled")
#     if s4_output == 'shoutcast' then
#         s4_namespace := "shoutcast_stream_4"
#     else
#         s4_namespace := s4_mount
#     end
#     server.register(namespace=!s4_namespace, "connected", fun (s) -> begin log("#{!s4_namespace}.connected") !s4_connected end)
#     output_to(s4_output, s4_type, s4_bitrate, s4_host, s4_port, s4_pass,
#                 s4_mount, s4_url, s4_name, s4_genre, s4_user, s, "4",
#                 s4_connected, s4_description, s4_channels)
# end


# command = "timeout --signal=KILL 45 pyponotify --liquidsoap-started &"
# log(command)
# system(command)


# icecast_mount1 = create_icecast_output(id, host, port, password, mount, name, url, description, genre)

# # out = output.icecast(host="localhost", port=8000, password="hackme")
# # out(%mp3, mount="rock.mp3", rock)
# # out(%fdkaac, mount="rock.aac", rock)
# # out(%mp3, mount="techno.mp3", techno)
# # out(%fdkaac, mount="techno.aac", techno)


# # Decode
# # Inputs
# # Encode
# # Outputs

# radio = ffmpeg.encode.audio(%ffmpeg(%audio(codec="libmp3lame")), radio)


# output.icecast(fallible=true, format="audio/mpeg", %ffmpeg(format="mp3", %audio.copy), mount="radio", radio)
# output.file.hls(fallible=true, "hls", [("mp3", %ffmpeg(format="mp3", %audio.copy))], radio)

# output.file(fallible=true, %ffmpeg(format="mp3", %audio.copy), "radio.mp3", radio)

# %ffmpeg(format="mpegts",
# %audio(codec="libfdk_aac", samplerate=22050, b="32k",
# afterburner=1, profile="aac_he_v2"))
