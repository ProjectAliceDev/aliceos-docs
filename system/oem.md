---
title: OEM settings
---
# OEM Settings
AliceOS allows distribution managers and manufacturers to easily change settings and properties of AliceOS in addition to modifying its source code. In the `Resources` directory, manufactureres can edit the `OEMSettings.rpy` file to achieve this.

## General information
In order to enable the OEM mode and its settings, the following needs to be filled in.

- `aliceos.oem_mode` - Whether the OEM mode should be turned on or off. Default is False.
- `aliceos.oem_name` - The OEM's name.
- `aliceos.oem_website` - The OEM's website.
- `aliceos.oem_support` - The email address to which the player can contact for questions regarding the custom distribution of AliceOS.

## Custom fonts
For each of the respected variants of AliceOS's fonts, variables exist to acommodate them. Their values should equal the path of where the font file is located in the `game` folder. For example:

<pre><code class = "prettyprint lang-py">
define aliceos.oem_font_regular = "Resources/systemfont/OEM/Regular.ttf"
</code></pre>

AliceOS will replace the default system font with the ones provided by the OEM if OEM mode is enabled.