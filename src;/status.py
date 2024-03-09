import pypresence
import time

def set_discord_status():
    RPC = pypresence.Presence(client_id="1120412154080800929") # Replace "YOUR_CLIENT_ID" with your actual Discord application's client ID

    RPC.connect()

    activity = {
            "state": "Farming Story",
            "details": "V1.0.0",
            "large_image": "goku_image",
            "large_text": "Godku Farm BOT",
            "buttons": [
                {"label": "Godku Project!", "url": "https://discord.gg/sPygFGGn"}
            ]
        }

    RPC.update(**activity)

    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        RPC.close()

if __name__ == "__main__":
    set_discord_status()
