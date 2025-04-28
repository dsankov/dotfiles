# .zshrc - Main configuration file
#!/usr/bin/env zsh

# XDG Base Directory Specification
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"
export ZDOTDIR="$XDG_CONFIG_HOME/zsh"

# Enable Powerlevel10k instant prompt
(( ${+commands[direnv]} )) && emulate zsh -c "$(direnv export zsh)"

if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

(( ${+commands[direnv]} )) && emulate zsh -c "$(direnv hook zsh)"

# Basic zsh settings
export EDITOR=/usr/bin/nvim
export VISUAL=/usr/bin/nano
WORDCHARS=${WORDCHARS//\/[&.;]}

# Define Zim location
export ZIM_CONFIG_FILE=~/.config/zsh/zimrc.zsh
export ZIM_HOME=${XDG_DATA_HOME:-${HOME}/.local/share}/zim
# Download zimfw plugin manager if missing.
if [[ ! -e ${ZIM_HOME}/zimfw.zsh ]]; then
  curl -fsSL --create-dirs -o ${ZIM_HOME}/zimfw.zsh \
      https://github.com/zimfw/zimfw/releases/latest/download/zimfw.zsh
fi

# Install missing modules and update ${ZIM_HOME}/init.zsh if missing or outdated.
if [[ ! ${ZIM_HOME}/init.zsh -nt ${ZIM_CONFIG_FILE:-${ZDOTDIR:-${HOME}}/.zimrc} ]]; then
  source ${ZIM_HOME}/zimfw.zsh init
fi

# Initialize modules.
source ${ZIM_HOME}/init.zsh

# Source all config files (order matters)
source ${ZDOTDIR}/aliases.zsh
# source ${ZDOTDIR}/completion.zsh
source ${ZDOTDIR}/functions.zsh
source ${ZDOTDIR}/history.zsh
source ${ZDOTDIR}/keybindings.zsh
# source ${ZDOTDIR}/plugins.zsh  # This now sources Zimfw instead of Zinit
source ${ZDOTDIR}/theme.zsh
source ${ZDOTDIR}/fzf.zsh

zle_highlight=('paste:none')
setopt interactive_comments


# Initialize tools
eval "$(zoxide init zsh)"
eval "$(atuin init zsh --disable-ctrl-r)"

# To customize prompt, run `p10k configure` or edit ~/.config/zsh/p10k.zsh.
[[ ! -f $ZDOTDIR/p10k.zsh ]] || source $ZDOTDIR/p10k.zsh
