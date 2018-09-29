---
title: Stop errors
---
# Stop errors
Stop errors (red screens of death) are system-wide errors that occur when a problem with the operating system has been reached. These errors are similar to ones found in Windows 8 and can be customised to the developer's needs.
![Standard boot screen](../media/img/rsod/default.png)

<div class="p-notification--information">
  <p class="p-notification__response">
    <span class="p-notification__status">Error Databaswe:</span>Users of AliceOS can now search for the respective Stop error on the AliceOS Error Database, a collective database by the AliceOS team and third-party OEMs. We recommend searching for the error in the database than here.
  </p>
</div>

<p><a href = "https://errordb.aliceos.app" class = "p-button--brand p-link--external">View Error Database</a></p>

## Typical causes of Stop errors
These may or may not apply to each Stop error, but these are common causes for such errors.

- SEAlice may have been not properly implemented into the AliceOS distribution.
- The user failed to agree to the license terms of AliceOS or the game that AliceOS is bundled with.
- The script may have called an area that doesn't yet exist or broke in a way that Ren'Py doesn't detect.
- A component needed for a system action was not initialized or made accessible.

## Customizing Stop errors
![Standard boot screen](../media/img/rsod/custom.png)

To call a Stop error at any point in your visual novel project, run `call screen ThrowASError()`.

### `ThrowASError(error_type)`
Throws a Stop error and restarts the game.

- error_type - the Stop error code to be displayed. AliceOS comes with three defaults, but additional ones can be added in OEM settings or directly called in the function.

#### Live example
<pre><code class = "prettyprint lang-py">
call screen ThrowASError("PAGE_FAULT_IN_NON_PAGED_AREA")
</code></pre>

### Customizing looks
Fonts are automatically pulled from OEM settings and will be applied when OEM mode and custom font mode is enabled.

The background is provided in `Resources/rsod_overlay.png`. We recommend setting your base background as Strawberry 500 (`#c6262e`).