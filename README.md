python-flock
============

flock.Flock(fd, op)
-------------------

Flock object uses `fcntl.flock` to lock (resp. unlock)
file descriptor (`fd`) with operation (`op`)
when entering (resp. leaving) runtime context related to it.

File objects providing a `fileno()` method are accepted as well.

Operation is one of the following values:
    
 * `LOCK_SH` - acquire a shared lock
 * `LOCK_EX` - acquire an exclusive lock

Operation can also be bitwise ORed with `LOCK_NB`
to avoid blocking on lock acquisition.


Example:
--------

    with open('/tmp/file.lock', 'w') as f:
        blocking_lock   = flock.Flock(f, flock.LOCK_EX)
        noblocking_lock = flock.Flock(f, flock.LOCK_EX|flock.LOCK_NB)

        with blocking_lock:
            pass # do something here

        try:
            with noblocking_lock:
                pass # do something else here
        except BlockingIOError:
            pass

