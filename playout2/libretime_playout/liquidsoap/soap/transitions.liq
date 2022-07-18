
def transition(previous, next) =
    log("transition called...")
    add(
        normalize=false,
        [
            sequence([
                blank(duration=0.01),
                fade.initial(duration=!default_dj_fade, next)
            ]),
            fade.final(duration=!default_dj_fade, previous)
        ]
    )
end

def transition_default(previous, next) =
    if !just_switched then
        just_switched := false
        transition(previous, next)
    else
        just_switched := false
        next
    end
end

def to_live(previous, next) =
    previous = fade.final(previous)
    sequence([previous, next])
end
