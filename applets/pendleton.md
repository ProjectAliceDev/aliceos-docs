---
title: System Applet (Pendleton)
---
System Applet (Pendleton)
=============

AliceOS comes with a unique applet designed for system notifications and processes that must be executed in such a manner: Pendleton.

Applet Information
------------------

-   `short_name` - Pendleton
-   `long_name` - AliceOS System
-   `version` - Uses AliceOS version
-   `author` - AliceOS Developers
-   `permissions` - `pm_notify`, `pm_files`, `pm_sysadmin`
-   `description` - Send system notifications.

In code, Pendleton is called as `SystemUIServer`.

## Sending notifications
To send a notification on the behalf of the system, use Pendleton's `send_temporary_notification()` functionality. However, there are certain cases in which this should be used:

<ul class="p-list">
    <li class="p-list__item is-ticked">A system action is performed (eg. file save, user added)</li>
    <li class="p-list__item is-ticked">An update or more information on the system is available</li>
    <li class="p-list__item is-ticked">Anything that does not pertain to an Applet, both first-party and third-party</li>
</ul>