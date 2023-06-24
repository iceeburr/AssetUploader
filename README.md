<h1 style="text-align: center;"><a href="https://github.com/iceeburr/AssetUploader">Asset Uploader</a></h1>

> This project was originally created for my Video Player Module. If you want more in-depth documentation, please refer to the [post on the Roblox Developer Forum.](https://devforum.roblox.com/t/video-player-v10-play-your-own-video-inside-roblox-full-resolution-fps-and-audio/2423381)

## Overview

**This simple [Python](https://www.python.org/) script will suit you if you want to upload a large amount of assets to Roblox. It uses a third-party library called [rblx-open-cloud](https://github.com/treeben77/rblx-open-cloud). Simply clone the repo, put your files inside the folder, change your `API_KEY` and you are good to go! The script will automatically save the IDs of each asset to an `output.txt` file.**

## Code Usage
*For more in-depth documentation, refer to [this](https://devforum.roblox.com/t/video-player-v10-play-your-own-video-inside-roblox-full-resolution-fps-and-audio/2423381).*

First of all, clone the repo to a folder. Also, make sure you have [Python](https://www.python.org/) and [pip](https://pypi.org/project/pip/) installed.

We will now install the packages we need. Open a command prompt and navigate to the directory where you cloned the repo. [Tutorial here if you struggle](https://www.youtube.com/watch?v=8-mYKkNzjU4).
Enter `pip install -r requirements.txt` and wait for it to install.

Now put all the assets you need in the files folder.
> Make sure you only have the assets that you choose from the script. For example, if you are going to upload images, then pick decal in the script and only put .png or .jpg files in the folder. The script will error if it tries to upload a file of a different type (e.g., you tried to upload audio as a decal).

*If you are looking for instructions on how to extract each frame from an image from a video, please refer to [this Tutorial](https://www.youtube.com/watch?v=NIzWZg02kHU).*

Open `main.py` in any text editor you are comfortable with. On the very top, you will see this:
```py
creator = rblxopencloud.Group("USER_ID/GROUP_ID", api_key="API_KEY")
```
First, input the owner under `USER_ID/GROUP_ID`. If you don't have a group, change `rblxopencloud.Group(` to `rblxopencloud.User(`.

* `GROUP_ID` - The ID of the group owning the API_KEY.
* `USER_ID` - The ID of your account, found on the profile page.

Now change `"API_KEY"` to your key. If you don't have one, follow [this guide](https://create.roblox.com/docs/cloud/open-cloud/managing-api-keys). Make sure not to share it, because anyone with that key can publish assets on your behalf and get your account banned in seconds. Make sure to have both read and write permissions under the Asset API scope. Add `0.0.0.0/0` as the IP address, unless you know what you are doing.

If you did everything correctly, now you can simply enter `python main.py` while in the directory of the script, and it will start running.

## Additional Information

The script will save all new AssetIDs in `output.txt` located in the directory of the script. This is useful if you need to get all the IDs. If your script errors, then that means something wrong might have happened. In most cases, that would be because your account was moderated (banned). The script will automatically save all progress to the output, regardless of the error. Unfortunately, you will have to manually remove all old assets that were already uploaded. Just double-check your files to see if they might violate anything. If you think they would, manually upload them from an alternate account. If an output file already exists, the script will ask you if you want to continue. **IT WILL AUTOMATICALLY WIPE ALL CONTENTS OF THAT FILE!!!** Always back up your progress.
If it errors with HTTP 400 then that means your asset name or description was moderated. Change it to "Example Asset" or anything static that can't be moderated.

## I am not responsible for your actions!
**Anything you do with this script is on your behalf. I have nothing to do with any illegal actions. This script should not be abused, even if it does not violate any community standards or terms of service. This is the generic way developers would upload an asset remotely; this is why the Open Cloud API exists in the first place. Do not blame me for any moderated assets; this is purely your issue. I have been banned many times myself, so always use an alt account!**

#### For any suggestions, issues, or general questions, feel free to open an issue, pull a pull request, or just hit me up on Discord or the Roblox Developer Forum.
#### This project is licensed under [MIT](https://en.wikipedia.org/wiki/MIT_License).