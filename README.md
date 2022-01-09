# Android Cleaner
Almost every Android Device comes with programs that the OEMs don't want their customers to disable. Trouble is, these programs are garbage and we can always find better alternatives in the Google Play Store. Android Cleaner helps in disabling these useless programs.

## Compilation
```bash
$ make build
```

## How to Use
1. You will need to install **Package Name** on your Android Device. [Link](https://play.google.com/store/apps/details?id=com.csdroid.pkg)
1. In **Package Name**, select all the applications that you would like to disable
1. Copy this selection and transfer it your Phone. [Google Keep](https://play.google.com/store/apps/details?id=com.google.android.keep&hl=en) works quite well for this job.
1. The copied package details will be in the following form
```
app:Some App
package:com.developer.softwarename
Launcher:null
```
1. Create a text file and paste the copied package details
1. Connect your Android Device to your computer and enable **USB Debugging** under **Developer Options** menu
1. Run the following command
```bash
$ android-cleaner -file <package list>
```
1. Packages will be disabled on your Android Device
1. Enjoy a Bloat-free Android Experience

## FAQ
### Why Disable and not Remove?
Disabled applications can be easily re-enabled from the Device Settings should the need arise. This makes it a safer option compared with complete removal.

### How Does it Work?
Android Cleaner uses the Android Debug Bridge (ADB) to perform its interactions with your device. **ADB needs to be installed on your system before you can use this program**.
