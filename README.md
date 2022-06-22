# Deck Suspender

This is a plugin to suspend/resume games and apps on the Steam Deck using the [SteamOS Plugin Loader](https://github.com/SteamDeckHomebrew/PluginLoader).

## Usage
1. Follow the [Plugin Loader installation instructions](https://github.com/SteamDeckHomebrew/PluginLoader)
2. `git clone` this repository into the `/home/deck/homebrew/plugins` folder on your Steam Deck: ```cd /home/deck/homebrew/plugins && git clone https://github.com/safijari/DeckSuspender.git```
3. Run the `install_psutil.sh` script: `/home/deck/homebrew/plugins/DeckSuspender/install_psutil.sh`
4. Go to the Plugins tab in the Steam Deck's quick access menu and the plugin should show up there
5. (You'll probably need to hold Steam and touch the right trackpad to get into mouse mode for this) Click on the plugin, and it will list the running processes, click any of the process to pause/resume it.