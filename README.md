# Deck Suspender

This is a plugin to suspend/resume games and apps on the Steam Deck using the [SteamOS Plugin Loader](https://github.com/SteamDeckHomebrew/PluginLoader).

## Usage
1. Follow the [Plugin Loader installation instructions](https://github.com/SteamDeckHomebrew/PluginLoader)
2. `git clone` this repository into the `/home/deck/homebrew/plugins` folder on your Steam Deck: ```cd /home/deck/homebrew/plugins && git clone https://github.com/safijari/DeckSuspender.git```
3. Run the `install_psutil.sh` script: `/home/deck/homebrew/plugins/DeckSuspender/install_psutil.sh`
4. Go to the Plugins tab in the Steam Deck's quick access menu and the plugin should show up there
5. (You'll probably need to hold Steam and touch the right trackpad to get into mouse mode for this) Click on the plugin, and it will list the running processes, click any of the process to pause/resume it.

## Why
I find myself wanting to use the Deck for other purposes (e.g. managing downloads or browsing the web or some times, yes, playing some other game) while I'm taking a break from a game and instead of having to get to a suitable stopping point or losing progress, this appraoch lets me just put the current game to sleep.

## Caveats
1. This may not work with all programs. It has so far with everything I've tried but even the regular suspend/resume on the Deck fails in some cases (e.g. AC Valhalla)
2. When an app is suspended, its CPU load is 0 but whatever RAM it was already consuming remains the same. If you're using this to hotswap between two games be careful, as that opens you up to running out of RAM.
3. App names look weird right now and may not make sense some times. Any suggestions on how to get a more representative name would be much appreciated
4. I don't know how this will interact with play time logging. More than likely the suspended time will be considered active time.