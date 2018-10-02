---
title: Distribution
---
# Distributing AliceOS
AliceOS is fully supported when testing and developing Ren'Py projects. However, some Ren'Py options configurations may not fully support packaging AliceOS components into the final game.

## Editing Options
To add AliceOS to the build's artifacts, add the following lines to your `options.rpy`:

<pre><code class = "prettyprint lang-py">
# Classify AliceOS files as AliceOS
build.classify("game/Applets/**", "aliceos")
build.classify("game/CoreServices/**", "aliceos")
build.classify("game/Frameworks/**", "aliceos")
build.classify("game/Resources/**", "aliceos")

# Package AliceOS as an RPA
build.archive("aliceos",build.name)
</code></pre>

Alternatively, if developers want to bundle AliceOS by other means, note that the core folders must be included in the build.

## DDLC Mod Template
![DDLC](https://cdn-images-1.medium.com/max/2000/1*iRvm-m-wMuufrKn0V1xBmw.png)

For those that are making modifications to _Doki Doki Literature Club!_, we recommend grabbing the DDLC Mod Template maintained by Project Alice. This flavor already imports the bootloader and adds the proper options to package AliceOS as a part of the game.

[Get the template &rsaquo;](https://github.com/ProjectAliceDev/DDLCModTemplate)