Avendesora Export: Exports Selected Accounts to a Remote Host
=============================================================


.. image:: https://pepy.tech/badge/avendesora-export/month
    :target: https://pepy.tech/project/avendesora-export

.. image:: https://img.shields.io/pypi/v/avendesora-export.svg
    :target: https://pypi.python.org/pypi/avendesora-export

.. image:: https://img.shields.io/pypi/pyversions/avendesora-export.svg
    :target: https://pypi.python.org/pypi/avendesora-export


| Author: Ken Kundert
| Version: 0.1
| Released: 2022-11-01
| Please post all questions, suggestions, and bug reports to
  `Github Issues <https://github.com/KenKundert/avendesora-export/issues>`_.
|

*Avendesora Export* creates `Avendesora <https://avendesora.readthedocs.io>`_ 
account files on remote machines that contain selected accounts.  This allows 
you to use *Avendesora* on satellite hosts without maintaining two independent 
databases of account information.  Simply install *Avendesora* on both your 
primary and satellite machines.  Keep all, or at least most, of your accounts on 
your primary machine and configure *Avendesora Export* to manage the satellites.  
It needs to know the hostname, the path to the accounts file, the encryption 
keys, and the accounts you wish to export to each satellite.

For example, imagine owning a laptop, which is your primary machine, a media 
machine for watching videos and listening to music, and a server that contains 
your Bitcoin node.  Assuming *Avendesora* is already installed on your laptop 
and contains all of your accounts, install *Avendesora Export* on your laptop 
and add the following file to ~/.config/avendesora-export/config.nt::

    media:
        dest: media:.config/avendesora/imported.gpg
        gpg id: D790CFBA20343D0E
        accounts:
            - Netflix
            - YouTubeTV
            - Hulu
            - HBO
            - Disney
            - Spotify

    server:
        dest: server:.config/avendesora/imported.gpg
        gpg id: D790CFBA20343D0E
        accounts:
            - BitcoinRPC

Then, running::

    avendesora-export media

exports the selected accounts to your media machine.  It can be run from any 
directory on your laptop.

Be aware that an export simply overwrites the previously exported accounts file.  
You should not manually add accounts to a exported accounts file.  If you would 
like accounts that are only local to the satellite host, simply add them to its 
accounts.gpg file.  When you first export a file to a host, you need to add the 
name of that file to the *accounts_files* list in 
``~/.config/avendesora/accounts_files``.

You should also be aware that the exported secrets are frozen, meaning that any 
generated secrets that are exported are converted to remembered secrets on the 
satelite.


Releases
--------

Latest Development Version
    | Version: 0.1
    | Released: 2022-11-01
