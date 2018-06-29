<!--![AliceOS Logo](https://dokidokialice.marquiskurt.net/assets/img/aliceos_logo.png)-->

# Home
Welcome to the official documentation for the AliceOS project. AliceOS is an independent, open-source project that brings a virtual operating system into Doki Doki Literature Club! as a mod and to Ren'Py projects as a framework. AliceOS is also the core operating system used in _Doki Doki: The Angel Returns_.

## Download and installation
> Note: If you wish to use AliceOS on any Ren'Py project with a different SDK version from 6.99.12.4, you might want to grab a copy of the source code instead.

There are two ways to handle the download and installation of AliceOS into any project.

### Using AliceOS.rpa (Recommended)
1. Select the download for `AliceOS.SinglePackage.zip`.
2. Navigate to the `game` folder of your Ren'Py project.
3. Extract the contents of `AliceOS.SinglePackage.zip` into the game folder.

### Using the source code
Downloading the source version of ALiceOS may prove useful if you are using a different version of the Ren'Py SDK or want to expand on AliceOS's capabilities for your needs.

1. Select the download for `Source code.zip` or `SOurce code.tar.gz`.
2. Navigate to the `game` folder of your Ren'Py project.
3. The following folders will need to be copied to the `game` folder: `Resources`, `CoreServices`, `Frameworks`, `Applets`.
4. Run your Ren'Py project to compile the `.rpyc` versions of the files accordingly.

## Adding the AliceOS boot screen
The AliceOS boot screen helps inform users that you've added AliceOS to your project. There are two versions of the boot screen you can use:
* **Standard** (`default_boot_screen`) - the traditional AliceOS boot screen.
* **OEM (Partner)** (`oem_boot_screen`) - a version of the boot screen that displays "Powered by AliceOS" rather than the traditional boot screen.

The boot screens are labels with proper scenes. We recommend either adding this to the beginning of your `script.rpy` before the game starts or right before your `splashscreen`.