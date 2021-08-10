Avendesora Export: Exports a Selected Accounts to Remote Host
=============================================================


.. image:: https://pepy.tech/badge/avendesora-export/month
    :target: https://pepy.tech/project/avendesora-export

.. image:: https://img.shields.io/pypi/v/avendesora-export.svg
    :target: https://pypi.python.org/pypi/avendesora-export

.. image:: https://img.shields.io/pypi/pyversions/avendesora-export.svg
    :target: https://pypi.python.org/pypi/avendesora-export


| Author: Ken Kundert
| Version: 0.0.0
| Released: 2021-08-09
| Please post all questions, suggestions, and bug reports to
  `Github Issues <https://github.com/KenKundert/avendesora-export/issues>`_.
|

*Avendesora Export* can create `https://avendesora.readthedocs.io`_ account 
files on remote machines that contain selected accounts.  This allows you to use 
*Avendesora* on satellite machines without maintaining two independent databases 
of account information.  Simply install *Avendesora* on both your primary and 
satellite machines.  Keep all, or at least most, of your accounts on your 
primary machine and configure *Avendesora Export* to manage the satellites.  It 
needs to know the hostname, the path to the accounts file, the encryption keys, 
and the accounts you wish to export to each satellite.

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

Be aware that an export simply overwrites the previously exported accounts file 
and that an exported accounts file is not setup to support generated secrets.  
You should manually add accounts to a exported accounts file.  If you would like 
accounts that are only local to the satellite host, simply add them to its 
accounts.gpg file.



Releases
--------

Latest Development Version
    | Version: 0.0.0
    | Released: 2021-08-09
