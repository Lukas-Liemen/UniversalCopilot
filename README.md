# Universal Copilot
Hey there! I've been tinkering on something inspired by GitHub Copilot, but aiming for even broader uses. It’s built around Google’s gemma-7B language model and deployed using FastAPI on Google Colab. I’ve also integrated a local script that responds to a key combination, allowing for dynamic processing of clipboard content.

## Overview
This setup effectively transforms your clipboard into a direct line to an AI model. Press a specific key combination (ctrl + shift + L, change it to what you like though), and the contents of your clipboard are sent to the gemma-7B model. The AI then responds, and its output is typed out wherever your cursor is.

## How It Works
1. **Server Side:** I host the FastAPI application on Google Colab. This is where the gemma-7B model processes incoming text. The code it not fixed on this specific model, you can basically change it to any model you want to.
   - **Note:** You'll need to fill in your ngrok authentication token
   - **Note:** You'll need to fill in a SHA-256 representation of the API key that you want to use to allow the client to connect to your server

2. **Local Script:** A background script on your local machine listens for a predefined key combination. When activated, it sends the clipboard's content to the server and handles the response.
   - **Note:** Enter the URL of your server in the `model.py` script where indicated. The URL should be printed to your server code once it is running.
   - I drew inspiration from: https://gist.github.com/SalihTalha/8b9be8662f239ffbac4b31b2022288ea to employ FastAPI on Colab. 

3. **Clipboard Interaction:** Upon pressing the designated keys, the script captures the last content on the clipboard, sends it to the API, and the response is automatically input back into your active application.
   - **Note:** You may want to tweak the key combination in `keylogger.py` to fit your preference.

This approach allows you to summon AI assistance into any application. Whether you're coding, writing emails, or drafting documents.

## Example
![](https://github.com/Lukas-Liemen/UniversalCopilot/blob/main/example.gif)
