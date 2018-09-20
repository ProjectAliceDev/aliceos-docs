---
title: Boot Screens
---
# Boot Screens
The boot screen is an important part of any AliceOS project; the boot screen checks the integrity of some parts of the system and informs the user that he/she is using AliceOS.

![Standard boot screen](../media/img/sbs.png)


## Implementation
To incorporate this into your project, add the following lines to the beginning your `splashscreen` label:
<pre><code class = "prettyprint lang-py">
call bootloader
</code></pre>

The project, depending on your settings in `OEMSettings.rpy`, will determine which boot screen to display.
