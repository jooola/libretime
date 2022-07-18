# Live inputs
###############################################################################

# def live_auth(id, user, password, address) =
#     # TODO: Implement auth check
# end

# def live_on_connect(id, headers) =
#     update_source_status("live_#{id}", true)
# end

# def live_on_disconnect(id) =
#     update_source_status("live_#{id}", false)
# end

# live_main = create_live_source("main", "/main", 8001)
# live_show = create_live_source("show", "/show", 8002)
def create_live_source(id, mount, port) =
    audio_to_stereo(
        input.harbor(
            id="live_stream_#{id}",
            # auth=live_auth(id),
            mount,
            port=port,
            max=40.,
            # on_connect=live_on_connect(id),
            # on_disconnect=live_on_disconnect(id),
        )
    )
end
