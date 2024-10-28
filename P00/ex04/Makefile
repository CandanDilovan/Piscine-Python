# PYTHON = py
PYTHON = python3
SCRIPT = whatis.py

run: 
	@${PYTHON} ${SCRIPT}
 
lint:
	@flake8 ${SCRIPT}

clean:
#mac - linux
	@find . -type d -name "__pycache__" -exec rm -rf {} +

#windows
# @powershell -Command "Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"

