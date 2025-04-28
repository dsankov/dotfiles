# plugins.zsh - Plugins configuration for Zimfw

# Zimfw initialization
if [[ ! -e ${ZIM_HOME}/zimfw.zsh ]]; then
  # Download zimfw script if missing
  curl -fsSL --create-dirs -o ${ZIM_HOME}/zimfw.zsh \
      https://github.com/zimfw/zimfw/releases/latest/download/zimfw.zsh
fi

# Initialize zimfw
if [[ ! ${ZIM_HOME}/init.zsh -nt ${ZDOTDIR:-${HOME}}/.zimrc ]]; then
  source ${ZIM_HOME}/zimfw.zsh init -q
fi

# Module configuration
# Zimfw comes with many built-in modules (see https://github.com/zimfw/zimfw/wiki/Modules)
# We'll enable the ones that match your current plugins:

# Built-in modules that replace your Zinit plugins:
zmodule zsh-users/zsh-autosuggestions
zmodule zdharma-continuum/fast-syntax-highlighting
zmodule romkatv/powerlevel10k --use degit

# Additional modules you might want:
zmodule archive
zmodule git
zmodule input
zmodule termtitle
zmodule utility

# FZF tab completion (not built into Zimfw)
zmodule Aloxaf/fzf-tab

# Initialize Zimfw
source ${ZIM_HOME}/init.zsh
