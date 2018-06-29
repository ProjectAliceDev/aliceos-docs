Ren'Py Applet
=============

The Ren'Py Applet, also known as "Ren'Py VN Engine", is a 
quick and dirty way to present your visual novel as an 
AliceOS applet, enabling components like notifications 
and window management.

Applet Information
------------------

* ``short_name`` - Uses RenPy's ``build.name``
* ``long_name`` - Uses RenPy's ``config.name``
* ``version`` - Uses RenPy's ``config.version``
* ``author`` - Ren'Py Team
* ``permissions`` - ``pm_notify``, ``pm_files``, ``pm_sysadmin``
* ``description`` - Uses ``gui.about``

.. note:: In testing versions, the original names were "Ren'Py" and "Ren'Py VN Engine".
          If you want to overwrite this, edit ``Applets/RenPy/RenPy.rpy``.


