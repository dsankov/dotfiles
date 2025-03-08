# theme.zsh - Theme and appearance settings

# PowerLevel10k configuration
# Determine terminal capabilities
{
  if ! zmodload zsh/langinfo zsh/terminfo ||
     [[ $langinfo[CODESET] != (utf|UTF)(-|)8 || $TERM == (dumb|linux) ]] ||
     (( terminfo[colors] < 256 )); then
    # Don't use the powerline config on unsupported terminals
    USE_POWERLINE=false
    # Define alias `x` if our parent process is `login`
    local parent
    if { parent=$(</proc/$PPID/comm) } && [[ ${parent:t} == login ]]; then
      alias x='startx ~/.xinitrc'
    fi
  else
    USE_POWERLINE=true
  fi
} 2>/dev/null

if [[ $USE_POWERLINE == false ]]; then
  # Use 8 colors and ASCII
  source /usr/share/zsh/p10k-portable.zsh
  ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=black,bold'
else
  # Use 256 colors and Unicode
  source $ZDOTDIR/p10k.zsh
  ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=244'
fi

# Color settings for man pages
export LESS_TERMCAP_mb=$'\E[01;32m'
export LESS_TERMCAP_md=$'\E[01;32m'
export LESS_TERMCAP_me=$'\E[0m'
export LESS_TERMCAP_se=$'\E[0m'
export LESS_TERMCAP_so=$'\E[01;47;34m'
export LESS_TERMCAP_ue=$'\E[0m'
export LESS_TERMCAP_us=$'\E[01;36m'
export LESS=-R

# File and Dir colors for ls and other outputs
export LS_OPTIONS='--color=auto'
eval "$(dircolors -b)"
