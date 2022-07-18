# THIS FILE IS AUTO GENERATED. PLEASE DO NOT EDIT!
###########################################################
# The ignore() lines are to squash unused variable warnings



settings.server.socket.set(true)
settings.server.socket.path.set("liquidsoap.sock")

interactive.persistent("vars.json")

settings.harbor.bind_addrs.set(["0.0.0.0"])


icecast_outputs = ref([
    {
        id = "main1",
        enabled = true,
        # Meta
        name = "Main ogg (256kbps)",
        description = "",
        url = "",
        genre = "various",
        # Audio
        audio_type = "ogg",
        audio_channels = "stereo",
        audio_bitrate = "256",
        # Icecast
        icecast_host = "localhost",
        icecast_port = "8000",
        icecast_mount = "/main.ogg",
        # Icecast Auth
        icecast_admin_user = "admin",
        icecast_admin_password = "admin"
    },
])
ignore(icecast_outputs)

%include "/home/jo/git/github.com/jooola/libretime/playout/libretime_liquidsoap/soap/run.liq"
