#!/bin/bash

while true; do
	echo "Checking for new files..."
	new_files=($(git ls-files --others --exclude-standard))
	
	if [[ ${#new_files[@]} -eq 0 ]]; then
		echo "There no new files were created"
	else
		git add "${new_files[@]}"
		echo "New files added"
		git commit -m "${new_files[@]}"
		git push
	fi
	
	sleep 30
done
