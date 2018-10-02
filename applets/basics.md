---
title: Applet Basics
---
Applet Basics
=============

Applets are the core of the AliceOS system. Applets generally interact with the frameworks and services provided. They usually either add extra functionality to the system itself or enhance the gameplay of a visual novel. These self-contained applets are relatively easy to install and configure and follow a standard protocol.

<div class="p-notification--information">
    <p class="p-notification__response">
        <span class="p-notification__status"></span>For aspiring developers, we've provided an <a href="https://github.com/ProjectAliceDev/aliceos-applet">applet template</a> to get started with making applets quickly and easily.
    </p>
</div>

Structure
---------

Applets follow a generic structure that makes use of existing AliceOS file structures.

The overall structure of an applet in AliceOS looks like this:

    game/
        Applets/
            AppletName/
                AppletName.rpy
                src/
                Resources/
                    icons/
                        16.png
                        24.png
                        32.png
                        48.png
                        64.png
                        128.png
                        256.png

The Applet itself, as well as its manifest, is located in its source code. Additional source code such as libraries or extra files are located in the `src` folder, usually. Additional resources such as applet icons, images, etc., are located in the `Resources` folder.

Manifest
--------

Every applet contains a manifest and essential function list as a Python class of the object `Applet`. This manifest provides data such as applet names, authors, icons, and the permissions required.

### The `Applet()` class

The `Applet()` class is provided as a Framework for AliceOS and consists of important data that is needed for AliceOS to render notifications, list itself in the Control Center, and add icons to the desktop shell.

#### Basic Applet Information

By default, all AliceOS apps must contain the following information:

-   `short_name`: The short name for the applet
-   `long_name`: The full name for the applet
-   `app_dir`: The directory in which your applet resides in relative to
    the Applets folder
-   `author`: The author of the applet, primarily the developer or
    developer team
-   `version`: The semantic version of the applet (ex.: `0.1.0`)
-   `description`: A short description containing the applet's primary
    functionality

#### Declaring App Icons

Icons remain a key part of the AliceOS applet experience. It is recommended that you make the sizes for your icon appropriately and not merely downscale. The delcaration is as follows:

<pre><code class = "prettyprint lang-py">
icons = {
            16: "16.png",
            24: "24.png",
            32: "32.png",
            64: "64.png",
            128: "128.png",
            256: "256.png"
        }
</code></pre>

#### Setting App Permissions

AliceOS enforces a strong security system that requires apps to declare what permissions it will need. This is done in a list called `permissions`. When the user verifies these permissions, they are either stored in the `persistent` file of your Ren'Py game. More information on applet security can be found in the [Applet security documentation page](security.md).

-   `pm_notify` - Send notifications to the user
-   `pm_files` - Access the file system outside of the user's Home
    folder
-   `pm_admin` - Modify system settings
-   `pm_shell` - Lauch applets in the AliceOS system

The `permissions` list uses the `short_name` of the Applet as a prefix. For instance, the entry for notifications for an applet called "Cyanogen":

<pre><code class = "prettyprint lang-py">
persistent.aliceos_permissions["Cyanogen_notify"]
</code></pre>

#### Launcher capabilities
For applets that act as desktop shells, the `launch` properties make it easier to access launching functions:

<pre><code class = "prettyprint lang-py">
launch = {
    "action": "Return(0)",
    "show_in_launcher": True
}
</code></pre>

- `action` - The action that launches the applet
- `show_in_launcher` - Determines whether the applet should be included in the Applet list

## Default Functions

Most Applets will make use of two functions present:

#### `ask_app_permissions()`
Overtly asks the user permission for the specified items in the `permissions` list.

#### `send_temporary_notification(sender, contents, action)`
Sends a banner notification built upon the `banner()` screen.

- `sender` - the title or the "sender" of the banner
- `contents` - the message or description to be displayed
- `action` - the action when user presses "Respond"

