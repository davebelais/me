SHELL := bash
.PHONY: docs

# Create environment
install:
	{ hatch --version || pipx install --upgrade hatch || python3 -m pip install --upgrade hatch ; } && \
	npm install -g chromehtml2pdf && \
	echo "Install complete"

# Build resumes
build:
	{ hatch --version || pipx install --upgrade hatch || python3 -m pip install --upgrade hatch ; } && \
	hatch run python scripts/md2pdf.py && \
	rm docs/index.html && \
	mv docs/index.pdf docs/resume.pdf && \
	echo "Build complete"

# Re-create all environments
reinstall:
	{ hatch --version || pipx install --upgrade hatch || python3 -m pip install --upgrade hatch ; } && \
	hatch env prune && \
	make && \
	make requirements

# This will upgrade all dependencies, in all environments
upgrade:
	hatch run dependence freeze\
	 --include-pointer /tool/hatch/envs/default\
	 --include-pointer /project\
	 -nv '*'\
	 pyproject.toml > .requirements.txt && \
	hatch run pip install --upgrade --upgrade-strategy eager\
	 -r .requirements.txt && \
	rm .requirements.txt && \
	make requirements

# This will update requirement specifiers to align with the
# package versions installed in each environment, and will align the project
# dependency versions with those installed in the default environment
requirements:
	hatch run dependence update\
	 --include-pointer /tool/hatch/envs/default\
	 --include-pointer /project\
	 pyproject.toml && \
	echo "Requirements Updated"

# Build the documentation and serve it locally
docs:
	make build && \
	hatch run mkdocs build && \
	hatch run mkdocs serve

# Cleanup untracked files
clean:
	git clean -f -e .vscode -e .idea -x .

# Apply formatting rules and perform static analysis and type checking
format:
	hatch fmt --formatter
	hatch fmt --linter
	hatch run mypy && \
	echo "Formatting Successful"
