is_sourced() {
  if [ -n "$ZSH_VERSION" ]; then
    case $ZSH_EVAL_CONTEXT in *:file:*) return 0 ;; esac
  else
    case ${0##*/} in dash | -dash | bash | -bash | ksh | -ksh | sh | -sh) return 0 ;; esac
  fi
  return 1
}

read_env_file() {
  # shellcheck disable=SC2046
  export $(grep -E -v '^#' "$1" | xargs)
}
