# Test tasks for Allot

1. Tasks 1 and 2 are located in file "Task1-2.md" in the root of repository
2. Tasks 3.1, 3.2 and 3.3 are located in "src/" folder ("task3-1.py", "task3-2.py", "task3-3.py")
3. Clone the repository with the command:

    ```
    git clone https://github.com/vladimir-grigoriev/task_for_allot.git
    ```
4. In the root folder create `venv`
    ```
    python3 -m venv venv
    ```
5. Activate `venv`
    >Linux
    ```
    . ./venv/bin/activate
    ```
    >Windows
    ```
    venv/Scripts/activate.ps1
    ```
5. All necessary libraries are described in the "requirements.txt" file. Install them by command
    ```
    pip install -r requirements.txt
    ```
6. Tasks 3.1 and 3.3 contain code that interacts with `chromedriver`. 
    >for Windows
    1. To install it, open the website https://sites.google.com/a/chromium.org/chromedriver/downloads and download the version of ChromeDriver that matches the version of your browser.
    2. Create a chromedriver folder on the C: drive and put the previously unzipped chromedriver.exe file in the C: \ chromedriver folder
    3. Add the C: \ chromedriver folder to the PATH system variable.
    >for Linux
    1. To get a link, go to the driver version you need in your browser using the link to https://sites.google.com/a/chromium.org/chromedriver/downloads. On the page that opens, right-click on the file for Linux and copy the path to the file. In the example below, replace the file path for the wget command with your link:
        ```
        wget https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip
        unzip chromedriver_linux64.zip
        ```

    2. Move the unzipped file from the ChromeDriver to the desired folder and allow to run chromedriver as an executable file:

        ```
        sudo mv chromedriver /usr/local/bin/chromedriver
        sudo chown root:root /usr/local/bin/chromedriver
        sudo chmod +x /usr/local/bin/chromedriver
        ```
7. From root folder, run scripts with commands
    >Linux
    ```
    python ./task3-1.py
    python ./task3-2.py
    python ./task3-3.py
    ```
    >Windows
    ```
    python .\task3-1.py
    python .\task3-2.py
    python .\task3-3.py
    ```
