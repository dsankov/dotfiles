# +----+
# | ls |
# +----+

# alias ls='ls --color=auto'
alias ls='eza --icons=always'
alias l='eza --icons=always -l -F -g'
alias ll='ls -lahF'
alias lls='ls -lahFtr'
alias la='ls -A'
alias lc='ls -CF'
alias tree="ls --tree"


# zoxide
alias zz='z -'

# git
alias lg="lazygit"

install() {
  local package
  package=$(pamac search "$1" --quiet | awk '{print $1}' | fzf --prompt="Select package: " --height=40% --border --layout=reverse --preview="pamac info {1}")
  [[ -n "$package" ]] && pamac install "$package"
}
