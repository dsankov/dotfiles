# completion.zsh - Completion system configuration

# Initialize the completion system
autoload -U compinit colors
compinit -d "$XDG_CACHE_HOME/zsh/zcompdump-$ZSH_VERSION"
colors

# Options
setopt CORRECT                  # Auto correct mistakes
setopt EXTENDEDGLOB             # Extended globbing. Allows using regular expressions with *
setopt NOCASEGLOB               # Case insensitive globbing
setopt RCEXPANDPARAM            # Array expansion with parameters
setopt NUMERICGLOBSORT          # Sort filenames numerically when it makes sense
setopt NO_BEEP

# Completion styling
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' # Case insensitive tab completion
# zstyle ':completion:*' menu select  # Highlight menu selection

# FZF Tab configuration
# zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'
zstyle ':fzf-tab:complete:__zoxide_z:*' fzf-preview 'ls --color $realpath'
#styling from [jeffry.in/lightweight-intelligent-completion-in-zsh](https://jeffry.in/lightweight-intelligent-completion-in-zsh)
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'eza -1 --color=always $realpath'
zstyle ':fzf-tab:complete:git-(add|diff|restore):*' fzf-preview 'git diff $word | delta'
zstyle ':fzf-tab:complete:git-log:*' fzf-preview 'git log --color=always $word'
zstyle ':fzf-tab:complete:git-help:*' fzf-preview 'git help $word | bat -plman --color=always'
zstyle ':fzf-tab:complete:git-show:*' fzf-preview 'case "$group" in "commit tag") git show --color=always $word ;; *) git show --color=always $word | delta ;; esac'
zstyle ':fzf-tab:complete:git-checkout:*' fzf-preview 'case "$group" in "modified file") git diff $word | delta ;; "recent commit object name") git show --color=always $word | delta ;; *) git log --color=always $word ;; esac'
zstyle ':fzf-tab:*' switch-group '<' '>'

# Speed up completions
zstyle ':completion:*' accept-exact '*(N)'
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path "$XDG_CACHE_HOME/zsh/zcompcache"

zstyle ':completion:*:git-checkout:*' sort false
zstyle ':completion:*:descriptions' format '[%d]'
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' menu no
zstyle ':completion:*' list-max-items 20

