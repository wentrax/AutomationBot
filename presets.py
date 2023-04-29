class Presets(object):
    FILE_TYPES = ["photo", "animation", "document", "video", "audio"]
    WELCOME_MSG = "Hello <b>{}</b> 👋,\n<code>I can remove duplicate media files from your chat. For more, click on the help button.</code>"
    HELP_MESSAGE = """
By using this bot you can delete duplicate media in target chat.

The bot is only an interface to do the process, while the user is doing the deleting job. The bot doesn't need to be in the chat.

The user must be an admin with the <b>Delete Messages</b> privilege in the target chat.

Supported media are <b>document, video, photo, animation, and audio file.</b>

Duplicate Media counter and current message-id will be displayed in the UI with the process cancel button.

<b>The list of Admin commands is:</b>
/chat -100xxxxxxxxxx - <i>Set the target chat</i>
/delay 10 - <i>10 second delay</i>
/purge - <i>Delete duplicate media</i>


 𝐅𝐢𝐥𝐞𝐬 𝐟𝐨𝐫𝐰𝐚𝐫𝐝 𝐡𝐞𝐥𝐩
This Bot forward all files from One Public channel to Your Personal channel

<b>Follow These Steps!!</b>
<b>• Currectly fill your Config vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>
<b>• Then give admin permission in your personal telegram channel</b>
<b>• Then send any message In your personal telegram channel</b>
<b>• Then use /start_forward command in your bot</b>
<b><u>Available Command</b></u>
* /start_forward - <b>start forward</b>  

 𝐀𝐮𝐭𝐨 𝐅𝐢𝐥𝐭𝐞𝐫 𝐇𝐞𝐥𝐩
<i>
* Add user account to your channel !
* Add bot to group with admin rights.
* Once deployed and bot is started, send a message to channel (must do step)
* Bot will work now :)
No need add each filter again!
Bot will automatically search for your file and give links to that!
</i>
    """
    WAIT_MSG = "<b>Please wait...</b>"
    NOT_AUTH_TXT = "<b>You are not Authorized !</b>"
    CHECKING_MSG = "<i>Looking for Duplicates..</i>"
    CANCELLED_MSG = "<b>Purging Cancelled by user</b>"
    NO_DUPLICATES = (
        "<b>Congrats</b> 🎉\nThere are <b>no duplicate</b> media in the target chat."
    )
    DELAY_CNF = (
        "<b>Success</b> ✅\nA Delay of <b>{} Seconds</b> will be applied in the process."
    )
    INVALID_DELAY = (
        "<b>Error</b> ❎\nInput must be in the format of\n>>  <code>/delay 10</code>"
    )
    CHAT_ID_CNF = "<b>Success</b> ✅\nChat id <code>{}</code> saved !\n\nYou can now execute /purge command."
    NOT_IN_CHAT = "<b>Error</b> ❎\nThe user is not a member of the target chat. Join the target chat as an admin, and try again later."
    INCORRECT_PERMISSION = "<b>Error</b> ❎\nthe user is not an admin or doesn't have the privilege to delete messages in the target chat."
    INVALID_CHAT = "<b>Invalid Input</b> ❎\n<Input must be in the format of\n<code>/chat -10025486542156</code>"
    DELETING_MSGS = """
<b>Messages deleted   : {}</b>
\xad                                                                 \xad
<b>Message id covered: {}</b>
    """
    CANCEL_TEXT = "\xad          Click to cancel          \xad"
    PROCESS_FINISHED_TEXT = "<b>Success</b> ✅\nAll duplicate media were deleted."
    PROCESSING_MSG = "<b>Please wait...</b>\nThis will take some time to find the duplicates. Have a cup of coffee by the time I'll finish it off!"
    PURGE_ERROR = (
        "<b>Error</b> ❎\nConfigure the target chat first by using the /chat command."
    )
