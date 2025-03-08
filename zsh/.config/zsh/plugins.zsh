# plugins.zsh - Plugins configuration

### Zinit initialization
if [[ ! -f $XDG_DATA_HOME/zinit/zinit.git/zinit.zsh ]]; then
    print -P "%F{33} %F{220}Installing %F{33}ZDHARMA-CONTINUUM%F{220} Initiative Plugin Manager (%F{33}zdharma-continuum/zinit%F{220})…%f"
    command mkdir -p "$XDG_DATA_HOME/zinit" && command chmod g-rwX "$XDG_DATA_HOME/zinit"
    command git clone https://github.com/zdharma-continuum/zinit "$XDG_DATA_HOME/zinit/zinit.git" && \
        print -P "%F{33} %F{34}Installation successful.%f%b" || \
        print -P "%F{160} The clone has failed.%f%b"
fi

source "$XDG_DATA_HOME/zinit/zinit.git/zinit.zsh"
autoload -Uz _zinit
(( ${+_comps} )) && _comps[zinit]=_zinit

# Load important annexes
zinit light-mode for \
    zdharma-continuum/zinit-annex-as-monitor \
    zdharma-continuum/zinit-annex-bin-gem-node \
    zdharma-continuum/zinit-annex-patch-dl \
    zdharma-continuum/zinit-annex-rust

# Load plugins
zinit light zsh-users/zsh-autosuggestions
zinit light zdharma-continuum/fast-syntax-highlighting
zinit snippet OMZP::git
zinit snippet OMZP::sudo
zinit light Aloxaf/fzf-tab
zinit ice depth=1; zinit light romkatv/powerlevel10k
