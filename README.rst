Callback File Cache
====================

A simple cache class that stores result to files and support callbacks.


Instantiate client
------------------

.. code::

    from cache import File

    cache = File()

cache.get_with_callback
-----------------------
When using the ``get_with_callback`` method, all the subsequent
arguments are used to create a unique cache key. Example below using
the https://bitbucket.org/nord-fk/bfs-soap-api-wrapper/ package.

.. code::

    accounts = cache.get_with_callback(callback=bfs.get,
        method=bfs.methods.GET_ACCOUNTS,
        args={
            'Owners': ['edf2076b-75b6-4a41-9c65-d6eacd073543']
        })
