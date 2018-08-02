---
title: Stop errors
---
## Stop errors
Stop errors (red screens of death) are system-wide errors that occur when a problem with the operating system has been reached. These errors are similar to ones found in Windows 8 and can be customised to the developer's needs.
![Standard boot screen](../media/img/rsod.png)

### Typical stop errors
- `INACCESSIBLE_BOOT_DEVICE` - the file required to start the integrity check process is missing.
- `ERR_SEALICE_LOCK` - one or more of the SEAlice components are missing.
- `ERR_GOBFADU_LOCK` - one or more of the GOBFADU components are missing.
- `ERR_OS_LOCK` - one or more core operating system files are missing.
- `ERR_GUI_LOCK` - one or more of the interface-drawing files are missing.
- `ERR_FRAME_LOCK` - see `ERR_GUI_LOCK`.
- `ERR_RESOURCE_LOCK` - one or more of the SEAlice components are missing.
- `ERR_APPLET_LOCK` - one or more of core applet files are missing.
- `ERR_TEST_LOCK` - one or more of the testing components are missing. This should never appear to the user.

<div class="p-notification--caution">
    <p class="p-notification__response">
        <span class="p-notification__status">Deprecation warning:</span>Some of these Stop errors may be removed with the implementation of SEAlice.
    </p>
</div>
