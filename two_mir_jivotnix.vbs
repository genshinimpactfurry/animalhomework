CreateObject("Wscript.Shell").Run "cmd /c cd /d C:\Users\chief\Desktop\animalhomework && .venv\Scripts\activate && python main.js", 0, False
WScript.Sleep 3000
CreateObject("Wscript.Shell").Run "http://127.0.0.1:5000"