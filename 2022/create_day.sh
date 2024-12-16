#!/bin/zsh

DAY=$1

if [ -d "$DAY" ]; then
  echo "Day $DAY already exists."
  exit 0
fi

mkdir $DAY
cd $DAY
echo "#!/usr/bin/env python" > ${DAY}_1.py
echo "#!/usr/bin/env python" > ${DAY}_2.py

chmod +x ${DAY}_1.py ${DAY}_2.py
touch input