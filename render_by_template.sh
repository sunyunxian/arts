#!/usr/bin/env bash

year=$(date +%Y)
week_number=$(date +%V) # +V monday is first day of week.
render_file_name="${year}"-"${week_number}".md

function render_template() {
    cat <<EOF >"${year}"/"${render_file_name}"
# ${year}-${week_number}

## Algorithm

## Review

## Tips

## Share
EOF
}

if [ -f "${year}"/"${render_file_name}" ]; then
    echo "File \"${year}/${render_file_name} \" exists"
else
    render_template && echo "render succeed" || echo "render faild"
fi
