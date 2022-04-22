@REM if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
call conda activate automated-clockfy
python "C:\Users\BlueShift\OneDrive - blueshift.com.br\Projetos\Meus Projetos\AutomatedClockFy\python\main.py"
@REM exit