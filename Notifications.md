Notifications provide a level of interactivity and information updates for your Ren'Py project. The notification system built into AliceOS contains screens for both the native and custom functions regarding dialog and notification management.

![Permissive Alerts](https://imgur.com/quWQALX.png)
> A permissive alert.

## Types of notifications
There are multiple types of notifications that take inspiration from the way notifications are handled on iOS:
* _Banners_ provide a temporary pop-up at the top of the screen that has the option for a response before hiding itself after five seconds.
* _Alerts_ provide a message that requires an action, usually by pushing a button. They can be terse or have details with a title and message.
    * _Permissive alerts_ are alerts that require the player to grant access to parts of the AliceOS system. These usually include sending notifications, modifying the file system, and changing system settings.

| Alerts | Banners |
| --- | --- |
| ![Alerts](https://imgur.com/lGlEmZu.png) | ![Banners](https://imgur.com/kKpx6ji.png) |

## Sending notifications
### App manifest requirements
If you plan to have your AliceOS app send notifications, you need the following information in your app's manifest (provided is an example):
```renpy
# Provide a short name and a long name for your app.
define ddlc_short_name = "DDLC"
define ddlc_name = "Doki Doki Literature Club!"

# Define your icons here. They should be located in Resources/icons/
define ddlc_icon_24 = "ddlc_24.png"
```
### Notification screens
If you commonly use a particular notification, you may want to wrap your call statement in a label:
```renpy
label test_alert:
    call screen alert("This is an alert", "Press OK to dismiss this alert.", ok_action=Return())
    return
```
#### `alert(title, message, ok_action)`
Presents an alert to the user that requires an action.
* `title` - the main message
* `message` - the details or relevant information
* `ok_action` - the function called when user presses OK

```renpy
call screen alert("File Not Found", "The file specified could not be found.", ok_action=Return(1))
```

#### `confirm_alert(title, message, no_action_message, no_action, yes_action_message, yes_action)`
Presents an alert that requires the user to make a choice.
* `title` - the main choice text
* `subtitle` - the details or relevant information to the choice
* `no_action_message` - the negative button's text (placed on left)
* `no_action` - the function called when user presses negative button
* `yes_action_message` - the positive button's text (placed on right)
* `yes_action` - the function called when user presses positive button
> If you are asking the user permission to perform a function, use `ask_permission` instead.

```renpy
call screen confirm_alert("Do You Want To Run Alice32?", "Running this software may harm the AliceOS system.", "Don't Run", no_action=Return(1), "Run Anyway", yes_action=Return(0))
```

#### `ask_permission(app_name, action, no_action, yes_action)`
Asks the user permission to perform an action or to access a system-related function.
* `app_name` - the name of your app
* `action` - the action that requires permission:
    * `allow_un` - send notifications to the user
    * `allow_fs` - access the AliceOS file system beyond the Home directory
    * `allow_sip` - modify system settings or gain system control
* `no_action` - function called when user presses Don't Allow
* `yes_action` - function called when user presses OK

```renpy
call screen ask_permission(ddlc_name, allow_fs, no_action=Return(1), yes_action=Return(0))
```

#### `banner(applet, title, message, response)`
Presents a temporary banner at the top of the screen. Automatically dismisses after five seconds and returns a value of `0`.
* `applet` - the applet sending the notification
* `title` - either the sender or the main message
* `message` - the message or details
* `response` - function called when the user presses Respond
> If you need something "quick n' dirty", you can also make use of `renpy.notify()`; however, you won't have the same control as `banner()`.

```renpy
call screen banner(ddlc, "You're all set!", "You now will receive notifications in the game.", response=Return(1))
```

---
**Maintainer:** Marquis Kurt (@alicerunsonfedora)