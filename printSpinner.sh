# $1 must be message; $2 must be pid
print_spinner () {
  spin='-\|/'
  i=0
  while kill -0 $2 2>/dev/null
  do
    i=$(( (i+1) %4 ))
    printf "$1 \r${spin:$i:1}"
    sleep .1
  done
  echo "\nDone"
}
