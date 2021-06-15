#!/bin/bash

scp "$@" mhayden@fedorapeople.org:public_html/

echo ""
echo "Spec URL: https://fedorapeople.org/~mhayden/$(basename $1)"
echo "SRPM URL: https://fedorapeople.org/~mhayden/$(basename $2)"
echo "Description: "
echo "Fedora Account System Username: mhayden"
