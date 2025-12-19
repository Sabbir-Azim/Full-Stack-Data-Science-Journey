### Speed_trap_lookup

List lookup time: 0.01034164 seconds

In case of List, python search linearly O(N), looping 1,2,3...n whether the lookup number exists or not.

Set lookup time: 0.00000310 seconds

Whereas for set elements or dict keys, python first creates differnt hash memory for each item, and then directly search for memory location O(1) for the lookup number. It don't require the extensive loop search. It's known as Hash Lookup.