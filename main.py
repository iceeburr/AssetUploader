import rblxopencloud
import os
from pathlib import Path
assetIDsArray = []

creator = rblxopencloud.Group("USER_ID/GROUP_ID", api_key="API_KEY") # Change this to your API key. Don't forget to change the Group ID as well. If you use your own account change .Group to .User and Group ID would be your User ID.

def uploadAsset(currentFile):
    with open(currentFile, "rb") as file:
        asset = creator.upload_asset(
            file, rblxopencloud.AssetType.Decal, "Example Asset", "Decal Description" # Make sure your file names don't contain anything that can get moderated, if it does you will get HTTP 400 error. Use "frame00001" or something similar. Make sure to change your asset type to what you are uploading. .Decal for images, .Audio for audio files and .Model for models.
        )
        if isinstance(asset, rblxopencloud.Asset):
            print(asset.id, Path(currentFile).stem)
            assetIDsArray.append(asset.id)
        else:
            while True:
                status = asset.fetch_status()
                if status:
                    print(status.id, Path(currentFile).stem)
                    assetIDsArray.append(status.id)
                    break

def mainFunction():
    content = "local FrameIDs = {\n"
    fileDirectory = './files' # If your directory is named differently please edit this.
    for fileName in os.scandir(fileDirectory):
        if fileName.is_file():
            try:
                uploadAsset(fileName.path)
            except Exception as e:
                if len(assetIDsArray) == 0:
                    print(e)
                    exit("There was an error. No files have been uploaded. Are you sure you entered the correct ID and Key?")
                for i in range(len(assetIDsArray)):
                    content += "   " + str(assetIDsArray[i]) + ",\n"
                content += "}"
                with open('./output.txt', 'w') as file:
                    file.write(content)
                    file.close()
                print(e)
                exit("Something went wrong. Your image might have been moderated. All images have been saved to output.txt. Please read the error. If your content was moderated then you will have to check that out yourself.")

    if len(assetIDsArray) == 0:
        exit("No files have been uploaded. Are you sure you have any files in the folder?")
    for i in range(len(assetIDsArray)):
        content += "   " + str(assetIDsArray[i]) + ",\n"
    content += "}"

    with open('./output.txt', 'w') as file:
        file.write(content)
        file.close()
    print("The code ran successfully, all image ID's should be in the file output.txt. Good luck!")

if os.path.exists('./output.txt'):
  print("You currently have a output.txt file. If you continue it will be deleted completely and you won't be able to recover it's contents.")
  inputOutput = input("Do you want to continue? [Y/N] ").lower()
  if inputOutput == "y":
      os.remove('./output.txt')
      mainFunction()
  elif inputOutput == "n":
      exit()
  else:
      exit('That is not a valid answer! Please pick between "Y" (Yes) and "N" (No).')
else:
  print("No output.txt was detected. A new file will be created in the home directory of the python file.")
  inputOutput = input("Do you want to continue? [Y/N] ").lower()
  if inputOutput == "y":
      mainFunction()
  elif inputOutput == "n":
      exit()
  else:
      exit('That is not a valid answer! Please pick between "Y" (Yes) and "N" (No).')