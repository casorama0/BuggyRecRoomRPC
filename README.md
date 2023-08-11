# BuggyRecRoomRPC
An extremely buggy Rec Room rich presence client I made. It is NOT feature-rich and it only shows the bare minimum amount of information. This is mainly a place for me to store my newbie-level code, so expect minimal maintenance of this.

## Prerequisites
* This program directly depends on RecNet's matchmaking API, so authorization is needed to utilize it:
  * You MUST have [RecNetLogin's](https://github.com/Jegarde/RecNet-Login) source code in the same directory as your download; you must have RNL's dependencies installed, as well.
  * You MUST follow [RecNetLogin's setup instructions](https://github.com/Jegarde/RecNet-Login#setup).
  * Use `pip install -r requirements.txt` to install additional requirements.

## Configuration
* Double-check that the prerequisites are satisfied! If RecNetLogin is not present in the program's directory, then the program will not work AT ALL.
* This program requires minimal configuration. Upon the first startup of the program, you should be prompted to enter your username. After entering your username, you should not be asked again. You can prompt the program to ask for your username again by deleting the `accountInfo.json` file or clearing all contents of it.


## Usage
After configuration, you should be able to run the program without issue. Since I don't care too much about this, there is little to no error handling, if it stops unexpectedly and spews a bunch of stuff, ensure you are logged in on Rec Room and Discord is running, then restart the program. While the program is running, your Discord status should look similar to this: 
<br><br>
![image](https://github.com/ayocaso/BuggyRecRoomRPC/assets/91983138/6eb2d8cf-b234-483d-9992-a3e7a282e98c)

sorry to anybody who reads the awful source code ;)
