Some Basic Rules I want to follow

-Everything is Modular and easily expandible.
addition of new features should be hassle free

-Everything should be cleanly organized, no random one-off helper functions

-Most things should be deterministic only very few things are allowed to be random or controlled by the LLMs

-Nameless should not be able to alter or mess with the admin hirearchy

-dependencies point one way (no circular dependencies)

-only system/ touches the OS

-utils/ imports nothing from rest of Nameless

-Use of Nameless should be Free or Close to Free, At Least One Model should Exist like this

-All documents and packages are clearly explained (in as much detail as I can) so no confusion exists

-All of Nameless' Actions must be logged and easily accessible

-I'll try to handle all the edge cases, but any Exceptions must be clear. no silent failures

-It's Personality and Name Should be customizable
