These are the Contributor, Maintainer and Administrator issue answering "cheat" snippets. Feel free to use them as you see fit. 

Feel free to change them so they make sense depending on the situation (ie. use Cheers vs. Regards or sprinkle with emojis).


* [Contributor Snippets](#contributor-snippets)
  * [Community Welcome](#community-welcome)
  * [Needs more Information](#needs-more-information)
    * [Provide Version Info](#provide-version-info)
    * [Provide Error Message](#provide-error-message)
    * [Provide Logs](#provide-logs)
    * [Provide Screenshots](#provide-screenshots)
* [Maintainer Snippets](#maintainer-snippets)
  * [Consensus Needed](#consensus-needed)
* [Administrator Snippets](#administrator-snippets)
  * [Contributor Invite](#contributor-invite)
  * [Maintainer Invite](#maintainer-invite)
  * [Inactive Maintainer Removal](#inactive-maintainer-removal)
  * [Failure to Follow Process](#failure-to-follow-process)
  * [Bad Actor Block](#bad-actor-block)

Most of them where written using text snippets from the C4 specification with changes made to make them sound friendly rather than RFCy. Please add more and feel free to improve their wording or anything else on this page.

## Contributor Snippets

These snippets are made available to everyone who would like to help out with triaging bugs and supportings users.

### Community Welcome

Use this or a similar opening to welcome new Contributors to the community.

```
Hello @[name]

Welcome to the LibreTime community. We are glad to have you on board. 
Help us keep LibreTime open and inclusive by following our [Code of Conduct (CoC)](https://github.com/LibreTime/code-of-conduct/blob/master/CODE_OF_CONDUCT.md). 
Feel free to let us know if [CONTRIBUTING.md](https://github.com/LibreTime/libretime/blob/master/CONTRIBUTING.md)
is lacking anything you need to get onboarded rapidly.
```

After this introductory snippet, go on and address the community members 
needs. The FAQ cases might contain an answer below. If you need to craft 
one, please consider adding it below so other Maintainers can profit.

### Needs more Information

> The user or Contributor SHOULD write the issue 
> by describing the problem they face or observe.
>
> Users SHALL NOT log feature requests, ideas, suggestions, 
> or any solutions to problems that are not explicitly 
> documented and provable.

When an issue needs more info:

```
Hello @[name]

Thank you for your [choose one: feature request, idea, suggestion, solution].
We are trying to ensure that the release history of LibreTime is a list of 
meaningful issues logged and solved. To achieve this we need you to help out 
by only logging explicitly documented and provable issues (see
[C4:2.4](https://rfc.zeromq.org/spec:42/C4/#24-development-process) for 
details on this process).

I'm sure you have a valid issue at your hands. Please help us narrow it down 
by providing more information so we can get the docs updated and reproduce it
on our side.

[insert pointers to what we need to know]
```

#### Provide Version Info

```
Please specify the full version of LibreTime you are using. We will also need 
to know what OS your install is on and how you installed it.

If you installed from source (ie. by cloning or downloading this repo or a 
legacy upstream fork) we need to know the exact commit you installed. If you 
got it from GitHub, navigate to the branch or repo you installed and press 
<kbd>Y</kbd> before copying the URL, this is the URL we need to help 
diagnose your issue.

Thanks,

[your name]
```

#### Provide Error Message

```
Please supply us with the exact error message by copy pasting it below.

Thanks,

[your name]
```

#### Provide Logs

```
Please try trimming down the log to the part where you suspect 
the error happens while leaving enough context for us to see
what is going on. Often the lines before and after an error
are just as interesting as the error line itself. It usually
makes sense to include 10-20 lines of log both before and after 
the error message.

If you cannot trim a log file down to a sensible size, consider
uploading it to a [gist](https://gist.github.com) and post the
link. Remember, developers are usually fast at scanning a log.

# to be finished, needs some real world cases with users log paths and actual example to pick from
```

## Provide Screenshots

```
# TBD
```

## Maintainer Snippets

Please add more...

### Consensus Needed

> The user or Contributor SHOULD seek consensus on 
> the accuracy of their observation, and the value 
> of solving the problem.

```
# TDB
```

## Administrator Snippets:

These snippets are for the use of the project Administrators and help them fulfill their C4 duties.
### Contributor Invite
To reach em and maybe assign issues that we know a member Contributor has knowledge on. 

Getting on the team behind this has no write rights to the repos but all Contributors can be reached through `@LibreTime/contributors`. 

Can be used for folks that have written proper issues or helped others out immediately. 

If you are not an Administrator and would like to add someone, tag the admins as described 
so they can send out an invite.

```
Hi @[name]

Thank you for your recent contribution to LibreTime. We value you 
as a Contributor and I just invited [or: and I'm asking the 
@LibreTime/administrators to invite] you to the Contributors
Team. 

As a team member you can assign issues and use labels etc. You will
also be reachable through the LibreTime/contributors alias. We will 
keep the alias a low volume communications channel and only use it 
to reach you in case we have important announcements or urgent security 
related information.

Feel free to accept or decline the invitation as you see fit. Declining
it does not make you any less of a Contributor in our view.

Thanks again for being part of the LibreTime community!

Regards,

[your name]
```

### Maintainer Invite 

> A new Contributor who makes correct patches, who clearly 
> understands the project goals, and the process SHOULD be 
> invited to become a Maintainer.

Use this on a closed PR that was fun to close and you are convinced that @[name]
is a worthy Maintainer. Invite Contributors after they make a couple of
contributions without hesitating.
```
Dear @[name]

Thank you for contributing to LibreTime in a meaningful way. With 
contributions such as this one you have demonstrated that you are 
well able to make correct patches, and clearly understand the 
project goals.

Therefore, we would like to invite you to become one of the 
Maintainers of LibreTime. The duties of a Maintainer are 
outlined in [C4, 2.4](https://rfc.zeromq.org/spec:42/C4/#24-development-process). 
Below is an excerpt:

> 12. To accept or reject a patch, a Maintainer SHALL use the Platform interface.
> 13. Maintainers SHOULD NOT merge their own patches except in exceptional cases, such as non-responsiveness from other Maintainers for an extended period (more than 1-2 days).
> 14. Maintainers SHALL NOT make value judgments on correct patches.
> 15. Maintainers SHALL merge correct patches from other Contributors rapidly.
> 16. Maintainers MAY merge incorrect patches from other Contributors with the goals of (a) ending fruitless discussions, (b) capturing toxic patches in the historical record, (c) engaging with the Contributor on improving their patch quality.

Please let me know if you will join the Maintainers team
and I will set you up with the right membership.

Thanks again for your hard work!

Regards,

[your name]
```

When the Contributor accepts

```
Hi @[name]

Thank you for getting back to me and welcome aboard. I sent you a GitHub invite to
the Maintainers team. As a member of that team you can now merge pull requests on
the main LibreTime repos.

To make life easier for Maintainers we have prepared some snippets to use when 
engaging with the community in your capacity as a Maintainer. You can find them 
in the [wiki](https://github.com/LibreTime/libretime/wiki/Issue-Snippets). Feel 
free to edit them and add more as you see fit.

You will also be notified when people try to reach the @LibreTime/maintainers
team identifier. In fact everyone should have just been messaged so they can
welcome you aboard.

Regards,

[your name]
```

If the Contributor declines

```
Hi @[name]

Thank you for getting back to me. Regardless of your decision, having you on board
as a Contributor is valuable to us.

Let us know if your situation changes and you are ready to reconsider our offer.

Thanks again for being part of our community.

Regards,

[your name]
```

### Inactive Maintainer Removal

> Administrators SHOULD remove Maintainers who are 
> **inactive for an extended period of time**, or who 
> repeatedly fail to apply this process accurately.

If a Maintainer falls under these criteria, please
open an issue addressing this. 

In the case of inactivity (after you have exhausted 
ways of contacting the Maintainer and it is obvious 
that he/she is not simply on a prolonged leave or 
vacation).

```
Hello @LibreTime/maintainers

I will remove @[name] from the Maintainers team due to 
his [or her] inactivity over an extended period of time.

In the name of the LibreTime community, I would like to 
thank @[name] for his [or her] contribution to LibreTime.

@[name], if you would like to stay on the team, let us 
know as soon as possible.

If I do not hear from @[name] or another community member 
with information regarding @[name]s inactivity in two 
weeks time, I will finalize removing him [or her] from 
the Maintainers team.

Regards,

[your name]
```

### Failure to Follow Process

> Administrators SHOULD remove Maintainers who are 
> inactive for an extended period of time, or who 
> **repeatedly fail to apply this process accurately**.

```
# TBD
```

### Bad Actor Block

> Administrators SHOULD block or ban "bad actors" 
> who cause stress and pain to others in the project. 
> This should be done after public discussion, with a 
> chance for all parties to speak. A bad actor is 
> someone who repeatedly ignores the rules and culture 
> of the project, who is needlessly argumentative or 
> hostile, or who is offensive, and who is unable to 
> self-correct their behavior when asked to do so 
> by others.

This should only be used after public discussion and 
to inform the community as well as the "bad actor". 
Blocking or banning someone should not have the effect 
of a shadow ban, everything is expected to be in the 
open and understandable to both the banee and the 
community at large.

This should not be used in any way to denunciate the 
person we are blocking. Unfortunately, he or she may 
have reasons for their behaviour beyond our understanding. 
Keep this in mind when blocking someone and always consider
all involved parties.

You should go re-read the [CoC](https://github.com/LibreTime/code-of-conduct/blob/master/CODE_OF_CONDUCT.md)
before taking this drastic measure, it could help you 
get a different perspective on things.
```
# TBD (for hopefully obvious reasons)
```