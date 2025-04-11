# .zshrc - Main configuration file
#!/usr/bin/env zsh

# XDG Base Directory Specification
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"
export ZDOTDIR="$XDG_CONFIG_HOME/zsh"

# Enable Powerlevel10k instant prompt
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Basic zsh settings
export EDITOR=/usr/bin/nvim
export VISUAL=/usr/bin/nano
WORDCHARS=${WORDCHARS//\/[&.;]}

# Load configuration modules
source "$ZDOTDIR/history.zsh"
source "$ZDOTDIR/completion.zsh"
source "$ZDOTDIR/keybindings.zsh"
source "$ZDOTDIR/plugins.zsh"
source "$ZDOTDIR/fzf.zsh"
source "$ZDOTDIR/aliases.zsh"
source "$ZDOTDIR/functions.zsh"
source "$ZDOTDIR/theme.zsh"

zle_highlight=('paste:none')
setopt interactive_comments


# Initialize tools
eval "$(zoxide init zsh)"
eval "$(atuin init zsh --disable-ctrl-r)"

# To customize prompt, run `p10k configure` or edit ~/.config/zsh/p10k.zsh.
[[ ! -f $ZDOTDIR/p10k.zsh ]] || source $ZDOTDIR/p10k.zsh
