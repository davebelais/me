SHELL := bash
.PHONY: docs

# Install and build documentation + PDFs
build:
	{ hatch --version || pipx install --upgrade hatch || python3 -m pip install --upgrade hatch ; } && \
	make install && \
	hatch run python scripts/create_resume_variations.py && \
	make pdf


# Create environment
install:
	{ hatch --version || pipx install --upgrade hatch || python3 -m pip install --upgrade hatch ; } && \
	hatch env create default && \
	echo "Install complete"

# Build PDFs
pdf:
	{ hatch --version || pipx install --upgrade hatch || python3 -m pip install --upgrade hatch ; } && \
	hatch run python scripts/md2pdf.py && \
	{ rm docs/resume.html || true ; } && \
	mv docs/index.html docs/resume.html && \
	{ rm docs/resume.pdf || true ; } && \
	mv docs/index.pdf docs/resume.pdf && \
	hatch run python scripts/md2pdf.py '../resume/*.md' && \
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
