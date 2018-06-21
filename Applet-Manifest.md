Every applet contains a manifest and essential function list as a Python class of the object `Applet`. This manifest provides data such as applet names, authors, icons, and the permissions required.

## Applet Template
The [Applet Template](https://github.com/TheAngelReturns/aliceos-applet) provided by the AliceOS Team provides a structure that can be followed to create a working Applet with proper manifest data. Aspiring AliceOS applet developers should start with the template before creating their own classes and applets from scratch.

## The `Applet()` class
The `Applet()` class is provided as a Framework for AliceOS and consists of important data that is needed for AliceOS to render notifications, list itself in the Control Center, and add icons to the desktop shell.

### Basic Applet Information
By default, all AliceOS apps must contain the following information:

- `short_name`: The short name for the applet
- `long_name`: The full name for the applet
- `app_dir`: The directory in which your applet resides in relative to the Applets folder
- `author`: The author of the applet, primarily the developer or developer team
- `version`: The semantic version of the applet (ex.: `0.1.0`)
- `description`: A short desription containing the applet's primary functionality

### Declaring App Icons
Icons remain a key part of the AliceOS applet experience. It is recommended that you make the sizes for your icon appropriately and not merely downscale. The delcaration is as follows:

```python
icons = {
            16: "16.png",
            24: "24.png",
            32: "32.png",
            64: "64.png",
            128: "128.png",
            256: "256.png"
        }
```

### Setting App Permissions
AliceOS enforces a strong security system that requires apps to declare what permissions it will need. This is done in a list called `permissions`.

- `pm_notify` - Send notifications to the user
- `pm_files` - Access the file system outside of the user's Home folder
- `pm_admin` - Modify system settings

### Other Functions
Most Applets will make use of two functions present:

- `ask_app_permissions()` - Overtly asks the user permission for the specified items in the `permissions` list.
- `send_temporary_notification(sender, contents, action)` - Sends a banner notification built upon the `banner()` screen.

---
**Maintainer:** Marquis Kurt (@alicerunsonfedora)