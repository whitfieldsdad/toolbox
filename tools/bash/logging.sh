#!/bin/bash

# shellcheck disable=SC2034
HAPPY_FACE="ᕕ(ᐛ)ᕗ"
EXCITED_FACE="(๑˃̵ᴗ˂̵)و"
SAD_FACE="▐﹒︣ Ĺ̯ ﹒︣▐"

function log_info () {
  printf "[-] %s\n" "${1}"
}

function log_success () {
  printf "[✓] %s\n" "${1}"
}

function log_ok () {
  log_success "${1}"
}

function log_error () {
  printf "[✖] %s\n" "${1}"
}

function log_file_not_found () {
  log_error "File not found: ${1}"
}
