Applets make up the app ecosystem for AliceOS. Applets are how third-party developers add additional functionality to AliceOS and interact with users and players. Applet follow a generic structure that makes use of existing AliceOS file structures.

## What's needed
- App code (generally stored as a .rpy or .rpyc)
- App icons (see the [icon guidelines](Icon-Guidelines))

> Ensure that you are using Ren'Py 6.99.12.4 to ensure compatibility with AliceOS and games like Doki Doki Literature Club!

## Structure
The overall structure of an applet in AliceOS looks like this:
```
game/
	Applets/
		AppletName.rpy
		AppletName.rpyc
	Resources/
		icons/
			applet_16.png
			applet_24.png
			applet_32.png
			applet_64.png
			applet_128.png
```
Applets are stored in the `Applets` folder, either as compiled RenPy scripts or as the original source code (compiled at runtime). App icons are stored in `Resources/icons` under multiple sizes.

We've provided an applet template on GitHub that developers can use to quickly get started without worrying about setting up the structure. [Get the template here &rsaquo;](https://github.com/TheAngelReturns/aliceos-applet)

---
**Maintainer:** Marquis Kurt (@alicerunsonfedora)