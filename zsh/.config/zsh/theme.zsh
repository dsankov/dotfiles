# theme.zsh - Theme and appearance settings

# PowerLevel10k configuration remains the same since it's independent of the framework
{
  if ! zmodload zsh/langinfo zsh/terminfo ||
     [[ $langinfo[CODESET] != (utf|UTF)(-|)8 || $TERM == (dumb|linux) ]] ||
     (( terminfo[colors] < 256 )); then
    USE_POWERLINE=false
    local parent
    if { parent=$(</proc/$PPID/comm) } && [[ ${parent:t} == login ]]; then
      alias x='startx ~/.xinitrc'
    fi
  else
    USE_POWERLINE=true
  fi
} 2>/dev/null

if [[ $USE_POWERLINE == false ]]; then
  source /usr/share/zsh/p10k-portable.zsh
  ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=black,bold'
else
  source ${ZDOTDIR}/p10k.zsh
  ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=244'
fi

# The rest of your theme.zsh can remain the same
export LESS_TERMCAP_mb=$'\E[01;32m'
export LESS_TERMCAP_md=$'\E[01;32m'
export LESS_TERMCAP_me=$'\E[0m'
export LESS_TERMCAP_se=$'\E[0m'
export LESS_TERMCAP_so=$'\E[01;47;34m'
export LESS_TERMCAP_ue=$'\E[0m'
export LESS_TERMCAP_us=$'\E[01;36m'
export LESS=-R

export LS_OPTIONS='--color=auto'
eval "$(dircolors -b)"
