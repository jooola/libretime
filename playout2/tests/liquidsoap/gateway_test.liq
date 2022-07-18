
settings.server.socket.path.set(argv(1, default="liquidsoap.sock"))
settings.server.socket.set(true)

var1 = interactive.bool("var1", false)
ignore(var1)

output.dummy(blank(id="safe_blank"))
