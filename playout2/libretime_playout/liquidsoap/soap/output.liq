# Icecast output
###############################################################################

def create_icecast_output(id, ~protocol, ~host, ~port, ~password, ~mount, ~name, ~url, ~description, ~genre) =
    o = output.icecast(
        id="output_icecast_#{id}",
        protocol=protocol,
        host=host,
        port=port,
        password=password,
        mount=mount,
        fallible=true,

        name=name,
        url=url,
        description=description,
        genre=genre,

        # on_connect=icecast_on_connect(id),
        # on_error=icecast_on_error(id)
    )
    o
end

# HLS output
###############################################################################


# def hls_segment_name(id, ~position, ~extname, stream_name) =
#     timestamp = int_of_float(gettimeofday())
#     duration = 2
#     "#{id}_#{stream_name}_#{duration}_#{timestamp}_#{position}.#{extname}"
# end

# def create_hls_output(id, aac_lofi, aac_midfi, aac_hifi) =
#     streams = [
#         ("aac_lofi", aac_lofi),
#         ("aac_midfi", aac_midfi),
#         ("aac_hifi", aac_hifi),
#     ]
#     o = output.file.hls(
#         playlist="#{id}.m3u8",
#         segment_duration=2.0,
#         segments=5,
#         segments_overhead=5,
#         segment_name=hls_segment_name(id),
#         persist_at="./hls.conf",
#         "./hls/",
#         streams,
#         )
#     o
# end

# # Archive output
# ###############################################################################

# def archive_on_close(id, filename)
#     # TODO: Implement
#     process.run("cp #{fname} /radio/#{id}backup/")
# end

# def create_archive_output(id) =
#     o = output.file(
#         reopen_when={0m},
#         on_close=archive_on_close(id),
#     )
#     o
# end
