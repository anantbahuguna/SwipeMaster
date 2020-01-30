# SwipeMaster - 
<p>A tinder bot made using python</p>
   
   <img src='logo.jpg' height='150' style='border-radius: 50px'>
    <br/>

## Dependencies Required:

1. chromedriver

- Download zip file from <https://chromedriver.chromium.org/>
- Extract the zip file
- Write the following command in terminal-
  ```
  mv ~/Downloads/chromedriver /usr/local/bin
  ```

2.  selenium

    ```
    pip install selenium
    ```

## Steps to run the Bot:

1. Enter your facebook credentials in the secrets.py file
2. Run the command-
   ```
   python -i tinder-bot.py
   ```
3. Once it logs into tinder, write the following command in the python interpreter-
   ```
   bot.auto_swipe()
   ```
