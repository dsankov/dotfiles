#!/usr/bin/env zsh

###############################
# EXPORT ENVIRONMENT VARIABLE #
###############################

export TERM='rxvt-256color'
export DOTFILES="$HOME/.dotfiles"
export WORKSPACE="$HOME/workspace"

[ -f "$DOTFILES/install_config" ] && source "$DOTFILES/install_config"

# XDG
export XDG_CONFIG_HOME=$HOME/.config
export XDG_DATA_HOME=$XDG_CONFIG_HOME/local/share
export XDG_CACHE_HOME=$XDG_CONFIG_HOME/cache

# editor
export EDITOR="nano"
export VISUAL="nvim"

# zsh
export ZDOTDIR="$XDG_CONFIG_HOME/zsh"

# Define Zim location
export ZIM_CONFIG_FILE=~/.config/zsh/zimrc.zsh
export ZIM_HOME=${XDG_DATA_HOME:-${HOME}/.local/share}/zim
