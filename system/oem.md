---
title: OEM settings
---
# OEM Settings
AliceOS allows distribution managers and manufacturers to easily change settings and properties of AliceOS in addition to modifying its source code. In the `Resources` directory, manufacturers can edit the `OEMSettings.rpy` file to achieve this.

## General information
In order to enable the OEM mode and its settings, the following needs to be filled in.

- `aliceos.oem_mode` - Whether the OEM mode should be turned on or off. Default is False.
- `aliceos_oem_info` - Field for entering in provider details. An example is provided below:

<pre><code class = "prettyprint lang-py">
oem_info = """\
OEM Name: Aperture Laboratories
OEM Website: https://aperturescience.com
OEM Support Email: contact@aperturescience.com

For distribution with Aperture Science products only. If this policy is violated, please contact the support team with the email address above.
"""
</code></pre>

## Licenses
AliceOS generally displays two license agreement prompts: the standard GNU GPL license for the platform and an OEM's agreement, usually describing the game's nature (eg. disclaimers, IP guidelines, etc.). To write your license, edit the license field:

<pre><code class = "prettyprint lang-py">
license = """\
No license found.
"""
</code></pre>

If you do not wish to add an additional license, simply leave the field to its default value, `No license found`.

## Custom fonts
By default, custom fonts are disabled. To enable them, set `aliceos.oem_use_custom_font` to `True`. Note that you'll need to have your font files in `Resources/systemfont/OEM/` and they must be TrueType fonts.

```
Resources/systemfont/OEM/Regular.ttf
Resources/systemfont/OEM/Bold.ttf
Resources/systemfont/OEM/Italic.ttf
Resources/systemfont/OEM/Black.ttf
Resources/systemfont/OEM/Medium.ttf
Resources/systemfont/OEM/Thin.ttf
...
```

If you want the font to appear larger in the [Setup assistant](pisa.md), set `aliceos.oem_large_pisa_font` to `True`.